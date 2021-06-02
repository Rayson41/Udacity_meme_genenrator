# Ingestors Module

This module reads quotes from various files and returns a list of processed
quotes.

## Dependencies
Pandas module is required to read CSV
files.

python docx module is required to read DOCX files.
pdftotext is a command line application used to extract text from PDF files.

--Usage
Import the main `Ingestor` class and use its class method `parse`.

# Models

--IngestorInterface
This class is an interface that is used as a base class for all other
ingestors. It has a complete class method `verify` that checks if a file
extension is supported or not. It has an abstract class method `parse` that
is used by the derived classes to parse files.


--DocxIngestor
As the name suggests, this ingestor overrides the `parse` method to read
DOCX files, extract lines and return a list of quotes. It uses the
`python-docx` library to read DOCX files.

--CSVIngestor
As the name suggests, this ingestor overrides the `parse` method to read
CSV files, extract lines and return a list of quotes. It uses the `pandas`
library to read CSVs.

--TextIngestor
This ingestor overrides the `parse` method to read TXT files, 
extract lines and return a list of quotes. It uses the in-built
file reading methods to read text files.

--Ingestor
This is the main class that calls all the other ingestor classes. Its `parse`
method just takes the file path as an argument and it extracts the extension of
the file and returns results from the required ingestor.

--PDFIngestor
This ingestor overrides the `parse` method to read
PDF files and extract its lines into a text file. That text file is then
parsed using the `TextIngestor` It uses the `subprocess` library to call the
`pdftotext` command line tool to extract text from PDF into a `.txt` file.
