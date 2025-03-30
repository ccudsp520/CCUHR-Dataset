# CCUHR-Dataset

## Overview

The CCUHR-Dataset is a dual-modality dataset containing unaligned RGB and Near-Infrared (NIR) optical videos for heart rate (HR) estimation. This dataset includes synchronized HR ground truth (GT) measurements obtained using a BIOPAC PPG 100C instrument with a contact-based sensor. The dataset aims to facilitate research in remote photoplethysmography (rPPG) and multimodal HR detection.

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

