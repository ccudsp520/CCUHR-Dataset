import os
import csv
import cv2
import argparse
from video_realsense_file import Video

parser = argparse.ArgumentParser(description="CCUHR Dataset")
parser.add_argument("--root_path",type=str, default="CCUHR_Dataset", help="CCUHR Dataset root path")
parser.add_argument("--dataset_name",type=str,help="the specific dataset name")
args = parser.parse_args()

def reader(root_path: str, dataset_name: str):
    '''
        root_path is CCUHR Dataset path
    '''
    csv_file = os.path.join(root_path, dataset_name)
    gt_data = [] 
    data_path = []

    with open(csv_file, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            gt_data.append(float(row['GT']))
            data_path.append(os.path.join(root_path, row['data path']))
    return data_path, gt_data

# dataset_path = r"E://My_research/my_Research(the most important)/rPPG_Data/rppg_Dao/CCUHR_Dataset/"
args.dataset_path = r"E://My_research/my_Research(the most important)/rPPG_Data/rppg_Dao/CCUHR_Dataset"
args.dataset_name = "motion_10s_path_gt.csv"
data_path, gt_data = reader(args.dataset_path, args.dataset_name)
video = Video()
# read the first video in motion_10s_path_gt.csv
video.dirname = data_path[0]
video.start()
cnt = 0
while(True):
    cnt = cnt+1
    color, nir = video.get_frame()
    cv2.imshow("test", nir)
    cv2.waitKey(1)
print(f"the total frame is {cnt}")

