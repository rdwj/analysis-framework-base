"""
Shared data models for analysis frameworks.

This module provides UnifiedAnalysisResult and ChunkInfo dataclasses
that establish a consistent data format across frameworks.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional, List


@dataclass
class UnifiedAnalysisResult:
    """
    Standard result structure returned by all framework analyzers.

    This provides a consistent interface regardless of which framework
    performed the analysis.

    Supports multiple access patterns:
    - Dict-style: result['document_type']
    - Attribute-style: result.document_type
    - Dict conversion: result.to_dict()

    Attributes:
        document_type: Human-readable document type (e.g., 'PDF Technical Manual', 'S1000D XML')
        confidence: Confidence score 0.0-1.0 for document type detection
        framework: Framework that performed the analysis (e.g., 'xml-analysis-framework')
        metadata: Framework-specific metadata about the document
        content: Extracted text content (if applicable)
        ai_opportunities: Suggested AI/ML use cases for this document
        raw_analysis: Complete framework-specific analysis results

    Example:
        >>> result = UnifiedAnalysisResult(
        ...     document_type="S1000D Technical Manual",
        ...     confidence=0.98,
        ...     framework="xml-analysis-framework",
        ...     metadata={"version": "4.2", "schema": "s1000d"}
        ... )
        >>> result.document_type
        'S1000D Technical Manual'
        >>> result['confidence']
        0.98
        >>> result.get('framework')
        'xml-analysis-framework'
    """

    document_type: str
    confidence: float
    framework: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    content: Optional[str] = None
    ai_opportunities: List[str] = field(default_factory=list)
    raw_analysis: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary for serialization.

        Returns:
            Dictionary representation of the result

        Example:
            >>> result = UnifiedAnalysisResult(
            ...     document_type="Test", confidence=1.0, framework="test"
            ... )
            >>> result.to_dict()
            {'document_type': 'Test', 'confidence': 1.0, 'framework': 'test', ...}
        """
        return asdict(self)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Dict-style get method.

        Args:
            key: Attribute name
            default: Default value if key not found

        Returns:
            Attribute value or default

        Example:
            >>> result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")
            >>> result.get('document_type')
            'Test'
            >>> result.get('missing_key', 'default')
            'default'
        """
        return getattr(self, key, default)

    def __getitem__(self, key: str) -> Any:
        """
        Support dict-style access: result['key'].

        Args:
            key: Attribute name

        Returns:
            Attribute value

        Raises:
            KeyError: If key not found

        Example:
            >>> result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")
            >>> result['document_type']
            'Test'
        """
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(f"'{key}' not found in UnifiedAnalysisResult")

    def __contains__(self, key: str) -> bool:
        """
        Support 'in' operator.

        Args:
            key: Attribute name

        Returns:
            True if attribute exists

        Example:
            >>> result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")
            >>> 'document_type' in result
            True
            >>> 'missing_key' in result
            False
        """
        return hasattr(self, key)

    def keys(self):
        """
        Return field names like a dict.

        Returns:
            Iterator of field names

        Example:
            >>> result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")
            >>> list(result.keys())
            ['document_type', 'confidence', 'framework', 'metadata', 'content', ...]
        """
        return self.__dataclass_fields__.keys()

    def values(self):
        """
        Return field values like a dict.

        Returns:
            List of field values

        Example:
            >>> result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")
            >>> values = result.values()
            >>> 'Test' in values
            True
        """
        return [getattr(self, k) for k in self.keys()]

    def items(self):
        """
        Return (key, value) pairs like a dict.

        Returns:
            List of (field_name, value) tuples

        Example:
            >>> result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")
            >>> items = list(result.items())
            >>> ('document_type', 'Test') in items
            True
        """
        return [(k, getattr(self, k)) for k in self.keys()]


@dataclass
class ChunkInfo:
    """
    Standard structure for document chunks.

    Represents a single chunk from a document, suitable for embedding
    and vector database storage.

    Attributes:
        chunk_id: Unique identifier for this chunk
        content: Text content of the chunk
        metadata: Chunk-specific metadata (position, type, etc.)
        token_count: Estimated token count for LLM context
        chunk_type: Type of chunk (e.g., 'text', 'code', 'table', 'heading')

    Example:
        >>> chunk = ChunkInfo(
        ...     chunk_id="doc1_chunk_001",
        ...     content="This is the content of the first chunk.",
        ...     metadata={"page": 1, "section": "Introduction"},
        ...     token_count=42,
        ...     chunk_type="text"
        ... )
        >>> chunk.chunk_id
        'doc1_chunk_001'
        >>> chunk['content']
        'This is the content of the first chunk.'
    """

    chunk_id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    token_count: int = 0
    chunk_type: str = "text"

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary for serialization.

        Returns:
            Dictionary representation of the chunk

        Example:
            >>> chunk = ChunkInfo(chunk_id="test", content="test content")
            >>> chunk.to_dict()
            {'chunk_id': 'test', 'content': 'test content', ...}
        """
        return asdict(self)

    def __getitem__(self, key: str) -> Any:
        """
        Support dict-style access.

        Args:
            key: Attribute name

        Returns:
            Attribute value

        Raises:
            KeyError: If key not found

        Example:
            >>> chunk = ChunkInfo(chunk_id="test", content="test content")
            >>> chunk['chunk_id']
            'test'
        """
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(f"'{key}' not found in ChunkInfo")
