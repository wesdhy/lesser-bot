
import discord
from discord.ext import commands
from datetime import datetime, timedelta
from datetime import time
import asyncio
import time
from random import *





client = discord.Client()

times = datetime(2020, 2, 29, 0 ,0 , 0)# 상병
timeb = datetime(2020, 9, 11, 0 ,0 , 0)# 병장
time1 = datetime(2021, 2, 13 , 7 , 0, 0)# 전역

time00 = datetime(2018, 9, 15, 0, 0, 0)# 개설 2018, 9, 16





@client.event
async def on_ready():
    print("hi wesdhy")
    print(client.user.id)
    print("ready")
    game = discord.Game("야스")
    await client.change_presence(status=discord.Status.online, activity=game)
   



@client.event
async def on_message(message):
    time21 = datetime.now()
    print(message.author , message.content ,"                 " , time21 )
    i = randrange(9)
    x = randrange(99)

    if message.content.startswith("어림"):
    
         
         await message.channel.send("하지만 어림도 없지")

    if message.content.startswith("어때?"):
    
         
         await message.channel.send( str(x) + '%')

         

    
    
    


    if message.content.startswith("!액션빔"):
        embed = discord.Embed(
         title='2019 입대 1일 전',
         description='레서 ㅠㅠ',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682144379997126656/VRChat_1920x1080_2019-06-09_14-06-08.692.png")
        await message.channel.send(embed=embed)

   
    

    
    
    if message.content.startswith("!오토"):
        embed = discord.Embed(
         title='Auto_VRC',
         description='로리폴리스 타격대',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://steamuserimages-a.akamaihd.net/ugc/990134371123407502/6E7F57FAB3ED9291DC26D3D94D86F4C5AB353715/")
        await message.channel.send(embed=embed)

    if message.content.startswith("!카이"):
        embed = discord.Embed(
         title='2018 스타킹',
         description='비율 좋음',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682144411270119424/20181023_202740.jpg")
        await message.channel.send(embed=embed)

    



   




 

    if message.content.startswith("!라무네단"):
        embed = discord.Embed(
         title='공사장 라무네',
         description='안전 제일',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682297350604980282/VRChat_1920x1080_2018-09-16_00-37-36.919.png")
        await message.channel.send(embed=embed)
   





   
    
    if message.content.startswith("왕왕") and i==1:
        embed = discord.Embed(
         title='2019 레서 군번줄',
         description='a형',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682149075042304001/20190712_120447.jpg")
        await message.channel.send(embed=embed)

  

    elif message.content.startswith("왕왕") and i<=5:
        embed = discord.Embed(
         title='레서 팔',
         description='무료봉사 감사합니다.!',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/689371627716345874/IMG_0432.JPG")
        await message.channel.send(embed=embed)
    elif message.content.startswith("왕왕") and i==6:
        embed = discord.Embed(
         title='2019 떼껄룩',
         description='귀여움',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682148056463966235/VRChat_1920x1080_2019-02-10_14-19-48.625.png")
        await message.channel.send(embed=embed)
    elif message.content.startswith("왕왕") and i==7:
        embed = discord.Embed(
         title='액션빔',
         description='사진 지원:웨주디 방',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/689365654960078889/IMG_0764.jpg")
        await message.channel.send(embed=embed)

    elif message.content.startswith("왕왕") and i<10:
        embed = discord.Embed(
         title='그방',
         description='아기잇자기잇',
         colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/689371626768171024/IMG_0447.JPG")
        await message.channel.send(embed=embed)

    
    

    if message.content.startswith("홀리쉣")  :
        
        
     await message.channel.send("<:emoji96a:669494055193018368>")
       
        
    
    if message.content.startswith("레서야 ") or message.content.startswith("맞지?"):
        
        if message.author.id==253901897537290242 and i==8:
        
         await message.channel.send("자아성찰 중 인거야?")
         await message.channel.send("<:emoji96a:669494055193018368>")
        else:

         if i>6:
          await message.channel.send("응")
         elif i==1:
          await message.channel.send("예\n아니요\n예\n아니요\n예")

         elif(i==2):
          embed = discord.Embed(
          title='또 속냐?',
          description='또 속냐고',
          colour=discord.Colour.green()
          )
          embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682273583610724422/3432432.PNG")
          
          await message.channel.send(embed=embed)
         elif(i==3):
          await message.channel.send("%")
         



         else:
          await message.channel.send("아니야")

    elif message.content.startswith("레서야"):
        await message.channel.send("왜?")

   
    if message.content.startswith("안녕"):
         
         
         
         if (i==1):
          await message.channel.send("안넝하세요!\n젼나 좋은 하루되세요 !!!!!!!!")
          
         
         elif(i==2):
          await message.channel.send("감사합니다\n존나 진짜 좋은 하루되세요 !!!!!!!!")
          
          
         elif(i==3):
          await message.channel.send("안넝하세요!!!!!\n조까세요!!!!!!")
          
          
         elif(i==4):
          await message.channel.send("그만해")

         elif(i==5):
          await message.channel.send("뚱성!")

         elif(i==6):
          await message.channel.send("개조아")

         elif(i==7):
          await message.channel.send("우헤헤헤\n조까세요!!!!!!")

         
         
         else:
          await message.channel.send("안농안농")
          

    
    if message.content.startswith("섹스"):
         
         
         
         if (i==1):
          await message.channel.send("봉지")
          
         
         elif(i<=2):
          await message.channel.send("쥬지")

         elif(i<=6):
          await message.channel.send("봉지")
          

         
         else:
          await message.channel.send("인생절반손해봤어")
    
       
 
    if message.content.startswith("!짭레서"):
        await message.channel.send("@Lesser")
        await message.channel.send("이 친구가 짭이야")
       

        embed = discord.Embed(
             title='이름=짭레서',
             description='직업=군인',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/724087412732723231/56546456.PNG")
        await message.channel.send(embed=embed)

        
    
             
    if message.content.startswith("기타"):
        
      
       

        embed = discord.Embed(
             title='딩가',
             description='딩가',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/636533574618578965/qwerqwer_4.gif")
        await message.channel.send(embed=embed)


    if message.content.startswith("!춤"):
      
       

        embed = discord.Embed(
             title='뇌절 춤',
             description='야무지게 흔듬 ㄹㅇ',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/724086236557475850/Honeycam_2020-06-13_22-17-55.gif")
        await message.channel.send(embed=embed)

    if message.content.startswith("!넘버원"):
      
       

        embed = discord.Embed(
             title='너구리',
             description='혹독한 경쟁 세카이에서 도태되지않고 살아남음',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/719459438662123591/VRChat_1920x1080_2020-06-07_21-32-53.314.png")
        await message.channel.send(embed=embed)


    if message.content.startswith("!로피니아"):
      
       

        embed = discord.Embed(
             title='로피니아',
             description='늑머버림',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/722157208896274442/VRChat_1920x1080_2020-06-15_23-05-24.313.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("!수인"):
       
       

        embed = discord.Embed(
             title='꾸닝',
             description='수인',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/705781668161650688/EW7iNy0UMAE0X0_.png")
        await message.channel.send(embed=embed)





    if message.content.startswith("!뱁새"):
       
       

        embed = discord.Embed(
             title='외모지상주의',
             description='패배',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/700690818087911474/VRChat_1920x1080_2020-04-17_21-54-22.569.png")
        await message.channel.send(embed=embed)


    if message.content.startswith("!미코밭"):
       
       

        embed = discord.Embed(
             title='내가 왜...',
             description='무슨 잘못을 했다고',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/702537562996080730/VRChat_1920x1080_2020-04-22_20-59-10.1841.png")
        await message.channel.send(embed=embed)



    if message.content.startswith("!ㅗ")and i<5:
       
       

        embed = discord.Embed(
             title='욕',
             description='욕은 나쁨미다',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/724086546495701053/VRChat_1920x1080_2020-06-11_01-33-17.896.png")
        await message.channel.send(embed=embed)

    elif message.content.startswith("!ㅗ") and i<10:
       
       

        embed = discord.Embed(
             title='욕',
             description='욕은 나쁨미다',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/724086546495701053/VRChat_1920x1080_2020-06-11_01-33-17.896.png")
        await message.channel.send(embed=embed)
    

    if message.content.startswith("@clear"):
         time.sleep(1)
         await message.channel.send("```최근 메시지 10개를 삭제함.```")
         
    if message.content.startswith("!명언"):
         
         
        embed = discord.Embed(
             title='너구리',
             description='브쳇은 너구리처럼 즐겨야한다',
             colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/719459438662123591/VRChat_1920x1080_2020-06-07_21-32-53.314.png")
        await message.channel.send(embed=embed)
    
    
    if message.content.startswith("@super113355"):
        
         time.sleep(1)
        
         await message.channel.send("```최근 메시지 99개를 삭제함. 봇 서버에 삭제로그를 남겼습니다!")
    
        
    if message.content.startswith("!삼성") and i<5:
  
        embed = discord.Embed(
            title='외주디는 삼엽충임미다',
            description='머리 깨져도 삼성 노트북이야',
            colour=discord.Colour.dark_gold()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682282497098514485/VRChat_1920x1080_2019-04-20_22-02-27.153.png")
        await message.channel.send(embed=embed)
    
    elif message.content.startswith("!삼성") and i<10:
        embed = discord.Embed(
            title='갤럭시북',
            description='삼성 조아용 훠훠훠',
            colour=discord.Colour.dark_gold()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/689372856030593054/IMG_0464.JPG")
        await message.channel.send(embed=embed)




    if message.content.startswith("!띵언") and i<3:
  
        embed = discord.Embed(
            title='너구리',
            description='도태되면 죽는거다',
            colour=discord.Colour.dark_gold()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/537080589023707138/686159496963555364/20200308_193242.jpg")
        await message.channel.send(embed=embed)
    elif message.content.startswith("!띵언") and i<5:

        embed = discord.Embed(
            title='고추',
            description='고추',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/689382039610327040/5656.png")
        await message.channel.send(embed=embed)
    elif message.content.startswith("!띵언") and i<7:

        embed = discord.Embed(
            title='로피니아',
            description='구에엑',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/682150071764385842/20181017_183147.jpg")
        await message.channel.send(embed=embed)
    elif message.content.startswith("!띵언") and i<10:

        embed = discord.Embed(
            title='그의 다짐',
            description='어딘가로',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/573672972301238272/689381172413071380/lesser1.png")
        await message.channel.send(embed=embed)
  

    if message.content.startswith("!재정신")  :
  
        embed = discord.Embed(
            title='이름=레서',
            description='직업=약쟁이',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/678278912517865492/VRChat_1920x1080_2020-02-15_22-12-30.841.png")
        await message.channel.send(embed=embed)
    

    if message.content.startswith("!공사장")  :
  
        embed = discord.Embed(
            title='이름=레서',
            description='직업=건설 자원 봉사자',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/678152046347681842/VRChat_1920x1080_2018-09-15_19-20-33.985.png")
        await message.channel.send(embed=embed)

    
        
    

    if message.content.startswith("!개설일"):
        time2 = datetime.now()

        embed = discord.Embed(
            title='자칭신사 변태들',
            description='2018.09.16. 개설  '+ str((time00-time2).days)+"일 되는날",
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/635104475551498260/635106251792973845/VRChat_1920x1080_2018-12-25_00-40-11.209.png")
        await message.channel.send(embed=embed)


    if message.content.startswith("!명령어"):
        time2 = datetime.now()

        embed = discord.Embed(
            title='명령',
            description='레서야 명령어로 폭언자제요망.',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/689362953270853782/724100965535580273/334.PNG")
        await message.channel.send(embed=embed)


    if message.content.startswith("!머리"):
        time2 = datetime.now()

        embed = discord.Embed(
            title='박어',
            description='힝...',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/683632408838537252/VRChat_1920x1080_2020-03-01_20-09-46.360.png")
        await message.channel.send(embed=embed)
        
        
    if message.content.startswith("!기타"):
        time2 = datetime.now()

        embed = discord.Embed(
            title='딩가',
            description='딩가',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/636533574618578965/qwerqwer_4.gif")
        await message.channel.send(embed=embed)




    if message.content.startswith("!완"):
        time2 = datetime.now()

        embed = discord.Embed(
            title='타이',
            description='완',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/522132608134414347/549464375308845068/VRChat_1920x1080_2019-02-19_16-28-29.645.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("!탑"):
        time2 = datetime.now()

        embed = discord.Embed(
            title='탑',
            description='인간탑',
            colour=discord.Colour.green()
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/681485659806236672/VRChat_1920x1080_2020-02-18_21-47-08.575.png")
        await message.channel.send(embed=embed)


 
        
    if message.content.startswith("!레서"):



        time2 = datetime.now()
        if time1 < time2:
            embed = discord.Embed(
            title='레서의 판타스틱 군생활 끝!',
            description='전역을 환영합니다 !',
            colour=discord.Colour.green()
            )

            embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/683632412193718272/unknown.png")
        
       
            

        elif  time2 < time1:
            
            
            tomorrowAfterTemp = ('전역까지'+str((time1-time2))+' 남음')

       
            embed = discord.Embed(
                title='레서의 판타스틱 군생활',
                description='',
                colour=discord.Colour.green()
            )

            embed.set_image(url = "https://cdn.discordapp.com/attachments/556308043231395840/683632412193718272/unknown.png")
        
       
            embed.add_field(name='입대일 2021.03.10(월) 전역일 2024.02.12', value=tomorrowAfterTemp, inline=False)
        
        
        
        await message.channel.send(embed=embed)
        
        
      

        
        #if time2 < times:
        #    await message.channel.send('상병진급 '+str((times-time2).days) + '일 남음')
        #elif  time2 < timeb:
        #   await message.channel.send('병장진급 '+str((timeb-time2).days) + '일 남음')
       
         


       

client.run('NjgwNDM1NTYxOTE1NDgyMzI0.Xk_3gA.JnQ2VEwkQdZmh4Gb4rY2PwTJ8Do')


