import os
import discord
from discord.ext import commands
from flask import Flask

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

app = Flask(__name__)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    import threading

    def run_flask():
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)

    threading.Thread(target=run_flask).start()
    bot.run(os.environ["DISCORD_TOKEN"])
