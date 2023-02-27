import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

formula1com_drivers = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html')
formula1com_races = requests.get('https://www.formula1.com/en/results.html/2022/races.html')
base_url = "https://www.formula1.com"
discordwebhock = "" # put your discord webhhock here

soup = BeautifulSoup(formula1com_drivers.text, 'lxml')
pass1 = soup.find('tbody')
pass2s = pass1.find_all('tr')

discord_pkt = ""

discord_pkt += "--------------------"
discord_pkt += "\n"
discord_pkt += "Drivers:"
discord_pkt += "\n"

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

ra_soup = BeautifulSoup(formula1com_races.text, 'lxml')
ra_pass1 = ra_soup.find('tbody')
ra_pass2 = ra_pass1.find('tr')
ra_pass3 = ra_pass2.find('a', class_ = 'dark bold ArchiveLink')
ra_pass4 = ra_pass3.get('href')
ra_query_url = base_url + ra_pass4

formula1com_race = requests.get(ra_query_url)
ra1_soup = BeautifulSoup(formula1com_race.text, 'lxml')
ra1_pass1 = ra1_soup.find('tbody')
ra1_pass2s = ra1_pass1.find_all('tr')

discord_pkt += "--------------------"
discord_pkt += "\n"
discord_pkt += "Latest Race: "
discord_pkt += ra_query_url
discord_pkt += "\n"

for ra1_pass2 in ra1_pass2s:

    ra1_race_POS1 = ra1_pass2.find('td', class_ = 'dark')
    ra1_race_DRIVER1 = ra1_pass2.find('span', class_ = 'hide-for-mobile')

    ra1_race_POS2 = ra1_race_POS1.get_text()
    ra1_race_DRIVER2 = ra1_race_DRIVER1.get_text()

    text_string = "P" + ra1_race_POS2 + " " + ra1_race_DRIVER2

    discord_pkt += text_string
    discord_pkt += "\n"

print(discord_pkt)
webhook = DiscordWebhook(url=discordwebhock, content=discord_pkt)
webhook.execute()
