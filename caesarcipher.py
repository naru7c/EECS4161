cyphertext = 'XLIWP MRKWE RHEVV SAWSJ SYXVE KSIYW JSVXY RI'


def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


for i in range(26):
    print(chr(i + 65), ":", decrypt(i, cyphertext))
