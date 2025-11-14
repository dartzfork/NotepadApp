# Contributing to NotepadApp

Thank you for your interest in contributing to NotepadApp! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors. Please:

- Be respectful and considerate in your communications
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what is best for the community and the project

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- Python 3.7 or higher installed
- Git installed and configured
- A GitHub account
- Basic knowledge of Python and Tkinter

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/NotepadApp.git
   cd NotepadApp
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/dartzfork/NotepadApp.git
   ```

## Development Setup

### Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Optional: Create a virtual environment first
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Application

```bash
python Notepad.py
```

### Testing Your Changes

Before submitting changes:

1. Test the application thoroughly
2. Verify all features work as expected
3. Test on different screen sizes and resolutions if possible
4. Check that your changes don't break existing functionality

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Fixes**: Fix issues reported in the issue tracker
- **New Features**: Add new functionality to the application
- **Documentation**: Improve or add documentation
- **Code Quality**: Refactor code, improve performance, or add tests
- **UI/UX**: Enhance the user interface or user experience

### Workflow

1. **Check existing issues** to see if your contribution is already being discussed
2. **Create an issue** if one doesn't exist for your contribution
3. **Wait for feedback** before starting major work
4. **Create a branch** for your changes
5. **Make your changes** following our coding standards
6. **Test thoroughly** to ensure everything works
7. **Submit a pull request** with a clear description

## Coding Standards

### Python Style Guide

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines:

- Use 4 spaces for indentation (no tabs)
- Limit lines to 79 characters for code, 72 for docstrings/comments
- Use meaningful variable and function names
- Add docstrings to all classes and methods
- Use type hints where appropriate

### Documentation

- Write clear, concise docstrings following [PEP 257](https://www.python.org/dev/peps/pep-0257/)
- Include parameter descriptions and return types
- Add inline comments for complex logic
- Update README.md if adding new features

### Code Organization

- Keep methods focused and single-purpose
- Group related functionality together
- Maintain the existing code structure
- Add comments for non-obvious code

### Example Code Style

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of function.
    
    More detailed description if needed. Explain what the function does,
    why it exists, and any important considerations.
    
    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: When param2 is negative
    """
    if param2 < 0:
        raise ValueError("param2 must be non-negative")
    
    # Implementation with clear logic
    result = process_data(param1, param2)
    return result
```

## Commit Guidelines

### Commit Message Format

Use conventional commit messages:

```
type(scope): subject

body (optional)

footer (optional)
```

### Commit Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring without feature changes
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
feat(ui): add dark mode toggle button

fix(save): resolve file encoding issue on Windows

docs(readme): update installation instructions

refactor(notepad): simplify file opening logic
```

### Best Practices

- Write clear, descriptive commit messages
- Make atomic commits (one logical change per commit)
- Reference issue numbers when applicable (e.g., "fixes #123")
- Keep commits focused and well-organized

## Pull Request Process

### Before Submitting

1. **Update your branch** with the latest upstream changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test thoroughly** to ensure everything works

3. **Update documentation** if you've added features or changed behavior

4. **Verify code quality** by reviewing your own changes

### Creating a Pull Request

1. Push your branch to your fork:
   ```bash
   git push origin your-branch-name
   ```

2. Go to the GitHub repository and create a pull request

3. Fill out the pull request template completely:
   - Clear title describing the change
   - Detailed description of what and why
   - Screenshots or demos for UI changes
   - List of testing performed
   - Reference related issues

4. Link the pull request to related issues using keywords:
   - "Closes #123" or "Fixes #123" for bug fixes
   - "Addresses #123" or "Related to #123" for features

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Changes Made
- Detailed list of changes
- What was added or modified
- Why these changes were necessary

## Testing Performed
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Tested on Linux
- [ ] Verified existing features still work
- [ ] Tested edge cases

## Screenshots (if applicable)
[Add screenshots here]

## Checklist
- [ ] Code follows project style guidelines
- [ ] Documentation has been updated
- [ ] Changes have been tested thoroughly
- [ ] Commit messages follow conventions
- [ ] No breaking changes introduced

## Related Issues
Closes #(issue number)
```

### Review Process

1. **Automated checks** must pass (if configured)
2. **Maintainer review** will be conducted
3. **Address feedback** promptly and professionally
4. **Make requested changes** in new commits
5. **Squashing commits** may be requested before merge

## Reporting Bugs

### Before Reporting

1. Check if the bug has already been reported
2. Verify you're using the latest version
3. Collect relevant information about the issue

### Bug Report Template

When reporting bugs, include:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**:
  - Operating System and version
  - Python version
  - CustomTkinter version
- **Screenshots**: If applicable
- **Additional Context**: Any other relevant information

### Example Bug Report

```markdown
**Description**
Application crashes when opening files with special characters in filename

**Steps to Reproduce**
1. Click "Open" button
2. Select a file with special characters (e.g., "test_ñ.txt")
3. Application crashes

**Expected Behavior**
File should open successfully

**Actual Behavior**
Application crashes with UnicodeDecodeError

**Environment**
- OS: Windows 10
- Python: 3.9.5
- CustomTkinter: 5.2.0

**Screenshots**
[Error screenshot]
```

## Suggesting Features

### Feature Request Guidelines

When suggesting new features:

1. **Check existing requests** to avoid duplicates
2. **Describe the feature** clearly and concisely
3. **Explain the use case** and why it's valuable
4. **Consider implementation** complexity and impact
5. **Provide examples** or mockups if possible

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why is this feature needed? Who will benefit?

**Proposed Solution**
How could this feature be implemented?

**Alternatives Considered**
What other solutions have you considered?

**Additional Context**
Any mockups, examples, or references
```

## Development Tips

### Debugging

- Use print statements or Python's debugger (pdb)
- Test individual methods in isolation
- Check CustomTkinter documentation for widget-specific issues

### Common Pitfalls

- **Tkinter indices**: Text widget uses "1.0" format (line.character)
- **File paths**: Use `os.path` for cross-platform compatibility
- **Encoding**: Always specify encoding when opening files
- **Grid layout**: Ensure proper row/column configuration for expansion

### Useful Resources

- [CustomTkinter Documentation](https://github.com/TomSchimansky/CustomTkinter)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Docstring Conventions (PEP 257)](https://www.python.org/dev/peps/pep-0257/)

## Getting Help

If you need help:

1. Check the [README.md](README.md) for basic information
2. Review existing issues and discussions
3. Open a new issue with your question
4. Be specific and provide context

## Recognition

All contributors will be:

- Listed in the project's contributors page
- Credited in release notes for significant contributions
- Acknowledged in the project documentation

## License

By contributing to NotepadApp, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to NotepadApp! Your efforts help make this project better for everyone.
