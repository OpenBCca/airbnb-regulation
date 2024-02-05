# AirBnb Scrapping

## Overview

Scrapes listing data from AirBnb.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)


## Installation


1. Create and activate a virtual environment:

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Customize the Scrapy spider for your specific needs. Edit `spiders/your_spider.py` and configure start URLs, item
   definitions, and scraping logic.

2. Run the spider:

    ```bash
    scrapy crawl your_spider
    ```

3. Explore the scraped data in the console or check the output files, depending on your pipeline configurations.

## Folder Structure
```
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

