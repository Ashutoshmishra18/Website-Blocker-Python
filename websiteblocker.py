import time
host_path=r"C:\windows\system32\drivers\etc\hosts"
web_siteslist=["www.facebook.com","facebook.com"]
redirect="127.0.0.1"
file=open(host_path,"r+")
content=file.read()
for website in web_siteslist:
    if website in content:
        pass
    else:
        file.write(redirect+" "+website+"\n")
time.sleep(5)