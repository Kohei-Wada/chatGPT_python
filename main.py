import os
import openai
import sys
import readline
import atexit

# Define OpenAI API key 
openai.api_key = os.environ['APIKEY_GPT3']

# Set up the model and prompt
model_engine = "text-davinci-003"

GREEN = '\033[32m'
END   = '\033[0m'
console = GREEN + '<chatGPT>' + END

historyfile = os.path.join(os.path.expanduser("~"), ".chatGPT_history")

def interactive_loop():
    try:
        readline.read_init_file()
    except:
        pass
    try:
        readline.read_history_file(historyfile)
    except FileNotFoundError:
        open(historyfile, 'wb').close()

    while True:
        try:
            chat = input(console)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("^C")
            continue

        if not chat: 
            continue
        try:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=chat,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
        except BaseException as e:
            break

        response = completion.choices[0].text
        print(response)

    print("Byebye!")
    atexit.register(readline.write_history_file, historyfile)

def main(): 
    interactive_loop()

if __name__ == "__main__": 
    main() 
