# CCUHR-Dataset

## Overview

The CCUHR-Dataset is a dual-modality dataset containing unaligned RGB and Near-Infrared (NIR) optical videos for heart rate (HR) estimation. This dataset includes synchronized HR ground truth (GT) measurements obtained using a BIOPAC PPG 100C instrument with a contact-based sensor. The dataset aims to facilitate research in remote photoplethysmography (rPPG) and multimodal HR detection.

## How to install CCUHR Dataset
Due to the limitation of disk szie in Github, please dowload the dataset via following hyperlink: [CCUHR Dataset]((https://ccu365-my.sharepoint.com/:u:/g/personal/ieewnl_office365_ccu_edu_tw/EcBZOCHSeKNMi1gMGkREqk8BnHcT7pjpnzCPprCsHekSUA?e=aKFjyn)) and enter the password: `CCUHR520`.

## How to use CCUHR Dataset
### Dataset Reader

To use the CCUHR-Dataset, you can utilize the `Dataset_reader.py` script. The parameters required are:
- `root_path`: The path to the CCUHR_Dataset.
- `dataset_name`: The CSV file used for model evaluation, containing video paths and corresponding ground truth HR values.

### Example Usage
```bash
python Dataset_reader.py --root_path CCUHR_Dataset --dataset_name motion_10s_path_gt.csv
```
Explanation

The CSV file contains specific videos in the dataset along with their respective ground truth HR values. You can iterate through the CSV file and use `video_realsense_file.py` to read each video for model evaluation.

## Data Collection

- **Camera Used:** Intel RealSense D435
- **Resolution:** 640 × 480 pixels
- **Frame Rate:** 30 FPS (frames per second)

## Data Structure

The dataset consists of 116 video clips, categorized as follows:

- **Duration:**
  - 62 videos of 10 seconds
  - 54 videos of 20 seconds
- **Scenarios:**
  - **Non-Motion:** 77 videos (66.4%)
    - Good or low illumination
    - No head motion
  - **Motion:** 39 videos (33.6%)
    - Good illumination
    - Facial expression changes or medium head rotation

## Citation

If you use the CCUHR-Dataset in your research, please cite the corresponding paper:

```
@article{lie2023heart,
  title={Heart rate estimation from facial image sequences of a dual-modality RGB-NIR camera},
  author={Lie, Wen-Nung and Le, Dao-Quang and Lai, Chun-Yu and Fang, Yu-Shin},
  journal={Sensors},
  volume={23},
  number={13},
  pages={6079},
  year={2023},
  publisher={MDPI}
}
```

## Contact

For any questions , please contact Dr.Wen-Nung Lie:

- **Email:** [ieewnl@ccu.edu.tw](mailto\:ieewnl@ccu.edu.tw)
- **Institution:** National Chung Cheng University

