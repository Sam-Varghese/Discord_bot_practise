import discord
from discord.ext import commands
import os
import datetime
from datetime import datetime
import webbrowser

client=discord.Client()

eng_bad_words=['fuck','nude', 'shit', 'cock', 'titties', 'boner', 'muff', 'pussy', 'asshole','cunt', 'ass', 'cockfoam', 'nigger']
eng_depressing_words=['sad','depressed','feeling bad','disappointed']

@client.event
async def on_ready():

    print('Jarvis activated')

@client.event
async def on_message(message):

    if message.author==client.user:

        return None

    if message.content.startswith('Hey jarvis'):

        await message.channel.send('Jarvis activated sir , please command what should I do for you.')
        
    if message.content.startswith('Jarvis introduce yourself'):
        
        await message.channel.send('Namaste everyone , myself Jarvis , a bot made by Master Sam Varghese in order \
        to keep an eye on all the conversations of this discord group.')

    if message.content.startswith('Jarvis time'):

        msg='Sir today\'s date is '+str(datetime.now().strftime('%d-%m-%Y'))+'\n And presently its '+str(datetime.now().time())

        await message.channel.send(msg)

    if message.content.startswith('Jarvis open google'):

        webbrowser.open('https://www.google.com/')
        await message.channel.send('Opening Google sir....')
    
    if message.content.startswith('Jarvis open youtube'):
        
        webbrowser.open('https://www.youtube.com/')
        await message.channel.send('Opening YouTube sir...')
        
    if any(word in message.content for word in eng_bad_words):
        
        await message.channel.send('Sorry to interrupt in between but an abusing english word  has\
 been detected. Please mind the language in order to maintain peace and harmony')
        
    if any(word in message.content for word in eng_depressing_words):
        
        await message.channel.send('Sorry to interrupt in between but I should say that we should not let ourselves \
get discouraged so much , just believe in Lord your God , I know he is there in your boat ,and if he is there in your \
boat then dont fear the storms ,they cant even touch you because Lord wont let this happen sir.')
        

client.run('ODIyODMwNzIxMDYzOTc2OTcw.YFX-0w.Utb9jqsAwfoJVgCmF5zoLHYeeyU')