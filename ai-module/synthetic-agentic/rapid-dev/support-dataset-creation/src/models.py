"""Data models and validation for conversation generation."""

from typing import Optional
from pydantic import BaseModel, Field, field_validator


class ReasoningResponse(BaseModel):
    """Pydantic model for validating assistant responses with reasoning content."""

    reasoning: str = Field(..., description="The internal reasoning content")
    response: str = Field(..., description="The actual response to the user")

    @field_validator("reasoning", "response")
    @classmethod
    def not_empty(cls, v: str) -> str:
        """Validate that fields are not empty or just whitespace."""
        if not v or not v.strip():
            raise ValueError("Field cannot be empty or whitespace only")
        return v

    def to_training_format(self) -> str:
        """Convert to training format with <think> tags."""
        if not self.response:
            return ""
        return f"<think>\n{self.reasoning}\n</think>\n\n{self.response}"

    @classmethod
    def get_json_schema(cls) -> dict:
        """Return the JSON schema for Pydantic validation."""
        return cls.model_json_schema()
