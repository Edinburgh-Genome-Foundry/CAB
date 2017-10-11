from base64 import b64encode

def zip_data_to_html_data(zip_data):
    return 'data:application/zip;base64,' + b64encode(zip_data).decode("utf-8")
