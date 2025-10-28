"""
Abstract base classes defining the interface for analysis frameworks.

This module provides BaseAnalyzer and BaseChunker interfaces that all
specialized frameworks must implement to ensure consistency.
"""

from abc import ABC, abstractmethod
from typing import List

from .models import UnifiedAnalysisResult, ChunkInfo


class BaseAnalyzer(ABC):
    """
    Abstract base class that all framework analyzers must implement.

    This ensures consistent interface across xml, docling, document, and data frameworks.

    Example:
        >>> class MyAnalyzer(BaseAnalyzer):
        ...     def analyze_unified(self, file_path: str, **kwargs) -> UnifiedAnalysisResult:
        ...         # Implementation here
        ...         return UnifiedAnalysisResult(
        ...             document_type="My Document Type",
        ...             confidence=0.95,
        ...             framework="my-framework"
        ...         )
        ...
        ...     def get_supported_formats(self) -> List[str]:
        ...         return ['.xml', '.pdf']
    """

    @abstractmethod
    def analyze_unified(self, file_path: str, **kwargs) -> UnifiedAnalysisResult:
        """
        Analyze a document and return results in unified format.

        Args:
            file_path: Path to file to analyze
            **kwargs: Framework-specific options

        Returns:
            UnifiedAnalysisResult with standard structure

        Raises:
            UnsupportedFormatError: File format not supported
            AnalysisError: Analysis failed
        """
        pass

    @abstractmethod
    def get_supported_formats(self) -> List[str]:
        """
        Return list of supported file extensions.

        Returns:
            List of extensions like ['.xml', '.pdf', '.docx']

        Example:
            >>> analyzer = MyAnalyzer()
            >>> analyzer.get_supported_formats()
            ['.xml', '.pdf', '.docx']
        """
        pass


class BaseChunker(ABC):
    """
    Abstract base class for document chunking implementations.

    Note: Not all frameworks need to implement this (e.g., data-analysis-framework
    uses a query paradigm instead of traditional chunking).

    Example:
        >>> class MyChunker(BaseChunker):
        ...     def chunk_document(
        ...         self,
        ...         file_path: str,
        ...         analysis: UnifiedAnalysisResult,
        ...         strategy: str = "auto",
        ...         **kwargs
        ...     ) -> List[ChunkInfo]:
        ...         # Implementation here
        ...         return [
        ...             ChunkInfo(
        ...                 chunk_id="chunk_1",
        ...                 content="Content here",
        ...                 token_count=50
        ...             )
        ...         ]
        ...
        ...     def get_supported_strategies(self) -> List[str]:
        ...         return ['auto', 'hierarchical']
    """

    @abstractmethod
    def chunk_document(
        self, file_path: str, analysis: UnifiedAnalysisResult, strategy: str = "auto", **kwargs
    ) -> List[ChunkInfo]:
        """
        Split document into chunks suitable for LLM/RAG applications.

        Args:
            file_path: Path to document
            analysis: Previous analysis result
            strategy: Chunking strategy name
            **kwargs: Framework-specific options

        Returns:
            List of ChunkInfo objects

        Raises:
            ChunkingError: Chunking failed

        Example:
            >>> chunker = MyChunker()
            >>> analysis = UnifiedAnalysisResult(...)
            >>> chunks = chunker.chunk_document(
            ...     '/path/to/doc.xml', analysis, strategy='hierarchical'
            ... )
            >>> len(chunks)
            10
        """
        pass

    @abstractmethod
    def get_supported_strategies(self) -> List[str]:
        """
        Return list of supported chunking strategies.

        Returns:
            List of strategy names like ['auto', 'hierarchical', 'sliding_window']

        Example:
            >>> chunker = MyChunker()
            >>> chunker.get_supported_strategies()
            ['auto', 'hierarchical', 'sliding_window', 'content_aware']
        """
        pass
