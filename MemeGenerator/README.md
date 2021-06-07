# MemeGenerator

MemeGenerator is a project for the Intermediate Python Course in Udacity.  

It is a multimedia app that generates memes (an image overlaid with a quote) - either from stock data or via user input.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies listed in the requirements.txt in the virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
```
### Install pdftotext
To read the text from PDF files, you need to install [pdftotext](https://www.xpdfreader.com/download.html).

For MacOS:

- Install Brew (A Package Manager for MacOS):

```$/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
- run ```brew install pkg-config poppler python```
- run ```pip install pdftotext```


## Interface

To get started, you have two options:
1) Run ```python3 meme.py```:
- If no input, the program generates a random image and quote and saves it in the ```./tmp``` folder.

- To create a bespoke Meme, you have the option to add the following to the command line interface (CLI) of ```python3 meme.py```:
--path (local)
--body
--author

2) Run ```python3 app.py``` to start the flask web server
at local host ```http://127.0.0.1:5000/ ```
- Pressing the Random button will continue creating new Memes.
- Or press the Creator button and enter your own image, text and author details.
- All Memes are stored in the ```./static``` folder.

## More details on the Sub-Modules
### QuoteEngine
Contains modules to encapsulate quotes and ingest data from different file types as quote objects.
### QuoteModel.py
Defines QuoteModel class with two attributes: body and author.
### IngestorInterface.py
An Abstract Base Class (ABC) serving as the parent for the following 4 Ingestors below.

### CSVIngestor.py
Child of the ABC IngestorInterface.py used as a strategy object to parce .csv files. Requires import of Pandas and list from typing, returns a list of QuoteModel objects.

### DocxIngestor.py
Child of the ABC IngestorInterface.py used as a strategy object to parce .docx files. Requires import of Document from docx and list from typing, returns a list of QuoteModel objects.

### TxtIngestor.py
Child of the ABC IngestorInterface.py used as a strategy object to parce .txt files. Requires import of Pandas and list from typing, returns a list of QuoteModel objects.

### PDFIngestor.py
Child of the ABC IngestorInterface.py used as a strategy object to parce .pdf files. Requires import subprocess, os, random and list from typing, as well as pdftotext (see above under installation). Returns a list of QuoteModel objects.

###Ingestor.py
Child of the ABC IngestorInterface.py, contains Ingestor class to determine which ingestor to use for specific file. Returns a list of QuoteModel objects.


### MemeEngine
Contains a module defining the MemeEngine class.

### MemeEngine.py
Class to modify image by resizing and adding text either input by the user via the app or the CLI or randomly chosen from existing data. Contains three methods: resize, write_text, make_meme.
Needs import of Image, ImageDraw, and ImageFont from the Pillow library, and random.

### Exceptions.py
Module of exception classes including File/Format/Text Exceptions.




## License
This README file is created with an MIT License (https://choosealicense.com/licenses/mit/)
