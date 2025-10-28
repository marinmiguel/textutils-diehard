import textutils.core as c

def test_full_text_processing_with_unique_words():
    text = "Red red BLUE! Hello, world... Hello WORLD"
    
    # Normalize whitespace (assuming this function exists)
    normalized = c.normalize_whitespace(text)
    
    # Count unique words
    counts = c.unique_words(normalized)
    
    # Get top N words (assuming this function exists)
    result = c.top_n(counts, 3)
    
    # Verify the complete pipeline works
    assert result == [("hello", 2), ("world", 2), ("red", 2)]