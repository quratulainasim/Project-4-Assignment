import discord
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Regular hello command
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    # Gemini command using &
    elif message.content.startswith('&'):
        prompt = message.content[1:].strip()
        if prompt:
            await message.channel.send("Thinking... 🤔")
            try:
                response = model.generate_content(prompt)
                await message.channel.send(response.text)
            except Exception as e:
                await message.channel.send(f"Error: {e}")
        else:
            await message.channel.send("Please provide a prompt after `&`")

client.run(TOKEN)
