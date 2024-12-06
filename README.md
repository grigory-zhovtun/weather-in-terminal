# Weather Fetcher

This Python script retrieves weather information for specified locations using the [wttr.in](https://wttr.in) service. The script is designed for quick weather checks in a simple text format.

---

## Features
- Fetches weather data for multiple locations.
- Displays results in Russian (`lang=ru`).
- Simplified and concise output without unnecessary text.

---

## Prerequisites
- Python 3.6 or later
- A `requirements.txt` file specifying dependencies

---

## Installation and Setup

1. **Clone the repository or download the script:**  
   Ensure you have the `main.py` script and the `requirements.txt` file.

2. **(Optional) Create and activate a virtual environment:**  
   While not strictly required, using a virtual environment is recommended to avoid conflicts with other Python packages.
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate          # Windows
3. Install dependencies from requirements.txt:
This ensures consistent and tested versions of the packages.
   ```bash
   pip install -r requirements.txt
4. Run the script:
   ```bash
   python main.py