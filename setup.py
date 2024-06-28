import os

from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import shutil
import requests

# تعریف کلاس InstallCommand برای اجرای اسکریپت نصب
class InstallCommand(install):

    def run(self):
        install.run(self)

        static_files_urls = [
            'https://example.com/static_file1.zip',
            'https://example.com/static_file2.tar.gz',

        ]

        # مسیر مقصد برای ذخیره فایل‌های دانلود شده
        destination_dir = os.path.join(os.path.dirname(__file__), 'persian_pdf_converter', 'static')

        # ایجاد پوشه مقصد در صورت عدم وجود آن
        os.makedirs(destination_dir, exist_ok=True)

        # دانلود هر فایل از URL‌های مشخص شده
        for url in static_files_urls:
            filename = os.path.basename(url)
            filepath = os.path.join(destination_dir, filename)

            # دانلود فایل
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    shutil.copyfileobj(response.raw, f)
            else:
                print(f"Failed to download {url}")

setup(
    name="persian_pdf_converter",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'persian_pdf_converter': ['statics/*'],
    },
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
    cmdclass={
        'install': InstallCommand,  # اضافه کردن دستور InstallCommand به setup.py
    },
    python_requires='>=3.6',
)
