import sqlite3

connection = sqlite3.connect("knowledge/knowledge_base.db")

def load_entry(entry_id: int) -> dict:
    cursor = connection.cursor()
    cursor.execute("SELECT device_name, documentation FROM knowledge WHERE id = ?", (entry_id,))
    result = cursor.fetchone()
    if result:
        return {"id": entry_id, "device_name": result[0], "documentation": result[1]}
    else:
        raise ValueError(f"No entry found with id {entry_id}")

def total_entries() -> int:
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM knowledge")
    result = cursor.fetchone()
    return result[0] if result else 0