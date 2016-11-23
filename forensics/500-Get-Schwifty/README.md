#500 - Get Schwifty
> Problem description here

#Solution
The problem originally gave us a memory dump, and later in the competition, a zip file. Using a tool called volatility (`sudo apt-get install volatility`), we can analyze the memory dump to extract the TrueCrypt container and password.

The first thing I ran was `volatility imageinfo -f dump.raw` in order to figure out the profile (OS) which is necessary to run other commands. Running the command tells us that the most likely profile is `Win7SP0x64`, so we can use that for additional commands.

The next thing I ran was `volatility --profile="Win7SP0x64 -f dump.raw pslist"` in order to find what processes were running when the memory was dumped. The output is shown below. Taking a quick look at the processes reveals that several instances of `chrome.exe` were running when the memory was dumped.

![chrome.png]()

