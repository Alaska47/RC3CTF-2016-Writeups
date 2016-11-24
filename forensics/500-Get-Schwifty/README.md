#500 - Get Schwifty
> Problem description here

#Solution
The problem originally gave us a [memory dump](https://drive.google.com/file/d/0Bw7N3lAmY5PCdVYzMDdqS2E2MzA/view), and later in the competition, a [rar file](https://drive.google.com/file/d/0Bw7N3lAmY5PCODdpeTJPZjJjVUk/view). Using a tool called volatility (`sudo apt-get install volatility`), we can analyze the memory dump to extract the TrueCrypt container and password.

The first thing I ran was `volatility imageinfo -f dump.raw` (WARNING: the command took me a while to run so don't quit if you don't see anything) in order to figure out the profile (OS) which is necessary to run other commands. Running the command tells us that the most likely profile is `Win7SP0x64`, so we can use that for additional commands.

Realizing that I was looking for a TrueCrypt container and its password, I tried running several commands such as `truecryptsummary` and `truecryptpassphrase` which revealed nothing about the container or its password.

The next thing I ran was `volatility --profile=Win7SP0x64 -f dump.raw pslist` in order to find what processes were running when the memory was dumped. The output is shown below. Taking a quick look at the processes reveals that several instances of `chrome.exe` were running when the memory was dumped.

![pslist.png](https://raw.githubusercontent.com/Alaska47/RC3CTF-2016-Writeups/master/forensics/500-Get-Schwifty/pslist.png)

Doing a quick google search on how to view chrome history takes us to this [link](http://blog.superponible.com/2014/08/31/volatility-plugin-chrome-history/). After I downloaded and saved the plugins, I ran `volatility --plugins=/home/aneesh/v-plugin/chrome --profile=Win7SP0x64 -f dump.raw chromehistory` (WARNING: the command took me a while to run so don't quit if you don't see anything) where `/home/aneesh/v-plugin/chrome` is the directory in which I saved the `.py` file. Unfortunately the command didn't output anything for me, but taking a look at the other plugins, I decided to run `chromesearchterms`. 

The output of `volatility --plugins=/home/aneesh/v-plugin/chrome --profile=Win7SP0x64 -f dump.raw chromehistory`, shown below, reveals several interesting things. The user searched up `truecrypt` and `lastpass` several times, leading me to suspect whether the password to the TrueCrypt container was in LastPass.

![chrome_extension.png](https://raw.githubusercontent.com/Alaska47/RC3CTF-2016-Writeups/master/forensics/500-Get-Schwifty/chrome_extension.png)

Searching up how to extract LastPass passwords using volatility revealed this [link](https://techanarchy.net/2016/10/extracting-lastpass-site-credentials-from-memory/). After I downloaded and saved the plugins, I ran `volatility --plugins=/home/aneesh/v-plugin/lastpass --profile=Win7SP0x64 -f dump.raw lastpass` (WARNING: the command took me a while to run so don't quit if you don't see anything) where `/home/aneesh/v-plugin/lastpass` is the directory in which I saved the `.py` file. The output of the command is shown below.

![lastpass.png](https://raw.githubusercontent.com/Alaska47/RC3CTF-2016-Writeups/master/forensics/500-Get-Schwifty/lastpass.png)

Now that I had the TrueCrypt container password `VNBLnVqeqpBWnnr8bdR7iLehx`, all I needed to do was open the TrueCrypt container. Looking at the rar file and extracting it, I found `supersecret.docx`. I suspected that was the TrueCrypt container and I realized my suspicions were right after I ran TCHunt on the rar file, revealing that supersecret.docx was indeed a TrueCrypt container. All that is left to do was to mount the TrueCrypt container. The flag is shown in the image below (NOTE: you don't need to enter anything for the keyfile).

![flag.png](https://raw.githubusercontent.com/Alaska47/RC3CTF-2016-Writeups/master/forensics/500-Get-Schwifty/flag.png)

#Flag
RC3-2016-aEv6riGd
