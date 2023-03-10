import os
import openai

print('Welcome to MathieuGPT, you\'ll need an OpenAI API key (https://platform.openai.com)\nThis script requires python 3.x and the openai package to run\nWrite your queries in English or French and input \'exit\' at any point to exit and return to the terminal')
openai.organization = "org-vNip1LEkzDa2rbFClEkXncDz"
openai.api_key = input("\nChatGPT API Key: ")

messages=[]
messages.append({"role": "system", "content": "you are an assistant with a french accent, you occasionally swear in english and often respond sarcastically"})

while True:
    content = input("\n>>> User: ")
    if content != "exit":
      messages.append({"role": "user", "content": content})
      completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages

      )

      chat_response = completion.choices[0].message.content
      print(f'\n>>> MathieuGPT: {chat_response}')
      messages.append({"role": "assistant", "content": chat_response})
    else:
      break
