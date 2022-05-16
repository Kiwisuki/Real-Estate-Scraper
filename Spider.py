import logging
from Toolbox import *
import random
from importlib import reload
import logging

reload(logging)
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%I:%M:%S')

def main():
    nts = ['butai', 'butu-nuoma', 'namai', 'patalpos', 'namu-nuoma', 'patalpu-nuoma']
    while True:
        for nt in nts:
            links = scrape_type_links(nt)
            links = filter_links(links, get_ids())
            links = random.shuffle(links)
            for idx, link in enumerate(links):
                logging.info(f'{len(links) - idx} ads left to scrape, scraped {idx} ads, Type: {nt}')
                try:
                    scrape_ad(link, nt)
                except BotDetectedException:
                    logging.info('Bot detected, skipping')
                    pass
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    logging.critical(f'DANGER:{e}')
                    pass


if __name__ == '__main__':
    main()