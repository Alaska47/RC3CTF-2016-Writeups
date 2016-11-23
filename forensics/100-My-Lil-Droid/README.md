#100 - My Lil Droid

>We were given an ![apk](https://github.com/Alaska47/RC3CTF-2016-Writeups/blob/master/forensics/100-My-Lil-Droid/youtube.apk) file.

#Solution

Upon extracting the contents of the apk, we start searching through the files. In `build-data.properties`, we spot something peculiar.
`UkMz-2016-R09URU0yMQ==`

This is clearly the flag because of the -2016-. The `==` at the end tells us that it is most likely base 64, so we use decode it using base 64 and get the flag.

```python
import base64
print base64.b64decode("UkMz") + "-2016-" + base64.b64decode("R09URU0yMQ==")
```

#Flag

>RC3-2016-GOTEM21
