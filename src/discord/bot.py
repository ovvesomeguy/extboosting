# This file contain a representaion of role changer bot
# And he must be runned out of main vk bot


import discord
import requests

discord_key = 'NjUzMjczOTM1NDUzODgwMzMz.XfY7lw.kSGjH6p-u4ejNZ9k0ygysOh5v44'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles , name='Без Очереди')
    await member.add_roles(role)


@client.event
async def on_message(message):
    pass

# client.run(discord_key)