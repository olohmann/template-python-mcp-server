import signal
import sys

from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def graceful_exit() -> None:
    """Exit gracefully with a friendly message."""
    print("\n👋 Server stopped gracefully. Goodbye!")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda signum, frame: graceful_exit())

    try:
        mcp.run()
    except KeyboardInterrupt:
        graceful_exit()
