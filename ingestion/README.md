# Ingestion Module

## Overview

Ingestion Module relates to the scraping of airBnB data.

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

```
TODO
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

