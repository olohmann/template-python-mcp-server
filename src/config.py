"""Configuration settings for the MCP server."""

from enum import Enum
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TransportType(str, Enum):
    """Available MCP transport types."""

    STDIO = "stdio"
    STREAMABLE_HTTP = "streamable-http"
    SSE = "sse"


class McpSettings(BaseSettings):
    """Settings for MCP server configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="MCP_",
        case_sensitive=False,
        extra="ignore",
        frozen=True,
    )

    host: Annotated[str, Field(default="0.0.0.0", description="MCP Host (only if transport != stdio)")]
    port: Annotated[int, Field(default=8080, description="MCP Port (only if transport != stdio)")]
    transport: Annotated[TransportType, Field(default=TransportType.STDIO, description="MCP transport protocol")]
