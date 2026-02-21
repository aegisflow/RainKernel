## 📁 CONTRIBUTING.md

```markdown
# 🌍 Contributing to Rain Kernel

Thank you for considering contributing to Rain Kernel! **Every contribution helps build a more sustainable, resilient future for data.**

---

## 🧬 How to Contribute

### 1. Fork the Repository

```bash
git clone https://github.com/aegisflow/rainkernel.git
cd rain-kernel
```

### 2. Create a Branch

```bash
git checkout -b feature/amazing-feature
```

### 3. Make Your Changes

- Write clean, documented code
- Follow existing code style
- Add tests if applicable
- Update documentation if needed

### 4. Test Locally

```bash
# Run the self-validator
python -m core.validator

# Run benchmarks
python benchmark.py
```

### 5. Commit and Push

```bash
git add .
git commit -m "feat: add amazing feature"
git push origin feature/amazing-feature
```

### 6. Open a Pull Request

- Go to the repository on GitHub
- Click **"New Pull Request"**
- Fill in the PR template
- Wait for review (usually within 48h)

---

## 📋 What You Can Contribute

| Type | Description | Difficulty |
|------|-------------|------------|
| 🐛 **Bug Fixes** | Fix issues labeled `bug` | Easy |
| 🧬 **New Morphologies** | Add encoding rules to `core/codec.py` | Medium |
| 📊 **Benchmarks** | Test on new data types | Easy |
| 🌐 **Translations** | Translate README/docs to your language | Easy |
| ✨ **New Features** | Implement features from roadmap | Hard |
| 📖 **Documentation** | Improve guides, examples, comments | Easy |
| 🔒 **Security** | Report vulnerabilities responsibly | Medium |

---

## 🎯 Good First Issues

Looking to contribute but not sure where to start? Check these:

- [ ] Add benchmark for new data type
- [ ] Translate README to your language
- [ ] Create example notebook
- [ ] Improve error messages
- [ ] Add more semantic tokens to `compression.py`

[🔍 View All Issues](../../issues)

---

## 📐 Code Style

### Python Style

- Follow **PEP 8** guidelines
- Use **type hints** for all functions
- Write **docstrings** for public methods
- Keep functions **small and focused**

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Modules | `snake_case` | `data_codec.py` |
| Classes | `PascalCase` | `DataCodec` |
| Functions | `snake_case` | `encode_payload()` |
| Constants | `UPPER_CASE` | `COMMON_TOKENS` |

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new morphology type
fix: correct signature validation bug
docs: update README with new benchmarks
test: add resilience test cases
refactor: improve compression efficiency
```

---

## 🧪 Testing

### Required Tests

Before submitting a PR, ensure:

```bash
# Self-validator passes
python -m core.validator

# Benchmark runs without errors
python benchmark.py
```

### Optional Tests

```bash
# Test specific module
python -c "from core.codec import DataCodec; print('OK')"
```

---

## 📖 Documentation

When adding new features:

1. **Update README.md** if public API changes
2. **Add docstrings** to all new functions
3. **Update docs/** if architecture changes
4. **Add examples** for new morphologies

---

## 🛡️ Security

### Reporting Vulnerabilities

- **Do NOT** open a public issue for security vulnerabilities
- Email: [YOUR_EMAIL_HERE]
- Or use GitHub's **private vulnerability reporting**

### Security Best Practices

- Never commit secrets or API keys
- Use `.gitignore` for local configs
- Review dependencies for vulnerabilities

---

## 🏆 Recognition

Contributors are recognized in:

- [CONTRIBUTORS.md](CONTRIBUTORS.md) — All contributors list
- [README.md](README.md) — Contributors section
- GitHub **Contributors Graph** — Automatic tracking

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the **MIT License**.

---

## 🙏 Thank You

**Every contribution matters.** Whether it's a typo fix, a new feature, or a bug report — you're helping build a more sustainable future for data.
