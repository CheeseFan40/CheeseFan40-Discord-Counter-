import discord
import random

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)


    async def on_message(self, message):
        counter = 0
        
        list = ["Your number is:","Number:","Your next number is:"]
        Random = random.choice(list)
        
        
        
        if message.author == self.user:
            return
        
        if message.content == '$Count' or message.content == '$count':
            try:
                f = open("counter.txt", "r")
                counter = int(f.readline())
            except:
                f = open("counter.txt", "a")
                f.write(str(0))
            counter+=1
            f = open("counter.txt","w")
            f.write(str(counter))
                         
            
            await message.channel.send(Random + " " + str(counter))

client = MyClient()
client.run('enter token here')
