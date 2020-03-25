#Author - Spirited Wolf
import discord , string , re
from bs4 import BeautifulSoup
import requests

#Discord Token
TOKEN = '<Your token Here>'
client = discord.Client()

#Give information about the particular country
def cases(country_name):
    url = requests.get('https://www.worldometers.info/coronavirus/').content
    unicode_str = url.decode("utf8")
    encoded_str = unicode_str.encode("ascii",'ignore')
    soup = BeautifulSoup(encoded_str, "html.parser")
    lol = {}
    div_container = soup.find('div', class_ = 'main_table_countries_div')
    table = div_container.find('table')
    table_tbody = table.find('tbody')
    rows = table_tbody.find_all('tr')
    for row in rows:
        cols=row.find_all('td')
        cols=[a.text.strip() for a in cols]
        if(country_name == cols[0]):
            return cols
        

#Find the total cases and it's figures
def cases_total():
    url = requests.get('https://www.worldometers.info/coronavirus/').content
    unicode_str = url.decode("utf8")
    encoded_str = unicode_str.encode("ascii",'ignore')
    soup = BeautifulSoup(encoded_str, "html.parser")
    row = soup.find('tr', class_ = 'total_row')
    cols=row.find_all('td')
    cols=[a.text.strip() for a in cols]
    return cols

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    initial_command = message.content
    print(initial_command)
    splitted_command = initial_command.split()
    print(splitted_command)
    command = splitted_command[0]

    if len(splitted_command) > 1:
        argument = splitted_command[1]

    if message.author == client.user:
        return 

    if message.content.startswith("!help"):
        await message.channel.send("Hey I'm a Bot designed to give the current approx figures related to COVID-19 Cases.\nAvailable commands:\n!help\n !cases <country name>\n !cases total")
        
    if message.content.startswith('!cases'):
        if(argument != 'total'):
            a = cases(argument)
            await message.channel.send("Country Name:"+a[0]+"\n"+a[0]+" total Cases:"+a[1]+"\n"+a[0]+" New Cases:"+a[2]+"\n"+a[0]+" total deaths:"+a[3]+"\n"+a[0]+" new deaths:"+a[4]+"\n"+a[0]+" total recovered:"+a[5]+"\n"+a[0]+" active cases:"+a[6]+"\n"+a[0]+" series critical:"+a[7]+"\n Stay safe & stay inside")
        elif(argument == 'total'):
            a = cases_total()
            await message.channel.send(a[0]+" Cases:"+a[1]+"\n"+a[0]+" New Cases:"+a[2]+"\n"+a[0]+" deaths:"+a[3]+"\n"+a[0]+" new deaths:"+a[4]+"\n"+a[0]+" recovered:"+a[5]+"\n"+a[0]+" active cases:"+a[6]+"\n"+a[0]+" series critical:"+a[7]+"\n Please Stay safe & stay inside")
        
    

client.run(TOKEN)
