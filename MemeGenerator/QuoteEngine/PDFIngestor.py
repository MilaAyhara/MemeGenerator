"""An ingestor for reading pdf files."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """The class that ingests info from pdf."""
    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse form a pdf file."""

        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
        try:
            tmp = f'./tmp/{random.randint(0,100000000)}.txt'
            call = subprocess.call(['pdftotext', '-simple', path, tmp])

            file_ref = open(tmp, "r")
            quotes = []

            for line in file_ref.readlines():
                line = line.replace('\"', '').strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    if len(parsed) > 1:
                        new_quote = QuoteModel(parsed[0].strip(),
                                               parsed[1].strip())
                        quotes.append(new_quote)

            file_ref.close()
            os.remove(tmp)

        except Exception as e:
            raise Exception("PDF Parsing Issue.")

        return quotes
