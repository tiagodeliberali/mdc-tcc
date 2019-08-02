import pandas as pd

# load dataset
data = pd.read_csv("./Landmarks/train.csv")
print("total number of lines: ", data.shape[0])

# group information by landmark_id
gdata = pd.DataFrame(data.groupby("landmark_id").count())
gdata.drop(['url'], axis=1, inplace=True)
gdata.rename(columns={"id": "total"}, inplace=True)
print("total number of landmarks: ", gdata.shape[0])

# save landmarks with more images to csv
top_gdata = gdata.sort_values(by=['total'], ascending=False).head(150)
print("filtered number of landmarks: ", top_gdata.shape[0])
top_gdata.to_csv("./Landmarks/top_landmarks_counts.csv")

# get files from top landmarks
merged_data = pd.merge(top_gdata, data, on='landmark_id', how='inner')
merged_data.drop(['total'], axis=1, inplace=True)
print("filtered number of lines: ", merged_data.shape[0])
merged_data.to_csv("./Landmarks/top_landmarks_url.csv")
