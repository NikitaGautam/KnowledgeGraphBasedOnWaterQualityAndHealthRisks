
### WebOfScienceScrapper:
- Download chrome webdriver from the following link: https://chromedriver.chromium.org/downloads
- Path of this chrome driver should be provided as in input while running scrapper.py

## Use Scrapper.py to scrape urls from WebOfScience and NationalLilbraryOfMedicine with specific keywords.

python scrapper.py driverpath=<Path To ChromeDriver>


## Combine the extracted abstracts using combine_data.py
python combine_data.py rootdir=<Sourcedir> outdir=<Destinationdir>

## Convert PDF to text files using converter.py