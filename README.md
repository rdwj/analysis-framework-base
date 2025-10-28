# analysis-framework-base

**Lightweight foundation package defining shared interfaces and contracts for document analysis frameworks.**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Development Status](https://img.shields.io/badge/status-production-brightgreen)](https://github.com/redhat-ai-americas/analysis-framework-base)

## Overview

`analysis-framework-base` provides abstract base classes and data models that establish a consistent interface across multiple specialized document analysis frameworks. This package serves as the foundation for:

- **xml-analysis-framework** - XML and S1000D technical documentation
- **docling-analysis-framework** - PDF, Word, PowerPoint via Docling
- **document-analysis-framework** - General document processing
- **data-analysis-framework** - Structured data analysis

## Key Features

- **Zero Dependencies** - Pure Python standard library only
- **Type Hints** - Full typing support for better IDE integration
- **Multiple Access Patterns** - Dict-style and attribute-style access
- **Extensible** - Easy to implement new frameworks
- **Well Documented** - Comprehensive docstrings and examples

## Installation

```bash
pip install analysis-framework-base
```

### For Development

```bash
pip install analysis-framework-base[dev]
```

## Quick Start

### Implementing a Framework Analyzer

```python
from analysis_framework_base import (
    BaseAnalyzer,
    UnifiedAnalysisResult,
    UnsupportedFormatError,
    AnalysisError
)

class MyDocumentAnalyzer(BaseAnalyzer):
    """Custom analyzer for my document format."""

    def analyze_unified(self, file_path: str, **kwargs) -> UnifiedAnalysisResult:
        """Analyze a document and return unified results."""
        # Check file format
        if not file_path.endswith('.mydoc'):
            raise UnsupportedFormatError(f"Unsupported format: {file_path}")

        try:
            # Perform analysis
            with open(file_path, 'r') as f:
                content = f.read()

            return UnifiedAnalysisResult(
                document_type="MyDoc Technical Document",
                confidence=0.95,
                framework="my-doc-analyzer",
                metadata={
                    "version": "1.0",
                    "word_count": len(content.split())
                },
                content=content,
                ai_opportunities=[
                    "Document summarization",
                    "Question answering",
                    "Entity extraction"
                ]
            )
        except Exception as e:
            raise AnalysisError(f"Analysis failed: {e}")

    def get_supported_formats(self) -> list[str]:
        """Return supported file extensions."""
        return ['.mydoc', '.md']
```

### Implementing a Document Chunker

```python
from analysis_framework_base import (
    BaseChunker,
    ChunkInfo,
    UnifiedAnalysisResult,
    ChunkingError
)

class MyDocumentChunker(BaseChunker):
    """Custom chunker for my document format."""

    def chunk_document(
        self,
        file_path: str,
        analysis: UnifiedAnalysisResult,
        strategy: str = "auto",
        **kwargs
    ) -> list[ChunkInfo]:
        """Split document into chunks."""
        if strategy not in self.get_supported_strategies():
            raise ChunkingError(f"Unknown strategy: {strategy}")

        # Implement chunking logic
        chunks = []
        content = analysis.content or ""

        # Simple paragraph-based chunking
        paragraphs = content.split('\n\n')
        for i, para in enumerate(paragraphs):
            chunk = ChunkInfo(
                chunk_id=f"{file_path}_chunk_{i:04d}",
                content=para.strip(),
                metadata={
                    "paragraph_index": i,
                    "source_file": file_path
                },
                token_count=len(para.split()) * 1.3,  # Rough estimate
                chunk_type="paragraph"
            )
            chunks.append(chunk)

        return chunks

    def get_supported_strategies(self) -> list[str]:
        """Return supported chunking strategies."""
        return ['auto', 'paragraph', 'sliding_window']
```

### Using the Framework

```python
# Initialize analyzer
analyzer = MyDocumentAnalyzer()

# Analyze a document
result = analyzer.analyze_unified('document.mydoc')

# Access results (multiple patterns supported)
print(result.document_type)           # Attribute access
print(result['confidence'])           # Dict-style access
print(result.get('framework'))        # Dict get method

# Convert to dict for JSON serialization
result_dict = result.to_dict()

# Initialize chunker
chunker = MyDocumentChunker()

# Chunk the document
chunks = chunker.chunk_document('document.mydoc', result, strategy='paragraph')

# Process chunks
for chunk in chunks:
    print(f"Chunk {chunk.chunk_id}: {chunk.token_count} tokens")
    print(chunk.content[:100])  # First 100 chars
```

## Core Interfaces

### BaseAnalyzer

Abstract base class for document analyzers. Requires implementation of:

- `analyze_unified(file_path: str, **kwargs) -> UnifiedAnalysisResult`
- `get_supported_formats() -> List[str]`

### BaseChunker

Abstract base class for document chunkers. Requires implementation of:

- `chunk_document(file_path: str, analysis: UnifiedAnalysisResult, strategy: str, **kwargs) -> List[ChunkInfo]`
- `get_supported_strategies() -> List[str]`

## Data Models

### UnifiedAnalysisResult

Standard result structure with:

- `document_type: str` - Human-readable document type
- `confidence: float` - Confidence score (0.0-1.0)
- `framework: str` - Framework identifier
- `metadata: Dict[str, Any]` - Framework-specific metadata
- `content: Optional[str]` - Extracted text content
- `ai_opportunities: List[str]` - Suggested AI use cases
- `raw_analysis: Dict[str, Any]` - Complete framework results

Supports both attribute and dict-style access:

```python
result.document_type        # Attribute
result['document_type']     # Dict-style
result.get('document_type') # Get method
'document_type' in result   # Contains check
```

### ChunkInfo

Standard chunk structure with:

- `chunk_id: str` - Unique identifier
- `content: str` - Chunk text content
- `metadata: Dict[str, Any]` - Chunk metadata
- `token_count: int` - Estimated token count
- `chunk_type: str` - Type (text, code, table, etc.)

## Exception Hierarchy

```python
FrameworkError                  # Base exception
├── UnsupportedFormatError     # File format not supported
├── AnalysisError              # Analysis failed
└── ChunkingError              # Chunking failed
```

## Constants

### ChunkStrategy Enum

Standard chunking strategy names:

- `AUTO` - Framework auto-selects best strategy
- `HIERARCHICAL` - Structure-based (sections, headings)
- `SLIDING_WINDOW` - Fixed-size overlapping chunks
- `CONTENT_AWARE` - Semantic boundary detection
- `STRUCTURAL` - Element-based (paragraphs, tables)
- `TABLE_AWARE` - Special table handling
- `PAGE_AWARE` - Page-boundary chunking

```python
from analysis_framework_base import ChunkStrategy

strategy = ChunkStrategy.HIERARCHICAL
print(strategy.value)  # 'hierarchical'
```

## Framework Suite

This package is part of a suite of analysis frameworks:

- **xml-analysis-framework** - 29+ specialized XML handlers, S1000D support, hierarchical chunking
- **docling-analysis-framework** - PDF, DOCX, PPTX via Docling, table-aware chunking
- **document-analysis-framework** - General document processing, format detection
- **data-analysis-framework** - CSV, JSON, Parquet with query paradigm

Each framework implements the interfaces defined in this package for consistent usage.

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/redhat-ai-americas/analysis-framework-base.git
cd analysis-framework-base

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v

# Generate HTML coverage report
pytest --cov-report=html
```

### Code Quality

```bash
# Format code
black src/ tests/

# Check formatting
black --check src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Standards

- Follow PEP 8 style guidelines
- Add type hints to all functions
- Write comprehensive docstrings
- Include examples in docstrings
- Maintain test coverage above 80%
- Keep the package dependency-free (stdlib only)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/redhat-ai-americas/analysis-framework-base/issues)
- **Documentation**: [GitHub Repository](https://github.com/redhat-ai-americas/analysis-framework-base)

## Authors

Red Hat AI Americas Team

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.
