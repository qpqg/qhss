from requests import request
from threading import Thread
from random import randint as magic
from os import system as hapus
#========== [ SETTING DISINI ] ==================
method = "GET"
cari_server = ["AkamaiGHost"] #Cari ex: ["AkamaiGHost", "gws"]
save_file = "/storage/emulated/0/FreeHostScan/"
waktu = 5 #putuskan koneksi setelah 5 detik
#================================================

garis = "="*20
def banner():
    print garis
    print "Simple Script Cari Server Host"
    print "Coded by: Qiuby Zhukhi"
    
def ok(isi):    
    return "\033[32m{}\033[00m".format(isi)

def save_files(isi, f):
    file_name = f+"checkServer1.txt"
    with open(file_name, "a+") as writer:
        writer.write(isi)
        writer.close()
        
def open_host(f):
    list_host = []
    with open(f) as writer:
       for i in writer.readlines():
           i = i.replace("\n","").replace("\r\n","")
           if i.startswith(":"):
               proxy, port = i.split(":");
               i = proxy
           list_host.append(i)
    return list_host
    
list_server = []
def checker(h, m):
    try:
        get_resp = request(m, "http://"+h, timeout=waktu, verify=True, allow_redirects = True)
        headers = get_resp.headers["Server"]
        if headers in cari_server:
            print "Host: {}\nServer: {}\nStatus Code: {}\r\n".format(h, ok(headers), get_resp.status_code)
            list_server.append(h)
        else:
            print "Host: {}\nServer: {}\nStatus Code: {}\r\n".format(h, headers, get_resp.status_code)
    except Exception as e:
        pass

thread_list = []
def watasi_wa_wibu_desu():
    while 1:
        banner()
        try:
            files = raw_input("Full path host: ")
            op = open_host(files)
            break
        except Exception as e:
            print e
            continue
    for _ in op:
        t = Thread(target=checker, args=(_, method))
        t.daemon = True
        t.start()
        thread_list.append(t)
    join_kopi = [i.join() for i in thread_list]
    result()
      
def single_scan():
    cek_host = raw_input("Host: http://")
    print ("\n")
    checker(cek_host, method)
    result()
    
def result():
    global list_server
    if list_server != []:
        print "==== [Server Ditumukan] ===="
        for i in list_server:
            print ok(i)
            save_files(i+"\r\n", save_file)
        print "Save di: "+save_file+"checkServer.txt"
        print "Membersihkan List"
    else:
        print "Wkwkwkwkw Zonk :v "
    list_server = []

def options():
    while 1:
        banner()
        a = ["0. Single Scan","1. List Scan"]
        print garis
        print "\n".join(_ for _ in a)
        print garis
        try:
            num_ops = int(raw_input("Pilihan: > "))
            if num_ops <= len(a):
                print "Pilihan Anda: " + a[num_ops]
                if num_ops == 0:
                    single_scan()
                elif num_ops == 1:
                    watasi_wa_wibu_desu()
            else:
                stat = ["ngelawak gan?",
                "Yaelah milih aja susah yah?",
                "Pilihannya kan ada {} kenapa milih {} ?".format(str(len(a)), num_ops)
                ]
                print stat[magic(0,2)]
                continue
        except Exception as e:
            print e
            continue
            
if __name__ == "__main__":
    hapus("clear")
    options()


