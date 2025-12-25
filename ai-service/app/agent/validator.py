def validate_query(query: str) -> bool:
    return "FROM" in query and "SHOW" in query
