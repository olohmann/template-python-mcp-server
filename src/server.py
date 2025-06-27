"""FastMCP server."""

import signal
import sys

import structlog
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

from .config import McpSettings

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger(__name__)

mcp: FastMCP[None] = FastMCP("MCP on 🔥")


@mcp.tool(annotations={"title": "Divide Numbers", "readOnlyHint": True, "openWorldHint": False})
def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a: The dividend (number to be divided)
        b: The divisor (number to divide by)

    Returns:
        The result of a divided by b
    """
    if b == 0:
        raise ToolError("Cannot divide by zero")

    return a / b


def graceful_exit() -> None:
    """Exit gracefully with a friendly message."""
    logger.info("Server shutting down gracefully")
    print("\n👋 Alpaca MCP server stopped gracefully. Goodbye!")
    sys.exit(0)


def main() -> None:
    """Main entry point for the server."""
    signal.signal(signal.SIGINT, lambda signum, frame: graceful_exit())

    try:
        mcp_settings: McpSettings = McpSettings()  # type: ignore[call-arg]
        logger.info("Starting Alpaca MCP server")

        # Initialize and run the server
        if mcp_settings.transport == "streamable-http":
            mcp.run(transport="streamable-http", host=mcp_settings.host, port=mcp_settings.port)
        elif mcp_settings.transport == "sse":
            mcp.run(transport="sse", host=mcp_settings.host, port=mcp_settings.port)
        else:
            mcp.run(transport="stdio")
    except KeyboardInterrupt:
        graceful_exit()
    except Exception as e:
        logger.error("Unexpected error", error=str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
