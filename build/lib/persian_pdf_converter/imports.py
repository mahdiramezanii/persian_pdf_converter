
#================================  import tqdm  =====================================
'''Importing necessary libraries
'tqdm' is used for creating progress bars,
which are useful to track the progress of
loops.'''
from tqdm import tqdm
#================================================================================

#=================================  import pdf2image ===========================
''''convert_from_path' from 'pdf2image'
 library is used to convert PDF
pages into images.'''
from pdf2image import convert_from_path
#=================================  End import pdf2image ===========================


#=================================   import pytesseract =============================
''''pytesseract' is a wrapper for Google's
 Tesseract-OCR Engine,
used for performing optical character
 recognition (OCR) on images.'''
import pytesseract
#================================= End  import pytesseract =============================

#================================= import PIL ===============================
''''Image' from 'PIL' (Python Imaging Library) 
is used for opening,
manipulating, and saving many different
 image file formats.'''
from PIL import Image
#================================= End  import PIL ===============================


#===============================  import Document ==========================
# 'Document' from 'docx' library is used to create new Word documents.
from docx import Document
#=============================== End import Document ==========================


#================================  import WD_ALIGN_PARAGRAPH  =====================
''''WD_ALIGN_PARAGRAPH' from 'docx.enum.text'
is used to align text in the Word document.'''
from docx.enum.text import WD_ALIGN_PARAGRAPH
#================================ End import WD_ALIGN_PARAGRAPH  =====================


#================================ import tempfile ==================================
# 'tempfile' is used to create temporary files and directories.
import tempfile
#================================ End import tempfile ==================================

#================================ import persian_pdf_converter  ==========================
''' '_my_random_string' is a custom function
 from 'persian_pdf_converter'
used to generate random strings,
 presumably for file naming.'''

from persian_pdf_converter import _my_random_string
#================================ End persian_pdf_converte =================================

#================================= import Path   ========================
'''Path' from 'pathlib' is used for object-oriented
 filesystem paths '''
from pathlib import Path
#================================= End import Path  ========================