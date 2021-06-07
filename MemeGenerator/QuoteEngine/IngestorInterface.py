""" Base of the Ingestor."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Class to identify an ingestible file and parse it."""
    allowed_extension = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file is ingestible."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file info."""
        pass
