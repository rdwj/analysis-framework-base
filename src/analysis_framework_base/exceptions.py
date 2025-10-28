"""
Exception hierarchy for analysis frameworks.

This module defines a standard set of exceptions that all frameworks
should use for consistency in error handling.
"""


class FrameworkError(Exception):
    """
    Base exception for all analysis framework errors.

    All framework-specific exceptions should inherit from this class
    to allow catching all framework errors with a single except clause.

    Example:
        >>> try:
        ...     raise FrameworkError("Something went wrong")
        ... except FrameworkError as e:
        ...     print(f"Framework error: {e}")
        Framework error: Something went wrong
    """

    pass


class UnsupportedFormatError(FrameworkError):
    """
    Raised when file format is not supported by the framework.

    This exception should be raised when a framework is asked to analyze
    a file type it doesn't support.

    Example:
        >>> def analyze(file_path: str):
        ...     if not file_path.endswith('.xml'):
        ...         raise UnsupportedFormatError(
        ...             f"Cannot analyze {file_path}: only XML files supported"
        ...         )
        >>> analyze('document.pdf')
        Traceback (most recent call last):
        ...
        UnsupportedFormatError: Cannot analyze document.pdf: ...
    """

    pass


class AnalysisError(FrameworkError):
    """
    Raised when document analysis fails.

    This exception should be raised when analysis encounters an error
    during processing, such as malformed documents, I/O errors, or
    parsing failures.

    Example:
        >>> def analyze_document(content: str):
        ...     if not content:
        ...         raise AnalysisError("Document is empty")
        >>> analyze_document("")
        Traceback (most recent call last):
        ...
        AnalysisError: Document is empty
    """

    pass


class ChunkingError(FrameworkError):
    """
    Raised when document chunking fails.

    This exception should be raised when chunking encounters an error,
    such as invalid strategy selection or processing failures.

    Example:
        >>> def chunk_document(strategy: str):
        ...     if strategy not in ['auto', 'hierarchical']:
        ...         raise ChunkingError(f"Unknown chunking strategy: {strategy}")
        >>> chunk_document('invalid')
        Traceback (most recent call last):
        ...
        ChunkingError: Unknown chunking strategy: invalid
    """

    pass
