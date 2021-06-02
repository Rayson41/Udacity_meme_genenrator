import os


from ingestor.docx_ingestor import DocxIngestor
from ingestor.csv_ingestor import CSVIngestor
from ingestor.text_ingestor import TextIngestor
from ingestor.pdf_ingestor import PDFIngestor
from ingestor.ingestor_interface import IngestorInterface, extensions


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        f_name, f_ext = os.path.splitext(path)
        if not cls.verify(f_ext):
            raise ValueError("Unsupported file extension:", f_ext)
        if f_ext == extensions.get("TEXT"):
            return TextIngestor.parse(path)
        if f_ext == extensions.get("DOCX"):
            return DocxIngestor.parse(path)
        if f_ext == extensions.get("PDF"):
            return PDFIngestor.parse(path)
        if f_ext == extensions.get("CSV"):
            return CSVIngestor.parse(path)
