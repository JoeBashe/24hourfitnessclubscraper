# 24 Hour Fitness Club Location Scraper

## Set up

```shell
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## club.py

Gets the raw data.

Usage:

```shell
./env/bin/scrapy runspider club.py -o 24hourfitnessclubs.csv
```

## data-cleaner.py

Geocodes the addresses to lat/lon points.

To use it, get an API key from geocod.io, and add it to the GEOCODIO_API_KEY variable in 
[data-cleaner.py](data-cleaner.py) 