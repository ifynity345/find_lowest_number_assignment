# Refactored code following the Single Responsibility Principle (SRP)

class TextAnalyzer:
    """Class responsible ONLY for analyzing text."""
    def __init__(self, text):
        self.text = text

    def word_count(self):
        words = self.text.split()
        return len(words)


class TextFileSaver:
    """Class responsible ONLY for saving text to a file."""
    @staticmethod
    def save(text, filename):
        with open(filename, "w") as f:
            f.write(text)


# Demo usage
if __name__ == "__main__":
    text = "An example that violates a SOLID principle."
    analyzer = TextAnalyzer(text)

    count = analyzer.word_count()
    print(f"Word count: {count}")

    TextFileSaver.save(text, "example.txt")
    print("Text saved to example.txt")
