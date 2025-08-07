# Video to TikTok Converter

A simple Python script that converts any video to TikTok's vertical 9:16 format.

## Features

- Converts videos to 1080x1920 (9:16 aspect ratio)
- Smart handling of different aspect ratios:
  - **Wide videos**: Center-cropped to fit
  - **Tall videos**: Black bars added (pillarboxed)
  - **Perfect ratio**: Simply resized
- Preserves audio quality
- Easy command-line interface

## Installation

1. Install the required dependency:
```bash
pip install -r requirements.txt
```

## Usage

### Basic usage:
```bash
python video_to_tiktok.py input_video.mp4
```
This creates `input_video_tiktok.mp4` in the same directory.

### Specify output filename:
```bash
python video_to_tiktok.py input_video.mp4 my_tiktok_video.mp4
```

## Supported Formats

The script supports most common video formats including:
- MP4
- AVI
- MOV
- MKV
- And more (anything supported by moviepy)

## Example

```bash
# Convert a landscape video to TikTok format
python video_to_tiktok.py landscape_video.mp4

# Output: landscape_video_tiktok.mp4 (1080x1920, center-cropped)
```

## Requirements

- Python 3.6+
- moviepy 1.0.3

## How it works

1. **Analyzes** the input video's aspect ratio
2. **Determines** the best conversion method:
   - If too wide: center crops horizontally
   - If too tall: adds black bars on sides
   - If perfect: just resizes
3. **Outputs** a 1080x1920 video optimized for TikTok
