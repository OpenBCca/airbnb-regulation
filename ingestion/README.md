# Ingestion Module

## Overview

Ingestion Module relates to the scraping of airBnB data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)


## Installation


1. Create and activate a virtual environment:

    ```
    python -m venv venv
    venv\Scripts\activate.bat
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Go into the directory containing `airbnb_listings` directory 
   ```
   cd .\airbnb_scrapping\
   ```
2. Run the `listing_spider` spider using the scrapy command. Specify the name of the output file.
   ```
   scrapy crawl listing_spider -O [file_name]   
   ```

## Folder Structure
```
├── airbnb_scarping/          # Contains the scrapy project for scarping 
├── airbnb_listings/          # Main Python package for the Scrapy project.
│ ├── init.py                 # Empty file indicating that the directory should be considered a Python package.
│ ├── items.py                # Definition of Scrapy items, specifying the structure of the data to be scraped.
│ ├── middlewares.py          # Custom or enabled built-in middlewares for request and response processing.
│ ├── pipelines.py            # Definition of item pipelines to process and store scraped data.
│ ├── settings.py             # Project settings for Scrapy, allowing customization of its behavior.
│ └── spiders/                # Directory containing spider scripts.
│ ├── init.py                 
│ └── your_spider.py
└── README.md
```

