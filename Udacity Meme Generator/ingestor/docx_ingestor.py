from docx import Document

from models import QuoteModel
from ingestors.ingestor_interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        doc = Document(path)
        q = []
        for i in doc.paragraphs:
            i.text and q.append(
                QuoteModel(*i.text.split(" - ")))
        return q
