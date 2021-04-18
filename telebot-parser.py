import telebot, requests, os, re
from bs4 import BeautifulSoup

API_TOKEN = '' # set your telegram-bot token here

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
    rows = set(lines)
    result = []
    for row in rows:
        if not row:
            pass
        else:
            try:
                r = requests.get(row, timeout=2)
                soup = BeautifulSoup(r.content, 'html.parser')
                exist = soup.find_all(text=re.compile(wts, re.I))
                if not exist:
                    pass
                else:
                    result.append(row)
            except requests.exceptions.RequestException as e:
                pass
    if not result:
        bot.send_message(message.chat.id, 'Nothing found')
    else:
        result = '\n'.join(result)
        bot.send_message(message.chat.id, 'Your word was found on:\n' + result, disable_web_page_preview=True)
    rfile.close()
    os.remove('urls.txt')

    
bot.enable_save_next_step_handlers(delay=2)
bot.polling()
