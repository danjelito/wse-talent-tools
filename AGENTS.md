# AGENTS.md

## Coding Agent Guide – Project: TO Tools and Calculator

Welcome! Coding agents contributing to this Python/Streamlit project should follow the practices below. This file provides commands, inferred code style, best practices for error handling and documentation, and guidance for linting/testing. Keep code readable, robust, and user-friendly!

---

## 1. Running & Development Commands

### 1.1. Installation

```bash
uv venv .venv
source .venv/bin/activate
uv pip install --upgrade pip
uv pip install -r requirements.txt
```

Or, if you prefer global install for development (not recommended for production/repo scripts):
```bash
uv pip install -r requirements.txt
```

### 1.2. Running the Application

Main entry point is:

```bash
streamlit run Home.py
```

### 1.3. Build & Deployment

- No dedicated build system. Deploy via Streamlit or your chosen Python host.
- `pyproject.toml` and `requirements.txt` define dependencies.

### 1.4. Linting

- No enforced linter. *Strongly recommend* using `black` with default settings. To install and run, use:
  ```bash
  uv install black
  ```
- You may also check imports with `isort` or lint code with `flake8` (not enforced, but desirable):
  ```bash
  uv install isort flake8
  ```

### 1.5. Testing

- **No formal tests defined.**
- Testable logic may appear under `if __name__ == "__main__":` blocks in source files.
- If you add or run tests, prefer [pytest](https://docs.pytest.org/) with functions named `test_*`.
  ```bash
  uv install pytest
  ```
- To add a new test, create a file under `test/` with prefix `test_`, or convert/integrate commented demo code as setup for pytest.

---

## 2. Code Style Guidelines

### 2.1. Imports
- Use absolute imports (no relative dots), in this order:
  1. Standard Library
  2. Third-party
  3. Local application code
- Blank line between groups.

### 2.2. Formatting/Spacing
- Use 4 space indentation.
- Match [PEP8](https://www.python.org/dev/peps/pep-0008/): blank lines between function/class defs, max line length 79/88 where possible.
- Align assignment and keyword args for readability.

### 2.3. Naming
- Functions and variables: `snake_case`.
- Modules: `snake_case.py`.
- Classes (if any): `CamelCase`.
- Constants (rare): `ALL_CAPS`.

### 2.4. Types & Docstrings
- Use type hints for new/complex functions. Legacy code may lack them, but new agents should annotate as feasible.
- All public functions should have docstrings. One-line triple-quoted (`"""."""`) docstrings are acceptable for simple cases.

### 2.5. Comments
- Above complex logic, or to explain business rules.
- Use `# Inline comments` after at least two spaces.

### 2.6. Error Handling
- Use return `None` or default values for not-found/null situations (see `find_tax_percentage`).
- Validate arguments. Raise `ValueError` for invalid kinds/values.
- In UI components, use Streamlit’s `st.error`, `st.warning` for user feedback instead of raising exceptions.

---

## 3. Project Patterns & Conventions

- Put core logic in `src/`, UI in `pages/` and `Home.py`.
- Avoid side effects or I/O in import-time code.
- Place any script/test/demo logic under `if __name__ == "__main__":` blocks.

---

## 4. Tests and Continuous Integration

- No CI pipeline or test/lint hooks are currently set up.
- Encourage every agent to:
  1. Add minimal tests for new logic, ideally with pytest.
  2. Use local black/isort/flake8 before PRs.
- “Test” logic found in comments can be adapted into proper test functions as the codebase grows.

---

## 5. Copilot, Cursor, and AI-Specific Rules

- **No `.github/copilot-instructions.md` or `.cursor/rules/` found.**
  - Agents should default to PEP8, Black, and readable, well-documented code for libraries and user interfaces.
  - Write self-explanatory code, good docstrings, and validate arguments thoroughly.
- If Cursor/Copilot rules are added later, integrate/override these accordingly.

---

## 6. General Principles for Agents

- Prioritize user safety, clarity, and maintainability.
- Do not remove existing business logic/documentation unless superseded.
- Prefer backward-compatible enhancements unless a breaking change is required.
- Leave clear TODOs or FIXMEs if a compromise or deliberate technical debt is introduced.

---

## 7. Example Agent Workflow

1. **Install dependencies** as above.
2. **Read source/doc pages** before proposing changes.
3. **Improve code by**:
   - Adding docstrings to undocumented functions.
   - Adding or improving type hints.
   - Reformatting to PEP8/Black where style wavers.
   - Refactoring for readability (splitting long functions, extracting logic).
   - Adding minimal test coverage or converting `__main__` demo code into tests.
4. **Document** any new rules you introduce.
5. **Submit PR or changes with clear summary.**

---

For any questions or new conventions, update this file so future agents stay aligned!
