import discord
import config
import requests

history = []

def getChapo(getMessage):
    # Define the payload data for the request

    prompt = f"""
    
    MESSAGE-HISTORY: {history}
    PROMPT-MESSAGE: {getMessage}

    """

    payload = {
        "model": "chapo",
        "prompt": prompt,
        "stream": False
    }

    # Send a POST request to the Ollama API endpoint
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=15)
    except Exception as e:
        print(f"Error: {e}") 
        return "IDK"
    # Check if the request was successful
    if response.status_code == 200:
        # Print the generated text from the model
        return response.json()["response"]
    else:
        print("Error:", response.text)
        return "IDK"

# Define your bot token here
TOKEN = config.token

# Define the intents
intents = discord.Intents.all()
intents.messages = True

# Create a bot instance
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author != client.user:
        # Check if the message contains "chapo"
        if 'chapo' in message.content.lower():
            # Respond to the message
            print("Sending message...")
            print(history)
            async with message.channel.typing():
                await message.reply(getChapo(message.content))

    history.append(f"{message.author}: {message.content}")
    if len(history) > 10:
        history.pop(0)
# Run the bot
client.run(TOKEN)
