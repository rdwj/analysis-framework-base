"""
Tests for abstract base classes (interfaces).
"""

import pytest
from analysis_framework_base import BaseAnalyzer, BaseChunker, UnifiedAnalysisResult, ChunkInfo


class TestBaseAnalyzer:
    """Test BaseAnalyzer abstract interface."""

    def test_cannot_instantiate_base_analyzer(self):
        """BaseAnalyzer cannot be instantiated directly."""
        with pytest.raises(TypeError):
            BaseAnalyzer()

    def test_concrete_analyzer_implementation(self):
        """Concrete implementation of BaseAnalyzer works correctly."""

        class ConcreteAnalyzer(BaseAnalyzer):
            def analyze_unified(self, file_path: str, **kwargs) -> UnifiedAnalysisResult:
                return UnifiedAnalysisResult(
                    document_type="Test Document",
                    confidence=0.95,
                    framework="test-framework",
                )

            def get_supported_formats(self):
                return [".txt", ".md"]

        analyzer = ConcreteAnalyzer()
        assert isinstance(analyzer, BaseAnalyzer)

        # Test analyze_unified
        result = analyzer.analyze_unified("test.txt")
        assert isinstance(result, UnifiedAnalysisResult)
        assert result.document_type == "Test Document"
        assert result.confidence == 0.95
        assert result.framework == "test-framework"

        # Test get_supported_formats
        formats = analyzer.get_supported_formats()
        assert formats == [".txt", ".md"]

    def test_incomplete_implementation_fails(self):
        """Incomplete implementation cannot be instantiated."""

        class IncompleteAnalyzer(BaseAnalyzer):
            def analyze_unified(self, file_path: str, **kwargs) -> UnifiedAnalysisResult:
                return UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")

            # Missing get_supported_formats

        with pytest.raises(TypeError):
            IncompleteAnalyzer()


class TestBaseChunker:
    """Test BaseChunker abstract interface."""

    def test_cannot_instantiate_base_chunker(self):
        """BaseChunker cannot be instantiated directly."""
        with pytest.raises(TypeError):
            BaseChunker()

    def test_concrete_chunker_implementation(self):
        """Concrete implementation of BaseChunker works correctly."""

        class ConcreteChunker(BaseChunker):
            def chunk_document(
                self,
                file_path: str,
                analysis: UnifiedAnalysisResult,
                strategy: str = "auto",
                **kwargs,
            ):
                return [
                    ChunkInfo(
                        chunk_id="chunk_001",
                        content="Test content",
                        token_count=10,
                    )
                ]

            def get_supported_strategies(self):
                return ["auto", "hierarchical"]

        chunker = ConcreteChunker()
        assert isinstance(chunker, BaseChunker)

        # Test chunk_document
        analysis = UnifiedAnalysisResult(document_type="Test", confidence=1.0, framework="test")
        chunks = chunker.chunk_document("test.txt", analysis)
        assert len(chunks) == 1
        assert chunks[0].chunk_id == "chunk_001"
        assert chunks[0].content == "Test content"

        # Test get_supported_strategies
        strategies = chunker.get_supported_strategies()
        assert strategies == ["auto", "hierarchical"]

    def test_incomplete_chunker_implementation_fails(self):
        """Incomplete chunker implementation cannot be instantiated."""

        class IncompleteChunker(BaseChunker):
            def chunk_document(
                self,
                file_path: str,
                analysis: UnifiedAnalysisResult,
                strategy: str = "auto",
                **kwargs,
            ):
                return []

            # Missing get_supported_strategies

        with pytest.raises(TypeError):
            IncompleteChunker()
