# Contributing to Body Recomposition Simulator

Thanks for your interest in contributing! This project welcomes pull requests and bug reports from everyone.

## How to Contribute

### Reporting Bugs

1. Check existing [issues](../../issues) to avoid duplicates
2. Open a new issue with:
   - A clear, descriptive title
   - Steps to reproduce the bug
   - Expected vs actual behavior
   - Browser and OS information

### Suggesting Features

Open an issue with the **enhancement** label and describe:

- The problem you're trying to solve
- Your proposed solution
- Any scientific references that support the feature

### Submitting Pull Requests

1. **Fork** the repository
2. **Create a branch** from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Install dependencies**:

   ```bash
   uv sync
   uv sync --group dev
   ```

4. **Install Lefthook hooks**:

   ```bash
   brew install lefthook
   lefthook install
   ```

5. **Make your changes** — keep them focused and minimal
6. **Test locally**:

   ```bash
   uv run streamlit run app.py
   ```

7. **Commit** with a clear message:

   ```bash
   git commit -m "feat: add TDEE chart visualization"
   ```

8. **Push** and open a Pull Request against `main`

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/). Commits are validated by `commitizen` through `lefthook`:

| Prefix | Purpose |
| -------- | --------- |
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `refactor:` | Code restructuring |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks |

## Development Guidelines

- **Scientific accuracy first** — all physiological formulas must cite peer-reviewed sources
- **Keep it simple** — avoid over-engineering; the minimum code for the current task
- **Bilingual** — all user-facing strings must have both English and Portuguese translations in `src/i18n.py`
- **No hardcoded strings** — use the `t()` function from `src/i18n.py`

## Areas Where Help Is Needed

- [ ] Unit tests for simulation formulas (`src/model.py`)
- [ ] Validation against published clinical data
- [ ] Additional languages (Spanish, French, etc.)
- [ ] CSV/PDF export of simulation results
- [ ] TDEE chart visualization (data is already computed)
- [ ] Side-by-side scenario comparison view
- [ ] Female-specific hormonal cycle adjustments
- [ ] Reverse diet mode (gradual calorie increase post-cut)
- [ ] NEAT (Non-Exercise Activity Thermogenesis) as a separate factor

## Code of Conduct

Be respectful, constructive, and inclusive. We're all here to learn and build something useful.

## Questions?

Open an issue or start a discussion — we're happy to help!
