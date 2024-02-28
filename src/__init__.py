from getting_data_from_source import download_zips_and_unzip
from push_to_aws import list_files_in_folder
def __init__():
    list = list_files_in_folder('./covid__history')
    if list == 404:
       download_zips_and_unzip()
    else:
        print("all good")   

# Run everything
__init__()
