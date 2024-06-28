# setup.py

from setuptools import setup, find_packages

setup(
    name="persian_pdf_converter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "pdf2image",
        "pytesseract",
        "Pillow",
        "python-docx"
    ],
    author="mahdiramezani",
    author_email="mahdiramezanii.official@gmail.com",
    description="convert persian pdf to .docx",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mahdiramezanii/persian_pdf_converter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
