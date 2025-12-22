# Contributing to MedPredict

Thank you for your interest in contributing to MedPredict! This document outlines how to contribute effectively.

## 📋 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/MaternalHealth.git
   cd MaternalHealth
   ```
3. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and test thoroughly
5. **Commit with clear messages:**
   ```bash
   git commit -m "Add feature: description of what was added"
   ```
6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** against the main repository

## 🎯 Priority Areas

Refer to [TODO.md](./TODO.md) for high-priority and ongoing work. Key areas needing help:

- **Model Improvements:** Real trained models instead of placeholders
- **UI/UX:** Fetal form redesign, input validation
- **Testing:** Unit tests and integration tests
- **Documentation:** Expand docstrings, add examples
- **Deployment:** Docker, CI/CD, cloud hosting

## ✅ Code Standards

- Follow PEP 8 style guide
- Write clear, descriptive variable and function names
- Add docstrings to new functions and classes
- Include comments for complex logic
- Test changes locally before pushing

## 🧪 Testing

Before submitting a PR:

```bash
# Run the app locally
streamlit run main.py

# Test all sections: About, Pregnancy Risk, Fetal Health, Dashboard
# Verify predictions with known test values
# Check for errors in the terminal
```

## 📝 Commit Message Guidelines

- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Move cursor" not "Moves cursor"
- Start with a capital letter
- Keep messages concise but descriptive
- Reference issues: "Fixes #123" or "Addresses #456"

## 🔄 Pull Request Process

1. Update [TODO.md](./TODO.md) with any completed tasks
2. Update [README.md](./README.md) if documentation changes
3. Ensure all tests pass
4. Request review from maintainers
5. Address feedback promptly

## 📞 Questions?

Open an issue on GitHub or contact the maintainers. We're happy to help!

---

**Thank you for contributing to MedPredict!**
