# StarTech-Project
# Monitor Flicker / Display Anomaly Detector (Camera-based)

# Monitor Flicker / Display Anomaly Detector (Camera-based)

A lightweight tool that uses a camera pointed at a monitor to detect **display anomalies** over time (e.g., brightness flicker, black flashes, full-screen mosaic/artifacts, banding/rolling-shutter patterns).  
Designed for **long-duration monitoring** without saving full video: it stores **compact numeric features + anomaly flags**.

## What counts as “flicker” in this project?
Flicker means **any abnormal temporal instability** of the displayed image, including but not limited to:
- Brightness flicker / PWM-like modulation
- Sudden black/white flashes
- Full-screen mosaic / artifact bursts
- Unstable banding patterns captured by rolling shutter
- Localized abnormal changes (within a selected ROI)

## Features
- Real-time camera capture (USB webcam / Continuity Camera / etc.)
- Fixed ROI analysis (default: center region; interactive ROI selection planned)
- Per-frame feature extraction (no full video storage)
- Sliding-window statistics (e.g., 1s windows)
- Baseline calibration (learn “normal” behavior first)
- Anomaly decision + CSV logging
- (Optional) Save short evidence clips/snapshots on anomaly (planned)

## How it works (High-level)
Pipeline:
1. Capture frames from camera
|
V
2. Crop ROI (region on the monitor)
|
V
3. Convert to grayscale + preprocess
|
V
4. Extract compact features per frame, e.g.:
   - mean luminance
   - frame-difference energy
   - edge/gradient energy
   - (optional) row-banding score
|
V
5. Aggregate features over a sliding time window
|
V
6. Compare with baseline stats → compute anomaly score → flag flicker/anomaly
|
V
7. Log results to CSV (small storage footprint)

## Requirements
- OS: macOS / Windows / Linux
- Camera: any webcam; higher FPS helps (60/120 preferred)

<!-- ## Installation
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt -->