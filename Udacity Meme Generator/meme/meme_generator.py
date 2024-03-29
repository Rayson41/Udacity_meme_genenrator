import os
import random

from ingestor import Ingestor
from models import QuoteModel
from meme.meme_engine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    if path is None:
        img_d = "./_data/Photos/Dog/"
        img = []
        for root, dirs, files in os.walk(img_d):
            img = [os.path.join(root, name) for name in files]

        img_path = random.choice(img)
    else:
        img_path = path

    if body is None:
        q_file = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        q = []
        for f in q_file:
            q.extend(Ingestor.parse(f))

        quote = random.choice(q)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img_path, quote.body, quote.author)
    return path
