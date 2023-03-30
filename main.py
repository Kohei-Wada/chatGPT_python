import os
import openai
import sys

# Define OpenAI API key 
openai.api_key = os.environ['APIKEY_GPT3']

# Set up the model and prompt
model_engine = "text-davinci-003"


def print_console(): 
    GREEN = '\033[32m'
    END   = '\033[0m'
    print(GREEN + '<chatGPT>' + END, end='')
    sys.stdout.flush()


def interactive_loop():
    while True:
        print_console()

        try:
            chat = sys.stdin.readline() 
        except BaseException as e:
            print(e) # show nothing
            break

        if not chat:
            break
        elif chat == "\n": 
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
            print(e) # show nothing
            break


        response = completion.choices[0].text
        print(response)

    print("Byebye!")

def main(): 
    interactive_loop()

main() 
