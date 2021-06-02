from ingestor import Ingestor

q_file = ['./_data/DogQuotes/DogQuotesTXT.txt',
               './_data/DogQuotes/DogQuotesDOCX.docx',
               './_data/DogQuotes/DogQuotesPDF.pdf',
               './_data/DogQuotes/DogQuotesCSV.csv']

for f in q_file:
    try:
        print(Ingestor.parse(f))
    except ValueError as error:
        print(f"ValueError: {error}")
