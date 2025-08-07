# Internship 2025 Tasks

This folder contains solutions to internship tasks for Gotit in 2025. Each script is self-contained and demonstrates the use of modern Python tools and APIs.

## Contents
- `Haiku_Creator.py` — Generates haikus using Google Gemini API.
- `describe_and_translate.py` — Describes images and translates the description to Spanish using Gemini.
- `.env.example` — Template for environment variables required by the scripts.

## Setup
1. **Create a virtual environment (recommended):**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On Mac/Linux
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your API keys (e.g., `GEMINI_API_KEY`).

## Usage
- **Haiku Creator:**
  ```sh
  python Haiku_Creator.py
  ```
- **Describe and Translate:**
  ```sh
  python describe_and_translate.py <path_to_image>
  ```
  If no image path is provided, you will be prompted to enter one.

## Notes
- Do **not** commit `.env` files with secrets. The root `.gitignore` already prevents this.
- All scripts require a valid Google Gemini API key in your `.env` file.
- For more details, see inline comments in each script.
