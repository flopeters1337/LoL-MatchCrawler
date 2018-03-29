
import requests
import json
from definitions import riot_key
from src.crawler import LoLCrawler


if __name__ == '__main__':
    crawler = LoLCrawler(riot_key=riot_key)
    crawler.crawl(31128970)
