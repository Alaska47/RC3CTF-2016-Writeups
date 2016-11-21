#300 - Cats
>Problem description here

We were given a link to a gif file. After we download the file, our first instinct was to split the gif.
We used (http://ezgif.com/split) to split the gif into frames, and downloaded the frames.

We can see that there are 8 frames, and the problem description states that we need to find 8 characters, so we can be pretty sure that each frame decodes into one character.

We tried to run foremost, binwalk, and strings on the images, but that yielded no results. But then we looked at the images themselves, and saw that the number of cats may mean something.

We counted the number of cats in each image and got:

`14 9 1 20 23 15 5 13`

All of the numbers are below 26, so we thought alphabet indexes. So we used (http://rumkin.com/tools/cipher/numbers.php) to convert the numbers to letters and got:

`NIATWOEM`

We tried "RC3-2016-NIATWOEM" as the flag, but it didn't work. Then we saw MEOW in the word if you reverse the string, so we reversed the string and entered that as the flag.

#Flag

>RC3-2016-MEOWTAIN
