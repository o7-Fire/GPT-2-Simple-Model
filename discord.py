import discord
import main
client = discord.Client()
import asyncio
def submitTask(task):
  return asyncio.get_running_loop().create_task(task)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if(message.author.bot):
    return
  if(message.channel.name.startswith('quote')):
    submitTask(message.channel.send(main.generate(message.conntent)))
    
   

client.run('your token here')
