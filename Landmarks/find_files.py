import glob
import pandas as pd
import shutil
import subprocess

# read filenames and image ids
PATH = "/media/slow/landmarks/**/*.jpg"
DESTINATION_PATH = "/media/slow/landmarks/selected/"
files = []

for filename in glob.iglob(PATH, recursive=True):
     files.append([filename[-20:-4], filename])

data = pd.DataFrame(files)
data.columns = ["id", "path"]
print("number of files: ", data.shape[0])

# read selected images
selected_data = pd.read_csv("./Landmarks/top_landmarks_url.csv")
print("number of selected image files: ", selected_data.shape[0])

# associated selected images with local paths
merged_data = pd.merge(selected_data, data, on='id', how='inner')
print("number of selected image found: ", merged_data.shape[0])

# create folders
landmarks = pd.read_csv("./Landmarks/top_landmarks_counts.csv")
for index, row in landmarks.iterrows():
    bashCommand = f"mkdir {DESTINATION_PATH}{row['landmark_id']}/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

# move files to a central place
count = 0
for index, row in merged_data.iterrows():
    count = count + 1
    bashCommand = f"mv {row['path']} {DESTINATION_PATH}{row['landmark_id']}/"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
print("number of moved images: ", count)
