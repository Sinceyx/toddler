#基础镜像
FROM python:3.8.2

RUN mkdir /toddler

ADD /toddler /toddler_proj

WORKDIR /toddler_proj

RUN pip3 install -r toddler/requirements.txt

CMD python ./toddler/go_spider.py crawl luton


