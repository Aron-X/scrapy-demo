FROM python:3
MAINTAINER aron.xu

WORKDIR /app
COPY . /app

RUN pip install Scrapy \
    && pip install requests \
    && pip install bs4

CMD ["scrapy", "crawl", "lagou"]
#build : docker build -t scrapy-demo:latest . --no-cache
#run : docker run --name scrapy-demo-container -d scrapy-demo:latest