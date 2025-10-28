"""
Tests for constants (ChunkStrategy enum).
"""

from analysis_framework_base import ChunkStrategy


class TestChunkStrategy:
    """Test ChunkStrategy enum."""

    def test_enum_values(self):
        """Test that all expected enum values exist."""
        assert ChunkStrategy.AUTO.value == "auto"
        assert ChunkStrategy.HIERARCHICAL.value == "hierarchical"
        assert ChunkStrategy.SLIDING_WINDOW.value == "sliding_window"
        assert ChunkStrategy.CONTENT_AWARE.value == "content_aware"
        assert ChunkStrategy.STRUCTURAL.value == "structural"
        assert ChunkStrategy.TABLE_AWARE.value == "table_aware"
        assert ChunkStrategy.PAGE_AWARE.value == "page_aware"

    def test_enum_membership(self):
        """Test enum membership."""
        strategies = list(ChunkStrategy)
        assert ChunkStrategy.AUTO in strategies
        assert ChunkStrategy.HIERARCHICAL in strategies
        assert ChunkStrategy.SLIDING_WINDOW in strategies
        assert ChunkStrategy.CONTENT_AWARE in strategies
        assert ChunkStrategy.STRUCTURAL in strategies
        assert ChunkStrategy.TABLE_AWARE in strategies
        assert ChunkStrategy.PAGE_AWARE in strategies

    def test_enum_count(self):
        """Test that we have the expected number of strategies."""
        assert len(list(ChunkStrategy)) == 7

    def test_string_comparison(self):
        """Enum values can be compared to strings."""
        assert ChunkStrategy.AUTO == "auto"
        assert ChunkStrategy.HIERARCHICAL == "hierarchical"
        assert ChunkStrategy.SLIDING_WINDOW == "sliding_window"

    def test_enum_access_by_name(self):
        """Access enum by name."""
        assert ChunkStrategy["AUTO"] == ChunkStrategy.AUTO
        assert ChunkStrategy["HIERARCHICAL"] == ChunkStrategy.HIERARCHICAL
        assert ChunkStrategy["SLIDING_WINDOW"] == ChunkStrategy.SLIDING_WINDOW

    def test_enum_iteration(self):
        """Iterate over all enum values."""
        values = [strategy.value for strategy in ChunkStrategy]
        assert "auto" in values
        assert "hierarchical" in values
        assert "sliding_window" in values
        assert "content_aware" in values
        assert "structural" in values
        assert "table_aware" in values
        assert "page_aware" in values

    def test_enum_in_function(self):
        """Use enum in function parameter."""

        def process_with_strategy(strategy: ChunkStrategy) -> str:
            return f"Using {strategy.value} strategy"

        result = process_with_strategy(ChunkStrategy.HIERARCHICAL)
        assert result == "Using hierarchical strategy"

        result = process_with_strategy(ChunkStrategy.AUTO)
        assert result == "Using auto strategy"

    def test_enum_string_conversion(self):
        """Convert enum to string."""
        assert str(ChunkStrategy.AUTO.value) == "auto"
        assert str(ChunkStrategy.HIERARCHICAL.value) == "hierarchical"
