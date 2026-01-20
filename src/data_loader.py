import zipfile
import pandas as pd

def load_uidai_zip(zip_path):
    """
    Load the first CSV file from a UIDAI ZIP archive.
    """
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            csv_files = [f for f in zip_ref.namelist() if f.lower().endswith(".csv")]
            if len(csv_files) == 0:
                raise ValueError("ZIP file contains no CSV files")
            with zip_ref.open(csv_files[0]) as file:
                df = pd.read_csv(file)
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading ZIP file {zip_path}: {e}")
