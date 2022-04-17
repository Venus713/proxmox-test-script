import os
import logging
import requests

logging.basicConfig(filename='log.txt',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger('ProxmoxLxcTest')


def get_currency_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    print(data)
    return data


logger.info('You are running this python script to get current prices')

data = get_currency_price()

logger.info(f"current prices: {data}")
