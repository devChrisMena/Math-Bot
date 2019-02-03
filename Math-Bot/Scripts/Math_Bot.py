import discord
from behavior.math_basis import *
import asyncio
# Load token key
token = open('Scripts/token.txt', 'r').read()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content} ')
    if message.content.startswith('!integrate') or message.content.startswith('!diff'):
        call = calculus(message.content)
        command, func, a, to, b = message.content.split()
        if message.content.startswith('!integrate'):
            if a != 'None':
                data, ind_f = call.message_decoder()
                await client.send_message(message.channel, f"```∫{func}dx = {ind_f} from {a} to {b} = {data}```")
                await client.send_file(message.channel,'integration.png')
            else:
                data = call.message_decoder()
                await client.send_message(message.channel, f"```∫{func}dx = {data}```")

        elif message.content.startswith('!diff'):
            data = call.message_decoder()
            await client.send_message(message.channel, f"```d/dx {func} = {data}```")
    elif message.content.startswith('!help'):
        for help in expressions.keys():
            await client.send_message(message.channel, f"``` {help}  {expressions[help]}```")
    elif message.content.startswith('!solve'):
        call = algebra(message.content)
        data = call.solver()
        await client.send_message(message.channel, f"```Answer: {data}```")
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
client.run(token)