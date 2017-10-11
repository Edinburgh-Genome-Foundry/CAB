import os

data_path = os.path.join("app", "data", "example_data_file.txt")
with open(data_path, "r") as f:
    DATA = f.read()
