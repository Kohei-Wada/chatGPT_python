#!/bin/python3

import os
import openai
import sys
import readline
import atexit
from functools import reduce

openai.api_key = os.environ['APIKEY_GPT3']

GREEN = '\033[32m'
END   = '\033[0m'
console = GREEN + '<chatGPT>' + END
historyfile = os.path.join(os.path.expanduser("~"), ".chatGPT_history")

def chat(history):
    res = openai.ChatCompletion.create(
        messages=history,
        max_tokens=1024,
        n=1,
        stream=True,
        temperature=0.5,
        stop=None,
        presence_penalty=0.5,
        frequency_penalty=0.5,
        model="gpt-3.5-turbo"
    )

    fullResponse = '' 
    for chunk in res:
        text = chunk['choices'][0]['delta'].get('content')
        if text: 
            fullResponse += text
            print(text, end='', flush=True) 

    return fullResponse

def main_loop(): 
    history = []
    while True:
        try:
            text = input(console)
        except EOFError:
            break
        except KeyboardInterrupt:
            print('^C')
            continue

        if text:
            user_action = {"role": "user", "content": text}
            history.append(user_action)
            try:
                res = chat(history)
                chatGPT_responce = {"role": "assistant", "content": res}
                history.append(chatGPT_responce) 
            except:
                pass
            print('')

def interactive_shell():
    try:
        readline.read_init_file()
    except:
        pass
    try:
        readline.read_history_file(historyfile)
    except FileNotFoundError:
        open(historyfile, 'wb').close()

    main_loop()
    print("Byebye!")
    atexit.register(readline.write_history_file, historyfile)

def main(): 
    interactive_shell()

if __name__ == "__main__": 
    main() 
