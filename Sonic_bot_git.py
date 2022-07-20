import discord

client = discord.Client()


#now_version="2.1"
    
now_version="31th.tk"


@client.event
async def on_ready():
    
    
    
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name="Green Hill zone"))
    print("안녕! 난 소닉, 소닉 더 헤지혹이야!"))
    
    
    
    """Game: Sonic the Hedgehog이라고 설정"""
    
        
        
@client.event

async def on_message(message):
    if message.content == '소닉':
        await message.channel.send("나 불렀어?")
    
    

    
    if message.content == '소닉 버전 확인':
        embed = discord.Embed(title="Sonic Discord Bot Version", description="Now Version is" + now_version, color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="Harry_STH") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
    

        #출처: https://code-200.tistory.com/62 [CODE 200]
        
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
