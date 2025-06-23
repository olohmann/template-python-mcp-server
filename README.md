# README

This is a template for a Python [MCP](https://docs.anthropic.com/en/docs/mcp) (Model Context Protocol) server based on the [fastmcp](https://github.com/jlowin/fastmcp) library. It is optimized for VS Code setups with GitHub Copilot.

## Getting Started

To get started with this template, clone the repository and replace all occurrences of `TODO-TEMPLATE` with your own values and start implementing your MCP server in [server.py](server.py).

```bash
# Shallow clone the repository
git clone --depth 1
# Remove the .git directory to start fresh
rm -rf .git
# Initialize a new git repository
git init
# Find all TODO-TEMPLATE occurrences in the repository
grep -r "TODO-TEMPLATE" . --exclude=README.md
```

## File Structure

| File/Directory | Purpose |
|----------------|---------|
| [`server.py`](server.py) | Main MCP server implementation using FastMCP with example tools |
| [`pyproject.toml`](pyproject.toml) | Project configuration, dependencies, and tool settings (Ruff) |
| [`uv.lock`](uv.lock) | Locked dependency versions for reproducible builds |
| [`Dockerfile`](Dockerfile) | Container configuration for deployment |
| [`README.md`](README.md) | Project documentation and usage instructions |
| [`LICENSE`](LICENSE) | MIT license file |
| [`.gitignore`](.gitignore) | Git ignore patterns for Python projects |
| [`.editorconfig`](.editorconfig) | Cross-editor code formatting configuration |
| [`.github/`](.github/) | GitHub-specific configuration and workflows |
| └── [`copilot-instructions.md`](.github/copilot-instructions.md) | Coding guidelines for GitHub Copilot |
| └── [`workflows/`](.github/workflows/) | GitHub Actions CI/CD workflows |
| [`.vscode/`](.vscode/) | VS Code workspace configuration |
| └── [`settings.json`](.vscode/settings.json) | VS Code editor settings |
| └── [`tasks.json`](.vscode/tasks.json) | VS Code build and test tasks |
| └── [`extensions.json`](.vscode/extensions.json) | Recommended VS Code extensions |

## Managing Dependencies

This template uses [uv](https://github.com/astral-sh/uv) to manage dependencies.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
