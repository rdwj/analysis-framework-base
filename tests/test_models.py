"""
Tests for data models (UnifiedAnalysisResult and ChunkInfo).
"""

import pytest
from analysis_framework_base import UnifiedAnalysisResult, ChunkInfo


class TestUnifiedAnalysisResult:
    """Test UnifiedAnalysisResult data model."""

    def test_basic_creation(self):
        """Create a basic UnifiedAnalysisResult."""
        result = UnifiedAnalysisResult(
            document_type="Test Document",
            confidence=0.95,
            framework="test-framework",
        )

        assert result.document_type == "Test Document"
        assert result.confidence == 0.95
        assert result.framework == "test-framework"
        assert result.metadata == {}
        assert result.content is None
        assert result.ai_opportunities == []
        assert result.raw_analysis == {}

    def test_full_creation(self):
        """Create a UnifiedAnalysisResult with all fields."""
        result = UnifiedAnalysisResult(
            document_type="S1000D Technical Manual",
            confidence=0.98,
            framework="xml-analysis-framework",
            metadata={"version": "4.2", "schema": "s1000d"},
            content="Document content here",
            ai_opportunities=["Summarization", "QA"],
            raw_analysis={"element_count": 1000},
        )

        assert result.document_type == "S1000D Technical Manual"
        assert result.confidence == 0.98
        assert result.framework == "xml-analysis-framework"
        assert result.metadata["version"] == "4.2"
        assert result.content == "Document content here"
        assert len(result.ai_opportunities) == 2
        assert result.raw_analysis["element_count"] == 1000

    def test_attribute_access(self):
        """Access fields via attributes."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

        assert result.document_type == "Test"
        assert result.confidence == 1.0
        assert result.framework == "test"

    def test_dict_style_access(self):
        """Access fields like a dictionary."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

        assert result["document_type"] == "Test"
        assert result["confidence"] == 1.0
        assert result["framework"] == "test"

    def test_dict_style_access_invalid_key(self):
        """Dict-style access with invalid key raises KeyError."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

        with pytest.raises(KeyError):
            _ = result["nonexistent_key"]

    def test_get_method(self):
        """Use get() method like a dict."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

        assert result.get("document_type") == "Test"
        assert result.get("nonexistent", "default") == "default"
        assert result.get("missing") is None

    def test_contains_operator(self):
        """Use 'in' operator to check field existence."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

        assert "document_type" in result
        assert "confidence" in result
        assert "nonexistent" not in result

    def test_keys_method(self):
        """Get field names via keys()."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

        keys = list(result.keys())
        assert "document_type" in keys
        assert "confidence" in keys
        assert "framework" in keys
        assert "metadata" in keys

    def test_values_method(self):
        """Get field values via values()."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

        values = result.values()
        assert "Test" in values
        assert 1.0 in values
        assert "test" in values

    def test_items_method(self):
        """Get (key, value) pairs via items()."""
        result = UnifiedAnalysisResult(document_type="Test", confidence=0.9, framework="test")

        items = list(result.items())
        assert ("document_type", "Test") in items
        assert ("confidence", 0.9) in items
        assert ("framework", "test") in items

    def test_to_dict_method(self):
        """Convert to dict via to_dict()."""
        result = UnifiedAnalysisResult(
            document_type="Test",
            confidence=0.95,
            framework="test",
            metadata={"key": "value"},
        )

        result_dict = result.to_dict()
        assert isinstance(result_dict, dict)
        assert result_dict["document_type"] == "Test"
        assert result_dict["confidence"] == 0.95
        assert result_dict["framework"] == "test"
        assert result_dict["metadata"]["key"] == "value"


class TestChunkInfo:
    """Test ChunkInfo data model."""

    def test_basic_creation(self):
        """Create a basic ChunkInfo."""
        chunk = ChunkInfo(chunk_id="chunk_001", content="Test content")

        assert chunk.chunk_id == "chunk_001"
        assert chunk.content == "Test content"
        assert chunk.metadata == {}
        assert chunk.token_count == 0
        assert chunk.chunk_type == "text"

    def test_full_creation(self):
        """Create a ChunkInfo with all fields."""
        chunk = ChunkInfo(
            chunk_id="doc1_chunk_042",
            content="This is a paragraph of text.",
            metadata={"page": 5, "section": "Introduction"},
            token_count=42,
            chunk_type="paragraph",
        )

        assert chunk.chunk_id == "doc1_chunk_042"
        assert chunk.content == "This is a paragraph of text."
        assert chunk.metadata["page"] == 5
        assert chunk.metadata["section"] == "Introduction"
        assert chunk.token_count == 42
        assert chunk.chunk_type == "paragraph"

    def test_dict_style_access(self):
        """Access fields like a dictionary."""
        chunk = ChunkInfo(chunk_id="test_001", content="Test")

        assert chunk["chunk_id"] == "test_001"
        assert chunk["content"] == "Test"

    def test_dict_style_access_invalid_key(self):
        """Dict-style access with invalid key raises KeyError."""
        chunk = ChunkInfo(chunk_id="test_001", content="Test")

        with pytest.raises(KeyError):
            _ = chunk["nonexistent_key"]

    def test_to_dict_method(self):
        """Convert to dict via to_dict()."""
        chunk = ChunkInfo(
            chunk_id="test_001",
            content="Test content",
            metadata={"source": "test.txt"},
            token_count=10,
            chunk_type="paragraph",
        )

        chunk_dict = chunk.to_dict()
        assert isinstance(chunk_dict, dict)
        assert chunk_dict["chunk_id"] == "test_001"
        assert chunk_dict["content"] == "Test content"
        assert chunk_dict["metadata"]["source"] == "test.txt"
        assert chunk_dict["token_count"] == 10
        assert chunk_dict["chunk_type"] == "paragraph"

    def test_different_chunk_types(self):
        """Create chunks with different types."""
        text_chunk = ChunkInfo(chunk_id="c1", content="text", chunk_type="text")
        code_chunk = ChunkInfo(chunk_id="c2", content="code", chunk_type="code")
        table_chunk = ChunkInfo(chunk_id="c3", content="table", chunk_type="table")

        assert text_chunk.chunk_type == "text"
        assert code_chunk.chunk_type == "code"
        assert table_chunk.chunk_type == "table"
