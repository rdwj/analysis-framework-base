# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-27

### Added
- Initial release of analysis-framework-base
- `BaseAnalyzer` abstract interface for document analyzers
- `BaseChunker` abstract interface for document chunkers
- `UnifiedAnalysisResult` data model with dict and attribute access patterns
- `ChunkInfo` data model for document chunks
- Exception hierarchy: `FrameworkError`, `UnsupportedFormatError`, `AnalysisError`, `ChunkingError`
- `ChunkStrategy` enum with standard chunking strategies
- Comprehensive documentation and examples
- Full type hints support (Python 3.8+)
- Zero external dependencies (stdlib only)
- pytest test suite with 80%+ coverage
- Apache 2.0 license

### Features
- Multiple access patterns for data models (attribute, dict-style, get methods)
- Full docstring documentation with examples
- Type checking support with mypy
- Black and flake8 code quality standards

[1.0.0]: https://github.com/redhat-ai-americas/analysis-framework-base/releases/tag/v1.0.0
