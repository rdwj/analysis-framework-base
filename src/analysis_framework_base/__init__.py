"""
analysis-framework-base: Shared interfaces for document analysis frameworks.

This package provides abstract base classes and data models that establish
a consistent interface across multiple specialized analysis frameworks.

The package is designed to be dependency-free, using only Python standard library,
making it a lightweight foundation for framework development.

Example:
    >>> from analysis_framework_base import BaseAnalyzer, UnifiedAnalysisResult
    >>> class MyAnalyzer(BaseAnalyzer):
    ...     def analyze_unified(self, file_path: str, **kwargs) -> UnifiedAnalysisResult:
    ...         return UnifiedAnalysisResult(
    ...             document_type="Example Document",
    ...             confidence=0.95,
    ...             framework="example-framework"
    ...         )
    ...     def get_supported_formats(self):
    ...         return ['.txt', '.md']
"""

__version__ = "1.0.0"

from .interfaces import BaseAnalyzer, BaseChunker
from .models import UnifiedAnalysisResult, ChunkInfo
from .exceptions import (
    FrameworkError,
    UnsupportedFormatError,
    AnalysisError,
    ChunkingError,
)
from .constants import ChunkStrategy

__all__ = [
    "BaseAnalyzer",
    "BaseChunker",
    "UnifiedAnalysisResult",
    "ChunkInfo",
    "FrameworkError",
    "UnsupportedFormatError",
    "AnalysisError",
    "ChunkingError",
    "ChunkStrategy",
]
