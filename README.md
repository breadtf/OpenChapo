# OpenChapo 🤖
Open-Source discord AI chatbot using Ollama, based on the El Chapo bot from the WSE Discord Server.

## Setup

First, create the model. (Make sure you have llama2-uncensored installed already)
```
ollama create chapo -f ./Modelfile
```
Then, create the discord bot in the [Discord Dev Portal](https://discord.com/developers/)
Make sure you enable the `Message Content Intent`
![image](https://github.com/breadtf/OpenChapo/assets/103989916/a8abdd53-3315-4e53-92fa-75cb1a5b6fb9)

Then, open `config.py` and change the token placeholder to your discord bot token.

Once this is all done, run `python3 -m pip install -r requirements.txt`.

Then, finally, run `python3 main.py` to run your El Chapo bot.

## Usage

You can message chapo by typing his name into the message, like this:

![image](https://github.com/breadtf/OpenChapo/assets/103989916/8748db16-d1e9-469a-9462-8d0ce0c5f2d5)

Chapo will respond in 10-15 seconds depending on your CPU power.
