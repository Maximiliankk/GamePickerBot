# client_id=1220886460354396161
# permissions=534723819584
# https://discord.com/api/oauth2/authorize?client_id=1220886460354396161&permissions=534723819584&scope=bot%20applications.commands

import discord
from discord.ext import commands
import random

# Create a bot instance
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# A list of games to pick from
# games_list = ['Hunt Showdown', 'Helldivers', 'PUBG']

# read the games from the file
with open("default_games_list.txt", "r") as file:
    games_list = file.read().splitlines()

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Command to pick a game from the default list
@bot.command(name='pickgame', help='Picks a random game for the session')
async def pick_game(ctx):
    print('picking a game!')
    game = random.choice(games_list)
    response = f"Today's game is: {game}\nOptions were: \n" + str(games_list)
    await ctx.send(response)

# read the token from the file
with open("tokenkey.txt", "r") as file:
    tokenkey = file.read()

# Run the bot with your token
bot.run(tokenkey)
