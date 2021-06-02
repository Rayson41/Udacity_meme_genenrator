import os
import subprocess

from ingestor.ingestor_interface import IngestorInterface
from ingestor.text_ingestor import TextIngestor


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        text = './pdf_to_text.txt'
        cmd = f"./pdftotext -layout -nopgbrk {path} {text}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        q = TextIngestor.parse(text)
        os.remove(text)
        return q
