import requests as req
from colorama import Fore, init
from multiprocessing.dummy import Pool as ThreadPool
import re
import os
import pyfiglet

init(autoreset=True)

cyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
red = Fore.LIGHTRED_EX

pattern_sukses = 0
pattern_failed = 0
pattern_unknown = 0

try:
    open("result.txt", "a")
except:
    pass

def __banner__(s):
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format(s, font="slant", justify="center")
    print(f"{red}{my_banner}")
    print(f"{red}\t\t\t[ {white}Created By X-MrG3P5 {red}]\n")
    print(f"{red}( {white}Format: {yellow}username:hash {red})")

def decrypt(x):
    global pattern_unknown, pattern_failed, pattern_sukses
    try:
        if "email protected" in x:
            pass
        else:
            md5 = x.split(":")[1].strip()
            email = x.split(":")[0]
            print(f"{red}[{white}•{red}]{white} Decrypting -> {yellow}{md5}")
            r = req.get(f"https://www.cellphonetrackers.org/tool/mac.php?md5={md5}")
            decrypted = re.findall("red>(.*?)</font>", r.text)[0]
            
            validHash = re.finditer(r'(?=(\b[A-Fa-f0-9]{32}\b))', decrypted)
            result = [match.group(1) for match in validHash]
            
            if result:
                r2 = req.get(f"https://www.cellphonetrackers.org/tool/mac.php?md5={decrypted}")
                decrypted2 = re.findall("red>(.*?)</font>", r2.text)[0]
                
                if "1020" in decrypted2:
                    pattern_unknown += 1
                    pass
                else:
                    print(f"{red}[{white}•{red}] {white}Found ; {green}{email}|{decrypted2}")
                    chunks = email + "|" + decrypted2 + "\n"
                    
                    if chunks in open("result.txt", "r").read():
                        pass
                    else:
                        open("result.txt", "a").write(chunks)
                        pattern_sukses += 1
            else:
                if "1020" in decrypted:
                    pattern_unknown += 1
                    pass
                else:
                    print(f"{red}[{white}•{red}] {white}Found : {green}{email}|{decrypted}")
                    chunk = email + "|" + decrypted + "\n"
             
                    if chunk in open("result.txt", "r").read():
                        pass
                    else:
                        open("result.txt", "a").write(chunk)
                        pattern_sukses += 1
    except:
        pattern_failed += 1
        pass


if __name__=="__main__":
    __banner__("Md5-Decryptor")
    input_list = open(input(f"{red}[{white}?{red}] {white}Input List : "), "r").readlines()
    input_thread = input(f"{red}[{white}?{red}] {white}Thread : ")
    pool = ThreadPool(int(input_thread))
    pool.map(decrypt, input_list)
    pool.close()
    pool.join()
    print(f"{white}----------------------------")
    print(f" \t{white}Sukses: {green}{pattern_sukses}")
    print(f" \t{white}Failed: {red}{pattern_failed}")
    print(f" \t{white}Unknown: {yellow}{pattern_unknown}")
    print(f"{white}----------------------------")
    print(f"Saved file into {green}result.txt")
