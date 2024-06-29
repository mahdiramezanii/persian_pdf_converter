#========================== imports lib  ==================================

from imports import *
from persian_pdf_converter import _my_random_string

#============================ End imports =============================


''' Get the parent directory of 
the current script file.'''
parent_path = Path(__file__).resolve().parent.parent


'''

Define a function to convert a PDF
file to a Word document.

'''
def pdf_to_word(pdf_path: str, output_dir: str, lang="fas+eng", **kwargs):

    #==================================
    '''Replace backslashes with forward
     slashes in the output directory path
     to ensure compatibility across different
     operating systems.'''
    output_dir = output_dir.replace("\\", "/")
    # ==================================

    #====================================================================
    '''Generate a random name for the output
     Word document using the custom
    '_my_random_string' function.'''
    pdf_name = f"word-{_my_random_string(6)}"
    # ====================================================================



    #=====================================================================
    '''Convert PDF pages into images.
    'poppler_path' specifies the path to 
    the Poppler utility,
    required for PDF to image conversion.'''
    pages = convert_from_path(pdf_path,
                              poppler_path=f"{parent_path}/src/my_pkg/resources/poppler-24.02/bin")
    # =====================================================================


    #==========================================================
    # Set the path to the Tesseract OCR executable.
    pytesseract.pytesseract.tesseract_cmd = \
        f"{parent_path}/src/my_pkg/resources/Tesseract-OCR/tesseract.exe"
    #=====================================================================

    #========================================================================
    # Initialize an empty list to store the
    # extracted text from each page.
    texts = []
    #=========================================================================

    #================================================================
    # Loop through each page image and perform OCR to extract text.
    for i, page in tqdm(enumerate(pages), position=0):
    #===============================================================

        #==============================================================
        # Create a temporary directory to store the page image.
        with tempfile.TemporaryDirectory() as img_dir:
            # Define the file name for the image.
            img_name = f'{pdf_name}-{i+1}.jpg'
            # Define the full path for the image file.
            img_path = Path(img_dir) / img_name
        #==============================================================

            #===================================================================
            # Save the page as a JPEG image.
            page.save(img_path, 'JPEG')


            '''
             Perform OCR on the saved image
             to extract text.
            'lang' specifies the languages
             to use for OCR 
            (e.g., Persian and English).
            '''

            text = pytesseract.image_to_string(Image.open(img_path), lang=lang)
            # Append the extracted text to the list.
            texts.append(text)
            #===================================================================


    # Create a new Word document.
    document = Document()

    #==================================================================
    '''
    Set the default font and alignment for normal 
    text in the document.
    '''
    style_normal = document.styles['Normal']
    font = style_normal.font
    font.name = 'Arial'
    #==================================================================

    #===================================================================
    '''Enable right-to-left text direction,
    which is important for Persian text.'''
    font.rtl = True
    #=====================================================================



    #=====================================================================
    '''Set the font and alignment for heading
    1 style text in the document.'''
    style_h1 = document.styles['Heading 1']
    font = style_h1.font
    font.name = 'Arial'
    #=======================================================================



    # Enable right-to-left text direction for headings as well.
    font.rtl = True

    #=====================================================================
    '''Loop through each extracted text
    block and add it to the document.'''
    for i, text in tqdm(enumerate(texts), position=0):
        # Add a heading to indicate the page number.
        heading = document.add_heading(f'صفحه: {i+1}', level=1)
        # Align the heading to the right.
        heading.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        # Apply the heading style to the heading.
        heading.style = document.styles['Heading 1']

        # Add the extracted text as a paragraph in the document.
        paragraph = document.add_paragraph(text)
        # Align the paragraph to the right.
        paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        # Apply the normal style to the paragraph.
        paragraph.style = document.styles['Normal']
    #=========================================================================


    #=========================================================================
    # Define the output path for the Word document.
    output_path = Path(output_dir) / f'{pdf_name}.docx'
    # Save the Word document to the specified output path.
    document.save(output_path)
    #=========================================================================

    # Return the filename of the generated Word document.
    return f'{pdf_name}.docx'