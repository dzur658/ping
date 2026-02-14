import asyncio
import httpx
import sys
from typing import Optional
from langchain_core.tools import tool
from playwright.async_api import async_playwright
from unstructured.partition.html import partition_html
from unstructured.documents.elements import Title
from unstructured.documents.elements import NarrativeText, Text
from unstructured.staging.base import elements_to_json

from ..config import SEARXNG_URL, MAX_SEARCH_RESULTS


def add_markdonwn(text: str, element_class: str) -> str:
    """
    Adds markdown formatting based on the element class.
    """
    if element_class == "Title":
        return f"## {text}"
    elif element_class == "Text":
        return f"*{text}*"
    else:
        # NarrativeText and all others as standard text
        return text


# --- 2. The Python Functions that Implement the Tool ---


async def get_and_parse_page(url: str) -> tuple[Optional[str], str]:
    """
    Uses Playwright to browse to a URL and unstructured to parse its content.
    Returns a tuple of (clean_text, url).
    """
    # Using stderr for progress logs so stdout can be clean for piping
    # print(f"  > Parsing: {url}", file=sys.stderr)
    try:
        async with async_playwright() as p:
            # spoof the user agent to avoid bot detection
            # DO NOT abuse sites! Be mindful and send requests at human speeds.
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

            # We use Chromium. You must run `playwright install chromium` first.
            browser = await p.chromium.launch()
            page = await browser.new_page(user_agent=user_agent)
            await page.goto(url, timeout=10000)

            # Get the fully rendered HTML
            html_content = await page.content()
            await browser.close()

            # Use 'unstructured' to parse the HTML
            # This is "schema-less" - it finds the main content automatically.
            elements = partition_html(text=html_content)

            # Filter for just the useful text elements
            clean_text_parts = []
            for e in elements:
                # Title, NarrativeText, and Text are good general-purpose elements
                if isinstance(e, (Title, NarrativeText, Text)):
                    clean_text_part = add_markdonwn(e.text, e.__class__.__name__)

                    clean_text_parts.append(clean_text_part)

            clean_text = "\n".join(clean_text_parts)

            if not clean_text:
                # print(f"  > No text found at: {url}", file=sys.stderr)
                return None, url

            return clean_text, url

    except Exception as e:
        # print(f"  > Error parsing {url}: {e}", file=sys.stderr)
        return None, url


@tool
async def search_web(
    query: str, searxng_url: str = SEARXNG_URL, max_results: int = MAX_SEARCH_RESULTS
) -> str:
    """
    Search the web for device-specific information, menu locations, troubleshooting steps, or current details.

    Use this tool when the knowledge base doesn't have enough information to answer the user's question,
    or when you need to verify current/updated information about a device.

    Args:
        query: The search query describing what information is needed
        searxng_url: The SearXNG search endpoint URL
        max_results: Maximum number of search results to process

    Returns:
        Formatted search results as markdown with page sources
    """
    print(f"\n--- 1. Searching SearXNG for: '{query}' ---", file=sys.stderr)

    # --- Step 1: Query SearXNG ---
    urls = []
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                searxng_url,
                params={"q": query, "format": "json"},
                headers={"Accept": "application/json"},
                timeout=10,
            )
            response.raise_for_status()  # Raise error for bad responses
            results = response.json()

            # Extract URLs from the results
            urls = [r["url"] for r in results.get("results", [])]
            if not urls:
                return "No search results found."

            # Limit to top N results
            urls = urls[:max_results]

            # print(f"--- 2. Found {len(urls)} URLs. Starting parser... ---", file=sys.stderr)

    except Exception as e:
        # print(f"Error querying SearXNG: {e}", file=sys.stderr)
        return f"Error querying SearXNG: {e}"

    # --- Step 2 & 3: Browse and Parse all pages concurrently ---
    tasks = [get_and_parse_page(url) for url in urls]

    parsed_results = await asyncio.gather(*tasks)

    # --- Step 4: Format the output for the LLM ---
    final_output = []
    for text, url in parsed_results:
        if text:
            # Format as context for the LLM
            final_output.append(
                f"<begin_page>\n<source url={url} />\n{text}\n\n"
                + "\n</end_page>"
                + "\n"
            )

    # print(f"--- 3. Parsing complete. Returning content. ---", file=sys.stderr)
    # Return a single string of all context
    return "\n".join(final_output)


async def direct_load(url: str) -> str:
    """
    Directly load and parse a single URL using Playwright and Unstructured.
    This bypasses the SearXNG search step.
    """
    text, parsed_url = await get_and_parse_page(url)
    if text:
        return (
            f"<begin_page>\n<source url={parsed_url} />\n{text}\n\n"
            + "\n</end_page>"
            + "\n"
        )
    else:
        return f"<connection_refused>No content found at {parsed_url}.</connection_refused>"


if __name__ == "__main__":
    # This allows you to test the tool directly from the command line
    # Usage: python tool_prototype.py "your search query"
    if len(sys.argv) < 2:
        print('Usage: python tool_prototype.py "<search query>"', file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]

    # print(f"Testing search_web with query: '{query}'", file=sys.stderr)

    async def test_run():
        # The script will now print the *clean output* to stdout
        # and logs to stderr.
        output = await search_web(query, SEARXNG_URL, MAX_SEARCH_RESULTS)
        # print(output) # This prints the final result to stdout

        with open("results.md", "w", encoding="utf-8") as f:
            f.write(output)

    async def direct_load_test():
        output = await direct_load(query)
        with open("direct_results.md", "w", encoding="utf-8") as f:
            f.write(output)

    if "http://" not in query and "https://" not in query:
        asyncio.run(test_run())
    else:
        asyncio.run(direct_load_test())
