import discord #A python discord api
import pyttsx3
import speech_recognition as sr
from discord.ext import commands
bot = commands.Bot(command_prefix='dis ',intents=discord.Intents.all()) #define command decorator
import googlesearch
import datetime
import sqlite3
import webbrowser
import random
import people_also_ask
conn = sqlite3.connect("xyzee.db")
db = conn.cursor()
coins=10000
from webserver import keep_alive
engine = pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def takecommand():
                r=sr.Recognizer()
                with sr.Microphone() as source:
                                print("Listening")
                                r.pause_threshold=1
                                audio=r.listen(source)
                                print(audio)
                try:
                                print("recognizing")
                                query=r.recognize_google(audio)
                                print("User said : ",query)
                                                
                                                
                except Exception as a:
                                #print(a)
                                print("Say that again pls...")
                                return "None"
                return query

#Function to add the user 
def add_user(username,coins,date):
      db.execute("INSERT INTO MEMERDB(username,coins,date) VALUES(?,?,?)",(username,coins,date))
      return f"{username} added successfully"
#Function to update the change in the coins
def change_coins(username,coins,date):
      db.execute("UPDATE MEMERDB SET  coins = {final_amount} WHERE username = {username}")

print("Opened database successfully\n")
@bot.command(pass_context=True) #define the first command and set prefix to '!'
async def testt(ctx):
    await ctx.send('Hello!!')

@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    if reason=='no reason':
         await ctx.send(f"I don't slap without reason.")
    else:
        await ctx.send(f'{slapped} just got slapped for {reason}.')

@bot.command()
async def showresultsof(ctx,*args): ###
    query=args
    f=people_also_ask.get_answer(query)
    await ctx.send(f)
    

@bot.command()
async def answer(ctx):
    pass #question answer

@bot.command()
async def slaughter(ctx, members: commands.Greedy[discord.Member],reason='lack of friends'):
    slaughtered = ", ".join(x.name for x in members)
    await ctx.send(f'{slaughtered} just got slaughtered due to {reason}')

@bot.command()
async def typesomething(ctx):
    a=""
    while(a!="over and out"):
        a=takecommand()
        if("over and out" not in a):
            await ctx.reply(f"{ctx.author} \n"+a)
        else:
              await ctx.reply(f"...")
              break
    
@bot.command()
async def open(ctx,*args):
    try:
        if args=="twitter".lower() :
            webbrowser.open(f"https://twitter.com/elonmusk")
            await ctx.send("Opened",webbrowser.open(f"https://twitter.com/elonmusk"))
        elif "instagram".lower():
            webbrowser.open(f"https://www.instagram.com/tayl orswift")
            await ctx.send("Opened")
        else:
              await ctx.send(f"{args} not available")
    except:
        await ctx.send(f"{args}not found")

@bot.command()
async def tellme(ctx,*arg):
    try:
        from Chat_GPT import tell_me
        await ctx.send(f"{tell_me(arg)}")
    except:
        await ctx.send("Sorry but there might be some technical issues kindly wait for that after")
        print("Message failed")
#keep_alive()

#coins Game in this bot
@bot.command()
async def game(ctx):
    print(f"\n{ctx.author} just messaged")
    username=ctx.author
    coins=10000
    #db.execute("Select username * from MEMERDB")
    #f=db.fetchall()
    #if(username not in f):
     #     coins=10000
     #     add_user(username,coins,date=datetime.date.today())
    #else:
          #db.execute(f"Select coins from MEMERDB where username={username}")
          #f=db.fetchall()
          #coins=f
          #pass
    hint = random.randint(1, 100)
    number = random.randint(1, 100)
    coins_to_add = random.randint(1, 10000)
    tries = 1
    await ctx.send(f"your hint is {hint}. Type 'high' if the number generated is high and type 'low' if the number is lower. Type 'Jackpot' if the number is equal.")
    while True:
        guess_message = await bot.wait_for('message')
        if guess_message.author.id == ctx.author.id:
            if tries == 1:
                if guess_message.content.lower() == "high" and number > hint:
                    coins = coins + coins_to_add
                    await ctx.send(f"The guess was correct😀. Your Amount has been raised to {coins}")
                    #db.execute(f"UPDATE MEMERDB set coins={coins} where username={username}")
                    tries = 0
                elif guess_message.content.lower() == "low" and number < hint:
                    coins = coins + coins_to_add
                    await ctx.send(f"The guess was correct😀. Your Amount has raised to {coins}")
                    tries = 0
                elif guess_message.content.lower()=="jackpot":
                    coins = coins + coins_to_add
                    await ctx.send(f"The guess was correct😀. Your Amount has raised to {coins}")
                    tries = 0
                else:
                    coins=coins-coins_to_add
                    await ctx.send(f"incorrect😔, the number was {number}. Your Amount has been lowered to {coins}")
                    tries = 0
            else:
                return      
bot.run("MTAwNTE4NTY4ODE2NzI2ODQ3Mw.GUjO6r.pvnktGMH29b5iVHRN75KdKFkEmQQxEgx8kiLaY") #run the client using using my bot's token