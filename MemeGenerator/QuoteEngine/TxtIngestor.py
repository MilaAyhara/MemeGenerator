"""An ingestor for reading txt files."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """The class that ingests info from txt."""
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        try:
            quotes = []
            df = pandas.read_csv(path, sep='-', header=None)

            for index, row in df.iterrows():
                new_quote = QuoteModel(row[0], row[1])
                quotes.append(new_quote)
        except Exception as e:
            raise Exception("Txt Parsing Issue.")

        return quotes
