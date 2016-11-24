#400 - Music to my Ears
>Problem description here

#Solution
The problem gives us an `.aup` file, which is an Audacity Project file. Opening this file up in Audacity reveals that there are several tracks playing at the same time (`The Chainsmokers - Closer (Lyric) ft. Halsey`, `whoa`,`Fetty Wap-'679' Ft.Remy Boys OnScreen Lyrics`,`the_flag_is_somewhere`,`this_ain't_the_flag`). Playing the sounds and looking at the other tracks reveals that the only one of interest is `whoa`. I took a look at the spectrogram which unfortunately didn't reveal anything (then again, it’s a 400 point problem!).

![spectrogram.png](https://raw.githubusercontent.com/Alaska47/RC3CTF-2016-Writeups/master/misc/400-Music-to-my-Ears/spectrogram.png)

Next I took a look at the problem. It mentions Sirius XM, which is a broadcasting company for radio signals. The problem also talks about signals. I figured the `whoa` track might be a radio signal which I could then decode. A quick Google search for `radio signal database` revealed a [database](http://www.sigidwiki.com/wiki/Database) for radio signals. I went through all the signals usually looking at the spectrogram, and if the beginning looks similar to the one I’m looking for, I would play the sound recording to see the header.

Eventually after going all the down to the S’s, I came across Slow-Scan Television, which was a 

>method for picture transmission used by amateur radio operators to transmit and receive images.

![sstv.png](https://raw.githubusercontent.com/Alaska47/RC3CTF-2016-Writeups/master/misc/400-Music-to-my-Ears/sstv.png)

That seems interesting. Playing the audio clip that came with it revealed that the header was the exact same! The wiki suggests using the [MultiPSK](http://f6cte.free.fr/index_anglais.htm) software for Windows to decode the transmission. The software is somewhat badly designed with lots of small buttons and many options. However the important ones are `Sound Card (Input)` at the top and `RX/TX Screen`. Make sure the computer default sound card option is selected. If you want to use Stereo Mix to record the audio, feel free to do so as well. 
Next, clicking on `RX/TX Screen` reveals another window with many buttons. Again, the important ones are the `SSTV` button on the top right/middle part of the screen. After selecting SSTV, play the `whoa` track. If you want, you can export the track to a wmv and then play it but it’s not necessary. At first, it might take a while for the image to start appearing, but after waiting for about 30 seconds, you should see a blue/purple image. If it appears in other colors, or the text is faint, press the blue `Synchro` button above the image and play the track again. Eventually, after waiting for a couple minutes, the flag should appear, as shown below.

![flag.png](https://raw.githubusercontent.com/Alaska47/RC3CTF-2016-Writeups/master/misc/400-Music-to-my-Ears/flag.png)

#Flag
RC3-2016-BEAMMeUP
