"""We determine which ingestor to use."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TxtIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """The class choosing which ingestor to use."""

    ingestors = [DocxIngestor, CSVIngestor, TxtIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse the path for the correct ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise Exception('Filetype is not supported')
