# toddler
learn to crawl website by scrapy

# python version:3.8.2


## Run with docker at the directory of toddler project
`cp toddler/Dockerfile ./`

`cp toddler/toddler/requirements.txt ./`

`docker build -t luton-spider .`

`docker run -it -v ${YOUR_DIR}:/toddler_proj/output luton-spider`

## Run with terminal at `/toddler`

`python toddler/go_spider.py crawl luton`

## Run pylint at `/toddler`

`pylint toddler/`

## Run unittest at `/toddler`

`python -m unittest tests/test_luton_spider.py`
