import discord

client = discord.Client()



@client.event
async def on_ready():
    
    
    
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name="Green Hill Zone"))

"""디스코드 봇 상태 설정하기"""

@client.event

async def on_message(message):
    """메세지 입력 반응 테스트"""
    if message.content == '소닉':
        await message.channel.send("나 불렀어?")
    
    
    

    """음성 채널 참여 테스트"""    
    if message.content.startswith("voice channal - in"):
       await message.author.voice.channel.connect()
       await message.channel.send("Ok!")
       
    """음성 채널 아웃 """
    if message.content.startswith("voice channal - out"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice=vc
        
        await voice.disconnect()
        await message.channel.send("..done!")
        
        

        
        
   




    
    
    
    

client.run("Your Token")
