import pandas as pd
from sklearn.model_selection import train_test_split
import os

def remove(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)

# CONFIG
ORIGINAL_CSV_PATH = "./Landmarks/train.csv"
DATA_PATH = "./Landmarks/data"

# remove old data
remove(f"{DATA_PATH}/top_landmarks_counts.csv")
remove(f"{DATA_PATH}/top_landmarks_all.csv")
remove(f"{DATA_PATH}/top_landmarks_train.csv")
remove(f"{DATA_PATH}/top_landmarks_test.csv")
remove(f"{DATA_PATH}/subset_landmarks_all.csv")
remove(f"{DATA_PATH}/subset_landmarks_train.csv")
remove(f"{DATA_PATH}/subset_landmarks_test.csv")

# load dataset
data = pd.read_csv(ORIGINAL_CSV_PATH)
print("total number of lines on MDC file: ", data.shape[0])

# group information by landmark_id
gdata = pd.DataFrame(data.groupby("landmark_id").count())
gdata.drop(['url'], axis=1, inplace=True)
gdata.rename(columns={"id": "total"}, inplace=True)
print("total number of landmarks: ", gdata.shape[0])

# save landmarks with more images to csv
top_gdata = gdata.sort_values(by=['total'], ascending=False).iloc[50:150, :]
print("filtered number of landmarks: ", top_gdata.shape[0])
top_gdata.to_csv(f"{DATA_PATH}/top_landmarks_counts.csv", index=False)

# get files from top landmarks
merged_data = pd.merge(top_gdata, data, on='landmark_id', how='inner')
merged_data.drop(['total'], axis=1, inplace=True)
print("filtered number of lines: ", merged_data.shape[0])
merged_data.to_csv(f"{DATA_PATH}/top_landmarks_all.csv", index=False)

# split train  and test sets
train, test = train_test_split(merged_data, test_size = 0.2, random_state = 42)

train.to_csv(f"{DATA_PATH}/top_landmarks_train.csv", index=False)
test.to_csv(f"{DATA_PATH}/top_landmarks_test.csv", index=False)

# get a subset of landmarks
_, subset = train_test_split(top_gdata, test_size = 0.2, random_state = 42)
print("subset number of landmarks: ", subset.shape[0])

# get files from subset landmarks
subset_merged_data = pd.merge(subset, data, on='landmark_id', how='inner')
subset_merged_data.drop(['total'], axis=1, inplace=True)
print("subset number of lines: ", subset_merged_data.shape[0])
subset_merged_data.to_csv(f"{DATA_PATH}/subset_landmarks_all.csv", index=False)

# split train  and test sets
subset_train, subset_test = train_test_split(subset_merged_data, test_size = 0.2, random_state = 42)

subset_train.to_csv(f"{DATA_PATH}/subset_landmarks_train.csv", index=False)
subset_test.to_csv(f"{DATA_PATH}/subset_landmarks_test.csv", index=False)
