# CCUHR-Dataset

## Overview

The CCUHR-Dataset is a dual-modality dataset containing unaligned RGB and Near-Infrared (NIR) optical videos for heart rate (HR) estimation. This dataset includes synchronized HR ground truth (GT) measurements obtained using a BIOPAC PPG 100C instrument with a contact-based sensor. The dataset aims to facilitate research in remote photoplethysmography (rPPG) and multimodal HR detection.

## Data Collection

- **Number of Subjects:** 22 individuals
- **Total Video Clips:** 116
- **Camera Used:** Intel RealSense D435
- **Resolution:** 640 × 480 pixels
- **Frame Rate:** 30 FPS (frames per second)
- **Ground Truth HR Measurement:** BIOPAC PPG 100C

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

## Applications

The CCUHR-Dataset can be used for:

- Remote photoplethysmography (rPPG)
- Heart rate estimation from RGB and NIR modalities
- Multimodal fusion for physiological signal analysis
- Head motion and illumination robustness analysis in HR detection

## Citation

If you use the CCUHR-Dataset in your research, please cite the corresponding paper:

```
@article{CCUHR-Dataset,
  author    = {Author Name},
  title     = {CCUHR-Dataset: A Dual-Modality Dataset for Remote Heart Rate Estimation},
  journal   = {Journal Name},
  year      = {202X},
  volume    = {XX},
  number    = {X},
  pages     = {XX-XX}
}
```

## Contact

For any questions or access requests, please contact:

- **Email:** [example@university.edu](mailto\:example@university.edu)
- **Institution:** National Chung Cheng University

給我read讓我可以複製

