"""
Tests for exception hierarchy.
"""

import pytest
from analysis_framework_base import (
    FrameworkError,
    UnsupportedFormatError,
    AnalysisError,
    ChunkingError,
)


class TestExceptionHierarchy:
    """Test exception inheritance and behavior."""

    def test_framework_error_base(self):
        """FrameworkError is the base exception."""
        error = FrameworkError("Test error")
        assert isinstance(error, Exception)
        assert str(error) == "Test error"

    def test_unsupported_format_error(self):
        """UnsupportedFormatError inherits from FrameworkError."""
        error = UnsupportedFormatError("Format not supported")
        assert isinstance(error, FrameworkError)
        assert isinstance(error, Exception)
        assert str(error) == "Format not supported"

    def test_analysis_error(self):
        """AnalysisError inherits from FrameworkError."""
        error = AnalysisError("Analysis failed")
        assert isinstance(error, FrameworkError)
        assert isinstance(error, Exception)
        assert str(error) == "Analysis failed"

    def test_chunking_error(self):
        """ChunkingError inherits from FrameworkError."""
        error = ChunkingError("Chunking failed")
        assert isinstance(error, FrameworkError)
        assert isinstance(error, Exception)
        assert str(error) == "Chunking failed"

    def test_catch_specific_exception(self):
        """Can catch specific exception types."""
        with pytest.raises(UnsupportedFormatError):
            raise UnsupportedFormatError("Unsupported")

        with pytest.raises(AnalysisError):
            raise AnalysisError("Failed")

        with pytest.raises(ChunkingError):
            raise ChunkingError("Error")

    def test_catch_base_exception(self):
        """Can catch all framework errors with FrameworkError."""
        # UnsupportedFormatError
        with pytest.raises(FrameworkError):
            raise UnsupportedFormatError("Format error")

        # AnalysisError
        with pytest.raises(FrameworkError):
            raise AnalysisError("Analysis error")

        # ChunkingError
        with pytest.raises(FrameworkError):
            raise ChunkingError("Chunking error")

    def test_exception_messages(self):
        """Exceptions preserve custom messages."""
        try:
            raise UnsupportedFormatError("Cannot process .xyz files")
        except UnsupportedFormatError as e:
            assert "Cannot process .xyz files" in str(e)

        try:
            raise AnalysisError("Document is malformed")
        except AnalysisError as e:
            assert "Document is malformed" in str(e)

        try:
            raise ChunkingError("Invalid strategy: unknown")
        except ChunkingError as e:
            assert "Invalid strategy: unknown" in str(e)

    def test_exception_in_error_handling(self):
        """Exceptions work in typical error handling scenarios."""

        def analyze_file(path: str):
            if not path.endswith(".xml"):
                raise UnsupportedFormatError(f"Only XML files supported, got {path}")
            if path == "broken.xml":
                raise AnalysisError("File is corrupted")
            return "success"

        def chunk_file(strategy: str):
            if strategy not in ["auto", "hierarchical"]:
                raise ChunkingError(f"Unknown strategy: {strategy}")
            return []

        # Test UnsupportedFormatError
        with pytest.raises(UnsupportedFormatError) as exc_info:
            analyze_file("document.pdf")
        assert "Only XML files supported" in str(exc_info.value)

        # Test AnalysisError
        with pytest.raises(AnalysisError) as exc_info:
            analyze_file("broken.xml")
        assert "File is corrupted" in str(exc_info.value)

        # Test ChunkingError
        with pytest.raises(ChunkingError) as exc_info:
            chunk_file("invalid")
        assert "Unknown strategy: invalid" in str(exc_info.value)

        # Test success path
        assert analyze_file("valid.xml") == "success"
        assert chunk_file("auto") == []
