import discord
import asyncio

client = discord.Client()
token = "TOKEN HERE"
prefix = "$"
command = "leave"
leaveMessage = "MESSAGE HERE"

@client.event
async def on_ready():
    print("token verified type $leave in any dm and itll leave all your gcs")

@client.event
async def on_message(message):
    if message.author == client.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == prefix + command:
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id:
                        count = count + 1
                        await channel.send(leaveMessage)
                        await channel.leave()
                        print("Left a group: " + str(channel.id)) 
            await message.channel.send("you left [" + str(count) + "] group chats")
            await client.close()

client.run(token, bot=False)
input("Press enter to exit")