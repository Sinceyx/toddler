# toddler
learn to crawl website by scrapy

# python version:3.8.2


## Run with docker at directory of toddler project
`cp toddler/Dockerfile ./`

`cp toddler/toddler/requirements.txt`

`docker build -t luton-spider .`

`docker run -it -v /Users/xin.yu/Downloads/spider_output:/toddler_proj/output luton-spider`

## Run with terminal at `/toddler`

`python toddler/go_spider.py crawl luton`

## Run pylint

`pylint toddler/`

## Run unittest

`python -m unittest tests/test_luton_spider.py`
