# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-02

### Added

#### MCP Server
- TypeScript-based MCP server implementation
- 4 contract analysis tools:
  - `summarize_contract` - Extract key points from contracts
  - `analyze_contract` - Examine clauses and identify risks
  - `assess_risk` - Calculate risk scores and levels
  - `send_notification` - Alert stakeholders for high-risk contracts
- Rule-based implementation (fast, predictable, no API costs)
- LLM-enhanced tools example for production use

#### Framework Implementations
- **LangGraph**: State-based workflow with explicit control flow
- **CrewAI**: Role-based multi-agent collaboration system
- **Custom Orchestrator**: Raw Anthropic API implementation for full control

#### Documentation
- Comprehensive README with quick start guide
- Architecture diagram showing all framework approaches
- STARTER_GUIDE with 12 detailed implementation guides
- TROUBLESHOOTING guide for common issues
- Cross-platform instructions (macOS, Windows, Linux)
- Production enhancement recommendations

#### Testing & Examples
- 6 sample contracts with varying risk levels
- Test data with synthetic contract examples
- Example workflows for each framework
- Comparison framework for benchmarking

#### Developer Experience
- Cross-platform setup scripts
- Virtual environment management
- Environment variable configuration (.env.example files)
- Build and test automation

### Documentation
- Created comprehensive README.md
- Added architecture visualization
- Included framework comparison table
- Added external resource links
- Created CONTRIBUTING.md guidelines
- SEO optimization with badges and keywords

### Infrastructure
- MIT License for open-source use
- Git repository structure
- .gitignore for development files
- Package management (npm, pip)

## [Unreleased]

### Planned Features
- GitHub Actions CI/CD pipeline
- Automated testing suite
- Docker containerization
- Additional framework examples (LangChain, AutoGen)
- Web dashboard for comparisons
- Video tutorials and demos

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
