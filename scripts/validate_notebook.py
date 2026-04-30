"""Static notebook validation.

Checks:
- Notebook file is valid JSON.
- It has a cells list.
- Python code cells parse successfully with ast.

This script does not execute notebook cells and does not require the dataset.
"""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path


def validate_notebook(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Notebook not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        notebook = json.load(file)

    cells = notebook.get("cells")
    if not isinstance(cells, list):
        raise ValueError("Invalid notebook: missing cells list")

    code_cells = 0

    for index, cell in enumerate(cells, start=1):
        if cell.get("cell_type") != "code":
            continue

        code_cells += 1
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)

        try:
            ast.parse(source)
        except SyntaxError as exc:
            raise SyntaxError(
                f"Syntax error in code cell {index}: {exc.msg} at line {exc.lineno}"
            ) from exc

    if code_cells == 0:
        raise ValueError("Notebook has no code cells")

    print(f"OK: {path} ({len(cells)} cells, {code_cells} code cells)")


def main() -> int:
    notebook_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "generative-ai-tools-platforms-2025-eda-baseline.ipynb"
    )
    validate_notebook(notebook_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
