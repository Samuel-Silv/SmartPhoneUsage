import os
import json
import pandas as pd
   
dataset_name = "bhadramohit/smartphone-usage-and-behavioral-dataset"

def download_dataset(dataset_name):
    command = f"kaggle datasets download -d {dataset_name}"
    try:
        os.system(command)''
    except Exception as e:
        print(f"Falha ao tentar realizar o download: {e}")
    print('dowload zip realizado')

def unzip_file(dataset_name, zip_path, extract_to='.'):
    download_dataset(dataset_name)
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    except FileNotFoundError as e:
        print(f"Erro ao extrair o csv: {e}")
    print('csv extraido')