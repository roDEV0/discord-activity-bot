import discord
from discord.abc import GuildChannel

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

gameCheck = True

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_presence_update(before, after):

    for activity in after.activities:
        if activity.type == discord.ActivityType.playing:
            game_name = activity.name
            print(f"{before.name} is now playing {game_name}")

            system_channel = client.guilds[0].system_channel
            if system_channel is not None:
                await system_channel.send(f"{before.name} is now playing {game_name}")
            break

@client.event
async def on_message(message):
  global gameCheck
  if message.author == client.user:
      return

  if message.content.startswith('$toggle'):
    gameCheck = False if gameCheck == True else True
    await message.channel.send('Game check toggled to ' + str(gameCheck))

client.run('TOKEN')
