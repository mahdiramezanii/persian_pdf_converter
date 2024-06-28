# Dockerfile

FROM python:3.8-slim

# نصب ابزارهای لازم
RUN apt-get update && \
    apt-get install -y libsm6 libxext6 libxrender-dev tesseract-ocr poppler-utils tesseract-ocr-fas && \
    apt-get clean


WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-m", "persian_pdf_converter.pdf_converter"]
