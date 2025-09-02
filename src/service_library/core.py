"""Core functions for the sample service_library package."""

def greet(name: str) -> str:
    """Return a friendly greeting.

    Args:
        name: Person's name.

    Returns:
        A greeting string.
    """
    if not name:
        raise ValueError("name must be non-empty")
    return f"Hello, {name}!"
