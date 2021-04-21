import telebot, os, re
from bs4 import BeautifulSoup

import logging

import asyncio, aiohttp

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Type some url(s)')
  bot.register_next_step_handler(sent, input)


def input(message):
    with open('urls.txt', 'a') as wfile:
        wfile.write(f'\r'+message.text)
    sent = bot.send_message(message.chat.id, 'Add a word to search')
    bot.register_next_step_handler(sent, check)


def check(message):
    wts = message.text # word to search
    wts = str(wts)
    with open('urls.txt', 'r') as rfile:
        lines = [line.rstrip() for line in rfile]
    urls = list(filter(None, list(set(lines))))
    result = []
    async def fetch(url: str) -> str:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, ssl=False, timeout=2) as resp:
                    html = await resp.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    exist = soup.find_all(text=re.compile(wts, re.I))
                    if exist:
                        result.append(url)
                    else:
                        pass
            except Exception as e:
                pass

    async def getdata(urls):
            tasks = [ fetch(url) for url in urls ]
            result = await asyncio.gather(*tasks)

    asyncio.run(getdata(urls))


    if not result:
        bot.send_message(message.chat.id, 'Nothing found')
    else:
        result = '\n'.join(result)
        bot.send_message(message.chat.id, 'Your word was found on:\n' + result, disable_web_page_preview=True)
    rfile.close()
    os.remove('urls.txt')

bot.enable_save_next_step_handlers(delay=2)
bot.polling()
