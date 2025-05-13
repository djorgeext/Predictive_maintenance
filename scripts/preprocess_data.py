import requests
import zipfile
import io
import os
import pandas as pd

url = "https://archive.ics.uci.edu/static/public/601/ai4i+2020+predictive+maintenance+dataset.zip"
response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors

zip_file = zipfile.ZipFile(io.BytesIO(response.content))

# Extract the contents to a directory (e.g., 'data')
extract_dir = 'data/raw'
if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

zip_file.extractall(extract_dir)

print(f"Downloaded and extracted data to '{extract_dir}'")

# Assuming the CSV file is named 'ai4i2020.csv'
csv_file_path = os.path.join(extract_dir, 'ai4i2020.csv')

# Read the CSV file into a Pandas DataFrame
preprocessed_data = pd.read_csv(csv_file_path)

