cyphertext = 'XLIWP MRKWE RHEVV SAWSJ SYXVE KSIYW JSVXY RI'


def decrypt(key, message):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    payload = ""
    for l in message:
        if l in a:
            index = (a.find(l) - key) % len(a)
            payload = payload + a[index]
        else:
            payload = payload + l
    return payload


for i in range(26):
    print(chr(i + 65), ":", decrypt(i, cyphertext))
