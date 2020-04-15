import urllib.request, json, time,utils
def now(msg):
    print("[*] ctftime.now request")
    results=[]
    with urllib.request.urlopen(urllib.request.Request(f"https://ctftime.org/api/v1/events/?limit=100&start={int(time.time())-259200}&finish={int(time.time())+259200}",None,headers={'User-Agent':'Mozilla/5.0'})) as url:
        ctfs = json.loads(url.read().decode())
        for ctf in ctfs:
            if utils.time_to_secs(ctf["start"]) <= int(time.time()) and  int(time.time()) <= utils.time_to_secs(ctf["finish"]):
                results.append(utils.format_json_to_ctf(ctf))
                print("[*] Found ctf")
    if results == []:
        results.append("=================================================\nNo CTF happening right now")
    return results

def next_week(msg):
    results=[]
    print("[*] ctftime.next_week request")
    with urllib.request.urlopen(urllib.request.Request(f"https://ctftime.org/api/v1/events/?limit=100&start={int(time.time())+86400}&finish={int(time.time())+259200}",None,headers={'User-Agent':'Mozilla/5.0'})) as url:
        ctfs = json.loads(url.read().decode())
        for ctf in ctfs:
            results.append(utils.format_json_to_ctf(ctf))
            print(" *  Found ctf")
    if results == []:
        results.append("=================================================\nNo CTF scheduled for next week")
    return results