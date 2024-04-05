import zipfile
import io
import requests
import pandas as pd

from .const import GTFS_FILE_FIELDS_TYPES


def read_gtfs_zip_obj(gtfs_zip: zipfile.ZipFile) -> dict[str, dict[str, pd.DataFrame]]:
    """
    Reads a gtfs.zip object from a URL or local path and returns a dictionary of pandas DataFrames
    
    The dictionary is structured as follows:
        
        {
            mode_id: {
                table_name: pd.DataFrame
            }
        }
    """
    DFK = {}
    for item in gtfs_zip.namelist():
        if not item.endswith('/'): # Check if the item is a directory
            continue
        mode_id = item.strip('/')
        
        DFK[mode_id] = {}

        google_transit_zip_path = f"{mode_id}/google_transit.zip"
        with gtfs_zip.open(google_transit_zip_path) as google_transit_file:
            with zipfile.ZipFile(google_transit_file, 'r') as transit_zip:

                for nested_file_name in transit_zip.namelist():
                
                    if not nested_file_name.endswith('.txt'):
                        continue
            
                    table_name = nested_file_name.removesuffix('.txt')
            
                    with transit_zip.open(nested_file_name) as nested_file:
                        
                        DFK[mode_id][table_name] = pd.read_csv(nested_file, keep_default_na=False, low_memory=False, na_values=[''], dtype=GTFS_FILE_FIELDS_TYPES[table_name])
    
    return DFK


def read_gtfs_zip(url_or_path : str = "http://data.ptv.vic.gov.au/downloads/gtfs.zip") -> dict[str, dict[str, pd.DataFrame]]:
    """
    Reads a gtfs.zip file from a URL or local path and returns a dictionary of pandas DataFrames
    
    The dictionary is structured as follows:
        
        {
            mode_id: {
                table_name: pd.DataFrame
            }
        }
    """

    assert url_or_path.endswith('.zip'), "File must be a .zip file"   
    
    if ":" in url_or_path: # If url_or_path is a URL
        
        response = requests.get(url_or_path, stream=True)

        if response.status_code == 200:
            # Create a ZipFile object from the response content
            with zipfile.ZipFile(io.BytesIO(response.content)) as gtfs_zip:
                return read_gtfs_zip_obj(gtfs_zip=gtfs_zip)
    
    with zipfile.ZipFile(url_or_path, 'r') as gtfs_zip:
        return read_gtfs_zip_obj(gtfs_zip=gtfs_zip)
    