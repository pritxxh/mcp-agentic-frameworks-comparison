# Contributing to MCP Agentic Frameworks Comparison

Thank you for your interest in contributing! 🎉

## Ways to Contribute

1. ⭐ **Star the repository** - Show your support
2. 🐛 **Report bugs** - Open an issue with details
3. 💡 **Suggest features** - Share your ideas
4. 📝 **Improve documentation** - Fix typos, clarify instructions
5. 🔧 **Submit code** - Add new examples or fix bugs
6. 💬 **Help others** - Answer questions in discussions

## Development Setup

### Prerequisites
- Node.js 18+ (for MCP server)
- Python 3.9+ (for framework implementations)
- Git

### Initial Setup

1. **Fork and clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/mcp-agentic-frameworks-comparison.git
cd mcp-agentic-frameworks-comparison
```

2. **Build the MCP Server**
```bash
cd 01-mcp-server
npm install
npm run build
```

3. **Set up Python environments**
```bash
# LangGraph
cd 02-langgraph-agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env

# Repeat for other frameworks
```

4. **Test your setup**
```bash
# Test MCP server
cd 01-mcp-server
node build/index.js

# Test frameworks
cd 02-langgraph-agent
source venv/bin/activate
python src/workflow.py
```

## Pull Request Process

1. **Create a feature branch**
```bash
git checkout -b feature/amazing-feature
```

2. **Make your changes**
   - Write clean, readable code
   - Follow existing code style
   - Add comments for complex logic

3. **Test your changes**
   - Verify MCP server still builds
   - Test affected framework implementations
   - Check cross-platform compatibility (if applicable)

4. **Commit your changes**
```bash
git add .
git commit -m "Add amazing feature"
```

5. **Push to your fork**
```bash
git push origin feature/amazing-feature
```

6. **Open a Pull Request**
   - Describe what you changed and why
   - Reference related issues
   - Include screenshots for UI changes

## Code Standards

### MCP Server (TypeScript)
- Use TypeScript strict mode
- Follow existing file structure
- Document new tools with JSDoc comments
- Keep tool functions pure (no side effects where possible)

### Framework Implementations (Python)
- Follow PEP 8 style guide
- Use type hints where applicable
- Keep framework-specific code in respective directories
- Document environment variables in .env.example

### Documentation
- Use clear, concise language
- Include code examples
- Keep cross-platform instructions
- Update README.md if adding new features

## Reporting Bugs

When reporting bugs, please include:

1. **Description** - What happened vs. what you expected
2. **Steps to reproduce** - Exact steps to trigger the bug
3. **Environment** - OS, Python version, Node version
4. **Error messages** - Full error output
5. **Screenshots** - If applicable

**Example:**
```markdown
**Bug**: MCP server fails to start on Windows

**Steps to reproduce:**
1. Clone repo
2. Run `npm install` in 01-mcp-server
3. Run `node build/index.js`

**Environment:**
- Windows 11
- Node.js v20.0.0
- npm 10.0.0

**Error:**
[Paste error message here]
```

## Suggesting Features

We love new ideas! When suggesting features:

1. **Check existing issues** - Someone may have already suggested it
2. **Describe the use case** - Why is this feature needed?
3. **Provide examples** - Show what it would look like
4. **Consider alternatives** - Are there other solutions?

## Code Review Process

- Maintainers will review PRs within 3-5 days
- Address review feedback promptly
- Be open to suggestions and improvements
- Once approved, maintainers will merge your PR

## Community Guidelines

- Be respectful and constructive
- Help others learn and grow
- Give credit where credit is due
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)

## Questions?

- 💬 Open a [Discussion](https://github.com/pritxxh/mcp-agentic-frameworks-comparison/discussions)
- 🐛 Open an [Issue](https://github.com/pritxxh/mcp-agentic-frameworks-comparison/issues)
- 📧 Reach out to maintainers

## Recognition

Contributors will be:
- Listed in CHANGELOG.md
- Credited in release notes
- Featured in the README (for significant contributions)

Thank you for making this project better! 🚀
