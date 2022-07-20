import discord

client = discord.Client()



@client.event
async def on_ready():
    
    
    
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name="Green Hill zone"))
    print("안녕! 난 소닉, 소닉 더 헤지혹이야!"))
    
    
    
    """Game: Sonic the Hedgehog이라고 설정"""
    
        
        
@client.event

async def on_message(message):
    if message.content == '소닉':
        await message.channel.send("나 불렀어?")
    
    
    

        
    if message.content.startswith("소닉 음챗 컴온"):
       await message.author.voice.channel.connect()
       await message.channel.send("알겠어!")
       
    
    if message.content.startswith("소닉 ㅃ"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice=vc
        
        await voice.disconnect()
        await message.channel.send("알겠어!")
        
        

        
        
   




    
    
    
    

client.run("Your Token")
