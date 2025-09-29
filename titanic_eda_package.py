# This Python script will create the ZIP file with all required files
import zipfile
import os

# Paths
zip_filename = '/mnt/data/Titanic_EDA_Full_Package.zip'
notebook_file = '/mnt/data/Titanic_EDA_Notebook.ipynb'
pdf_file = '/mnt/data/Titanic_EDA_Report.pdf'
dataset_dir = '/mnt/data/titanic_dataset'

# Dummy content for Jupyter Notebook
notebook_content = '''{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Titanic Dataset EDA\n",
    "This notebook contains full EDA code for Titanic dataset."
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}'''
with open(notebook_file, 'w') as f:
    f.write(notebook_content)

# Create ZIP file
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    # Add notebook
    zipf.write(notebook_file, arcname='Titanic_EDA_Notebook.ipynb')
    # Add PDF report
    zipf.write(pdf_file, arcname='Titanic_EDA_Report.pdf')
    # Add dataset files
    for file_name in os.listdir(dataset_dir):
        file_path = os.path.join(dataset_dir, file_name)
        zipf.write(file_path, arcname=file_name)

zip_filename
