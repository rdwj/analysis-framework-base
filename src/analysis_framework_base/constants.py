"""
Shared constants for analysis frameworks.

This module defines standard constants used across frameworks,
particularly for chunking strategies.
"""

from enum import Enum


class ChunkStrategy(str, Enum):
    """
    Standard chunking strategy names.

    These strategies represent common approaches to splitting documents
    into chunks for LLM/RAG applications. Not all frameworks will support
    all strategies.

    Attributes:
        AUTO: Framework automatically selects best strategy
        HIERARCHICAL: Chunk based on document structure (sections, headings)
        SLIDING_WINDOW: Fixed-size overlapping chunks
        CONTENT_AWARE: Smart chunking based on semantic boundaries
        STRUCTURAL: Chunk by structural elements (paragraphs, tables)
        TABLE_AWARE: Special handling for tables and tabular data
        PAGE_AWARE: Chunk by page boundaries (for paginated documents)

    Example:
        >>> strategy = ChunkStrategy.HIERARCHICAL
        >>> strategy.value
        'hierarchical'
        >>> ChunkStrategy.AUTO
        <ChunkStrategy.AUTO: 'auto'>
        >>> list(ChunkStrategy)
        [<ChunkStrategy.AUTO: 'auto'>, <ChunkStrategy.HIERARCHICAL: 'hierarchical'>, ...]
    """

    AUTO = "auto"
    HIERARCHICAL = "hierarchical"
    SLIDING_WINDOW = "sliding_window"
    CONTENT_AWARE = "content_aware"
    STRUCTURAL = "structural"
    TABLE_AWARE = "table_aware"
    PAGE_AWARE = "page_aware"
