<!-- .github/copilot-instructions.md -->

# Repository Instructions for Copilot Chat

## General
- Target **Python 3.12 or newer**; take advantage of the latest `typing` features (PEP 695) and pattern-matching enhancements.
- Write **fully-typed** code with explicit return types and `typing.Annotated` where additional metadata helps.
- Keep modules small and cohesive; favour functions over classes unless state or polymorphism is required.

## Dependency & Environment Management
- Use **`uv`** for everything: create the virtual environment (`uv venv .venv`), add or remove dependencies (`uv pip install …`, `uv pip uninstall …`), lock (`uv lock`), sync (`uv sync`), and build (`uv build`).
- Store all configuration in **`pyproject.toml`**; do **not** create `requirements*.txt`.
- Commit `uv.lock`; never commit `.venv`. Add `.venv/` to `.gitignore`.

## FastMCP / Model Context Protocol
- Use **FastMCP 2.x** (`from fastmcp import FastMCP`) to build servers and tools.
- Decorate tool functions with `@mcp.tool`. Prefer **`async def`** when I/O-bound, otherwise `def` is fine.
- Always wrap `mcp.run()` in:

```python
if __name__ == "__main__":
    mcp.run()
```
so the server starts only when the file is executed directly.

## Project Layout
- Adopt the **src-layout**: place code in `src/<package_name>/`.
- Keep top-level directories minimal: `src/`, `tests/`, `docs/`, `.github/`.
- Enable **namespace-packages** via `pyproject.toml`.

## Tooling & Automation
- **Ruff** (formatter + linter) is the single source of truth for code style (`ruff format`, `ruff check --fix`).
- **Mypy** (strict mode) or Pyright runs in CI for static typing.
- Add a **pre-commit** configuration that runs `ruff`, `mypy`, and (when present) `pytest`.
- Use **commitizen** or a similar tool for Conventional Commits and automated changelogs.

## Logging & Configuration
- Use **`structlog`** with JSON output (good for Azure Monitor).
- Manage settings with **pydantic-settings**; keep secrets in environment variables and provide a `.env.example`.

## Testing
- Use **pytest** (plus `pytest-asyncio` for async code) when tests are requested.
- Do **not** add tests unless the prompt explicitly asks for them.

## CI/CD
- Provide a minimal **GitHub Actions** workflow:  
  1. Set up `uv`,  
  2. `uv sync`,  
  3. `ruff format --check`, `ruff check`, `mypy`,  
  4. run tests (if present).  
- For container builds, push images to **Azure Container Registry**.

## Style Conventions
- Limit lines to **120 chars** (enforced by Ruff).
- Prefer f-strings, `match` statements, and `pathlib.Path` over legacy equivalents.
- Keep error handling explicit; raise custom exceptions where it improves clarity.

---

End of instructions.