import time
def time_to_secs(ctf_time):
    return  time.mktime(time.strptime(ctf_time, "%Y-%m-%dT%H:%M:%S%z"))

def format_json_to_ctf(ctf):
    result = f"""Name: {ctf["title"] if ctf["title"] != '' else "Name not found"}\nStart: {ctf["start"]}\nEnd: {ctf["finish"]}\nDuration: {int(ctf["duration"]["days"])*24+int(ctf["duration"]["hours"])} hours\nUrl: {ctf["url"]}"""
    upwardpadding = ''.join(['=' for i in range(max([len(a) for a in result.split('\n')]))])+'\n'
    result = upwardpadding + result
    return result