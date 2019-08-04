import glob
import pandas as pd
import shutil
import subprocess
import os

# read filenames and image ids
PATH = "/media/slow/data/landmarks/"

def mkdir(directory_path):
    if not os.path.exists(directory_path):
        bashCommand = f"mkdir {directory_path}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        process.communicate()

def copy(group):
    destination_base_path = f"{PATH}{group}"
    mkdir(destination_base_path)

    data = pd.read_csv(f"./Landmarks/data/top_landmarks_{group}.csv")

    for item in data.landmark_id.unique():
        directory_path = f"{destination_base_path}/{item}"
        mkdir(directory_path)

    for _, row in data.iterrows():
        bashCommand = f"cp {PATH}{row.landmark_id}/{row.id}.jpg {destination_base_path}/{row.landmark_id}/"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        process.communicate()

copy("train")
copy("test")
