from os import system
import time
import pyfiglet
import requests
import random

text = pyfiglet.figlet_format("Sherlock 2.0")
print(text)
print("                   Made By NotSlater")
User = input("Username: ")
AdultWeb = input("18+ Website Scans?(y/n) ")

blogger_url = 'https://' + User + '.blogspot.com/'
s = requests.session()
response = s.get(blogger_url)
if response.status_code == 200:
    print('[+] Blogger:', blogger_url)
else:
    print('[-] Blogger:', blogger_url)

chess_url = 'https://chess.com/member/' + User
response = s.get(chess_url)
if response.status_code == 200:
    print('[+] Chess:', chess_url)
else:
    print('[-] Chess:', chess_url)

facebook_url = 'https://facebook.com/' + User
response = s.get(facebook_url)
if response.status_code == 200:
    print('[+] Facebook:', facebook_url)
else:
    print('[-] Facebook:', facebook_url)

fortnite_url = 'https://fortnitetracker.com/profile/all/' + User
response = s.get(fortnite_url)
if response.status_code == 200:
    print('[+] Fortnite:', fortnite_url)
else:
    print('[-] Fortnite:', fortnite_url)

github_url = 'https://github.com/' + User
response = s.get(github_url)
if response.status_code == 200:
    print('[+] Github:', github_url)
else:
    print('[-] Github:', github_url)

gitlab_url = 'https://gitlab.com/' + User
response = s.get(gitlab_url)
if response.status_code == 200:
    print('[+] Gitlab:', gitlab_url)
else:
    print('[-] Gitlab:', gitlab_url)

hackerone_url = 'https://hackerone.com/' + User
response = s.get(hackerone_url)
if response.status_code == 200:
    print('[+] Hackerone:', hackerone_url)
else:
    print('[-] Hackerone:', hackerone_url)

namemc_url = 'https://namemc.com/profile/' + User
s = requests.session()
response = s.get(namemc_url)
if response.status_code == 200:
    print('[+] Namemc:', namemc_url)
else:
    print('[-] Namemc:', namemc_url)

if AdultWeb == "y":    
    onlyfans_url = 'https://onlyfans.com/' + User
    response = s.get(onlyfans_url)
    if response.status_code == 200:
        print('[+] OnlyFans:', onlyfans_url)
    else:
        print('[-] OnlyFans:', onlyfans_url)

pastebin_url = 'https://pastebin.com/u/' + User
response = s.get(pastebin_url)
if response.status_code == 200:
    print('[+] Pastebin:', pastebin_url)
else:
    print('[-] Pastebin:', pastebin_url)
    
patreon_url = 'https://patreon.com/' + User
response = s.get(patreon_url)
if response.status_code == 200:
    print('[+] Patreon:', patreon_url)
else:
    print('[-] Patreon:', patreon_url)
    
pinterest_url = 'https://pinterest.com/' + User
response = s.get(pinterest_url)
if response.status_code == 200:
    print('[+] Pinterest:', pinterest_url)
else:
    print('[-] Pinterest:', pinterest_url)

if AdultWeb == "y":     
    pornhub_url = 'https://pornhub.com/users/' + User
    response = s.get(pornhub_url)
    if response.status_code == 200:
        print('[+] Pornhub:', pornhub_url)
    else:
        print('[-] Pornhub:', pornhub_url)
        
quizlet_url = 'https://quizlet.com/' + User
response = s.get(quizlet_url)
if response.status_code == 200:
    print('[+] Quizlet:', quizlet_url)
else:
    print('[-] Quizlet:', quizlet_url)
    
spotify_url = 'https://open.spotify.com/user/' + User
response = s.get(spotify_url)
if response.status_code == 200:
    print('[+] Spotify:', spotify_url)
elif response.status_code == 404:
    print('[-] Spotify:', spotify_url)
    
steam_url = 'https://steamcommunity.com/id/' + User
response = s.get(steam_url)
if response.status_code == 200:
    print('[+] Steam:', steam_url)
else:
    print('[-] Steam:', steam_url)
    
telegram_url = 'https://t.me/' + User
response = s.get(telegram_url)
if response.status_code == 200:
    print('[+] Telegram:', telegram_url)
else:
    print('[-] Telegram:', telegram_url)
    
tiktok_url = 'https://www.tiktok.com/@' + User
response = s.get(tiktok_url)
if response.status_code == 200:
    print('[+] Tiktok:', tiktok_url)
else:
    print('[-] Tiktok:', tiktok_url)
    
twitch_url = 'https://twitch.tv/' + User
response = s.get(twitch_url)
if response.status_code == 200:
    print('[+] Twitch:', twitch_url)
else:
    print('[-] Twitch:', twitch_url)
    
twitter_url = 'https://mobile.twitter.com/' + User
response = s.get(twitter_url)
if response.status_code == 200:
    print('[+] Twitter:', twitter_url)
else:
    print('[-] Twitter:', twitter_url)
    
virustotal_url = 'https://virustotal.com/ui/users/' + User + '/trusted_users'
response = s.get(virustotal_url)
if response.status_code == 200:
    print('[+] Virustotal:', virustotal_url)
else:
    print('[-] Virustotal:', virustotal_url)
    
youtube_url = 'https://youtube.com/' + User
response = s.get(youtube_url)
if response.status_code == 200:
    print('[+] Youtube:', youtube_url)
else:
    print('[-] Youtube:', youtube_url)

    
