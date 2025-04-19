# Animal API Web Generator

A Python application that generates a web page with information about animals using the API Ninjas Animals API.

## Features

- Fetches animal data from the API Ninjas Animals API
- Generates a responsive HTML page with animal information
- Displays animal name, diet, location, and type
- Modern and clean UI design

## Requirements

- Python 3.x
- Required packages:
  ```bash
  pip install requests python-dotenv
  ```

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the root directory with your API key:
   ```
   API_KEY='your-api-key-here'
   ```

## Usage

1. Run the script:
   ```bash
   python animals_web_generator.py
   ```
2. Enter an animal name when prompted
3. The generated HTML file will be saved as `animals.html`

## Files

- `animals_web_generator.py` - Main Python script
- `data_fetcher.py` - Module for fetching animal data from the API
- `animals_template.html` - HTML template for the generated page
- `animals.html` - Generated HTML file (created when running the script)
- `.env` - Environment variables file (not tracked by git)

## Note

This project uses the API Ninjas Animals API. Make sure you have a valid API key and have set it up in your `.env` file. 