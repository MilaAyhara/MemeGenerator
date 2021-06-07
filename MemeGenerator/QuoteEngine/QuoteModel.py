"""Allows for Quote Input."""


class QuoteModel():
    """Allows for user input of Body and Author."""

    def __init__(self, body, author):
        """Initialize body and author. """
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent how a quote should look like. """
        return f'"{self.body}" - {self.author}'
