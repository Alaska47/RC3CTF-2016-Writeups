#400 - Dirty Birdy

>We were given a  ![dump](https://github.com/RITC3/RC3CTF-2016/blob/master/Forensics/Forensics-400/dtrump.img.zip)

#Solution

First we extract the image and mount it. We then start examining the files for anything interesting. First thing to check is always the logs. We search `log` and `.log` and check all of the files that come up, but there wasn't anything peculiar. We then look on the root home folder and start looking in those files. When we looked at `_HISTORY` we knew we found something.

```
    1  mkdir secret files
    2  mkdir secretfiles
    3  rm -rf secret files/
    4  ls
    5  cd secretfiles/
    6  gpg --gen-key
    7  lkjsanfdklsnflkjsldfnlksjflksnklfsdknsaasl;kn;sdlafasnflnsa;lfn;lsanfas;dnfijsad;jnkmkjlknsm;dafijks mjnskfdmcmfd;najmldkfjdasnlvmdflkdasvklnmdsavjbknmdslvjdnjsmalcdvkjdknsfm,lvzcxkjkxlzvndsmd,lsakcvxzjklnm,s.admkcvxzojklnm,sadmlkcvxzjklnvm,smdalkcvjxzklnm,sdmalkcvzxjknm,s adlkcvcjzxknm,sdalkcvxnm,smdslakclvcnm,lkacslcm,lcsklv;mc ,slacxzknmc ,l,cxzkmmc,lcxzmk c,xlczklm ,lxkczlncm ,lcxzk lm zc,alscxzkln'klsdml'kanlnlksdnvla'dlvvalslsalsdlksnadv'sdlkvnsd'lvn'alskdnv'lsdkvns'ldnv'sldkvnsa'ldkvns'ladvnlasdvkna'sdvknasdv'a'sdvlnasdv'adnv'asdv'ksndv'sadv'savd'lsnadv'lskdnv'sdvlnsdv'lksadnv'lsamdv;lsdmv';lsa;dlvms'advm';asdmv';sadv;las'dmvsadv';asdlmvsa'd;vlmasd'vnmas'dv;lmsd'v;lsmadv';sladmv'sa;ldvmas'vd;l'masv';oasekmo;kmsdvav';lasdmv's;alvm'a;sldvm'sa;dlvmsa';ldvms'a;dvlmsd';vlmsa'd;vlsmad'vlksadv';lsamdv';saldmv';lsdavm'sad;vm'as;dlvmasd'v;lmsadv'asd;lmassdkalmvsad'sadmv'asd;vmasdv';saldmvsad';vkmsa'v;msdv';sadv';sadv;lasmvd';asldmvsa';dlvmsad;alssdav';saldvasdv';lsdamv'as;dv's;ladm'v;sdlmdv';lmdav';lmdsa';lsdv';lsdmv';lsdmsdva';lmsadv';ladvm'sdm;l'dsam';dlvsm'sadv;lmsda';msd';lmsv';lmsdv';lmdsvsdv;lmdv';ladsm'dsopwe[wqw
    8  alkn;lasdnf;lkasnd;flk,m smcm, lpcm ,sdlafk;ndv;kszlakofenjkvzoavdfewn;kavd;ndasfwken vkdmfavknv dakdskofweknv asdfokknv zvasdfkowdvknz cvsadkodvknzvsdakfokdvnzskdakfmkdlv;szsdmakfmldvsm ,zcxmvsadkvnz cxmvsdakofnv zcxvsdakofkdnv zsdakfokndv zcxvmsdakfkndv zvsdmkndv cxzmvsdaknvm zmvsdamkns vdczxmvsdkfknsvczxmvksdmknmv czxmvkslamfm ,vczmxlvsfam CXZMSdwqn. fdsvzcbzxshad m,czxc kojiobjkf wqeml;wpfasdovzxci0 
    9  LS
   10  ls
   11  gpgp
   12  gpg
   13  gpg --edit-key
   14  gpg --edit-key 'ThugG'
   15  gpg --encrypt Workbook1.xlsx 
   16  ls
   17  shred -n 200 -z -u Workbook1.xlsx
   18  ls
   19  vim document.txt
   20  gpg --export-secret-key -a "ThugG" > /home/dtrump/secretfiles/private.key
   21  echo "# supersecret" >> README.md
   22  git init
   23  git add private.key 
   24  git commit -m "initial commit"
   25  git config --global user.email "nope@gmail.com"
   26  git config --global user.name "ThugG"
   27  git commit -m "initial commit"
   37  history -c
```

We see that this person created a secretfiles directory. Then, we see that he used ![gpg](https://www.gnupg.org/documentation/manpage.html) to create a key and encrypt an excel file. Then deleted the original excel file, opened and presumably edited document.txt. He then exported the gpg key he used to encrypt the excel file and uploaded it onto a git repository.
We see that there is a folder named SECRETFI. This is probably the directory that this person created. We cd into it and start looking at the files.
We see the encrypted WORKBOOK.GPG that we will probably need to decrypt.
We quickly look in document.txt and find:
`passowrd123`
After reading a bit about gpg, we found that we need the key that was used to encrypt it. So we look inside the `_GIT` folder and look inside the `CONFIG` file to find a link to a git repository.
`https://github.com/rc3club/supersecret.git`
We click it and find private.key. We can now use this to decrypt `WORKBOOK.GPG`!!!
We cd into the directory with `private.key` and `WORKBOOK.GPG` then run the following command:
`gpg --import private.key`
This imports the private key which we can now use to decrypt `WORKBOOK.GPG`
`gpg -d WORKBOOK.GPG > workbook.xlsx`
Now we have the decrypted excel file. We open it and find a password prompt. This must be the password in document.txt! So we input `passowrd123` and it didn't work! But turns out they made a typo and the actual password was `password123`
We open the excel file and click on Sheet2 to find the flag.

#Flag

>RC3-2016-SNEAKY21
