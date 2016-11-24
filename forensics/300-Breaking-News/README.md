#300 - Breaking News

>We just received this transmission from our news correspondents. We need to find out what they are telling us.
>[file](https://github.com/Alaska47/RC3CTF-2016-Writeups/blob/master/forensics/300-Breaking-News/Forensics-300.tar.gz)

#Solution
We first extract the give file, `Forensics-300.tar.gz`, and we find 20 zip files inside of it. We then extract all of these and find that each of them contain a .txt file.
We first checked all of the .txt file, and they all appear to be simple plain text files with nothing interesting. We then proceeded to the standard procedure and ran binwalk on all of the files using:
`binwalk filename`
But we found nothing. There aren't any files hidden inside of them. We then used wc to count the number of bytes in each file, and we discovered that in some files, there were extra bytes at the end! Zip files usually end in many 00 bytes, so we write a python script to extract the extra bytes.

```python
import os, binascii

for f in os.listdir(os.getcwd()):
    if (open(f, "r").read().encode("hex")[:-2] != "00" and f != "script.py"):
        a = (binascii.hexlify(open(f, "rb").read())).split("00")
        if (a[len(a) - 1] != ""):
            print f
            print (a[len(a) - 1].decode("hex"))
```

We get:
```
Chapter10.zip
MTYtRFUK
Chapter15.zip
S1lGCg==
Chapter18.zip
QkxTCg==
Chapter4.zip
UkMK
Chapter9.zip
My0yMAo=
```

It is obvious that this is base64, so we change a small part of our python program and we can piece together the flag.

```python
import os, binascii, base64

for f in os.listdir(os.getcwd()):
    if (open(f, "r").read().encode("hex")[:-2] != "00" and f != "script.py"):
        a = (binascii.hexlify(open(f, "rb").read())).split("00")
        if (a[len(a) - 1] != ""):
            print f
            print base64.b64decode((a[len(a) - 1].decode("hex")))
```
```
Chapter10.zip
16-DU

Chapter15.zip
KYF

Chapter18.zip
BLS

Chapter4.zip
RC

Chapter9.zip
3-20
```

#Flag

>RC3-2016-DUKYFBLS
