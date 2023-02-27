import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

formula1com = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html')
discordwebhock = "" # put your discord webhook here

soup = BeautifulSoup(formula1com.text, 'lxml')
pass1 = soup.find('tbody')
pass2s = pass1.find_all('tr')
#print(pass2s)

discord_pkt = ""

for pass2 in pass2s:

    driver_pos1 = pass2.find('td', class_ = 'dark')
    driver_driver1 = pass2.find('span', class_ = 'hide-for-mobile')
    driver_car1 = pass2.find('a', class_ = 'grey semi-bold uppercase ArchiveLink')
    driver_PTS1 = pass2.find('td', class_ = 'dark bold')

    driver_pos1 = pass2.find('td', class_ = 'dark')
    driver_driver1 = pass2.find('span', class_ = 'hide-for-mobile')
    driver_car1 = pass2.find('a', class_ = 'grey semi-bold uppercase ArchiveLink')
    driver_PTS1 = pass2.find('td', class_ = 'dark bold')

    driver_pos2 = driver_pos1.get_text()
    driver_driver2 = driver_driver1.get_text()
    driver_car2 = driver_car1.get_text()
    driver_PTS2 = driver_PTS1.get_text()

    text_string = driver_pos2 + ". " + driver_driver2 + " | " + driver_car2 + " (" + driver_PTS2 + ")"

    discord_pkt += text_string
    discord_pkt += "\n"

print(discord_pkt)

webhook = DiscordWebhook(url=discordwebhock, content=discord_pkt)
webhook.execute()
