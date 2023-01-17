# -*- coding: utf8 -*-
from requests import Session
import pyuseragents
from concurrent.futures import ThreadPoolExecutor
from ctypes import windll
from urllib3 import disable_warnings
from loguru import logger
from sys import stderr, exit
from os import system
from msvcrt import getch

disable_warnings()
def clear(): return system('cls')


logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white>"
                          " | <level>{level: <8}</level>"
                          " | <cyan>{line}</cyan>"
                          " - <white>{message}</white>")
windll.kernel32.SetConsoleTitleW('Rey Autoreger | by MorS')
print('Telegram - t.me/morsxdd')
print('Twitter - twitter.com/MorS1337\n')

class Wrong_Response(BaseException):
    pass

def main(email):
    for _ in range(10):
        try:
            session = Session()
            session.headers.update({
                'user-agent': pyuseragents.random(),
                'accept': '*/*',
                'accept-language': 'ru-RU,ru;q=0.9',
                'origin': 'https://rey.xyz',
                'referer': 'https://rey.xyz/',
                'content-type': 'application/json'})
            
            r = session.post('https://rey.xyz/api/send',
                                json={"email": email,
                                    "context": "teaser"})
            if r.status_code != 202:
                raise Wrong_Response
            
            
            
        except Wrong_Response:
            logger.error(f'{email} | Wrong response, status code: '
                         f'{r.status_code}, response text: {r.text}')
            
        except Exception as error:
            logger.error(f'{email} | Unexpected error: {error}')
            
        else:
            logger.success(f'{email} | The account has been successfully registered')

        with open('registered.txt', 'a') as file:
            file.write(f'{email}\n')

        return

    with open('unregistered.txt', 'a') as file:
        file.write(f'{email}\n')
        
if __name__ == '__main__':
    threads = int(input('Threads: '))
    emails_folder = input('Drop .txt with emails: ')

    with open(emails_folder, 'r') as file:
        emails = [row.strip() for row in file]

    clear()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(main, emails)

    logger.success('Работа успешно завершена')
    print('\nPress Any Key To Exit..')
    getch()
    exit()
