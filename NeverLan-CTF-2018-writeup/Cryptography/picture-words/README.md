# NeverLan CTF 2018: Picture Words
**Category:** Cryptography 
**Points:** 200

**Description:**

>>Pictures have meaning, You just have to be able to understand!
>>https://ctf.neverlanctf.com/files/b887f34cb2dc9a2b0c1f3ea905728f5e/Invisible.jpeg

## Write-up

In this problem we were given a picture with 10 lines of symbols. We noticed that the symbols are repeated. But, no well-defined pattern can be found. For this reason, we assigned random letters to each symbol, and got this:

>LKNAVOBSXAFCTODBNGVIXFREEKNTOOEVXAVENRIOHJXVEKRPUXAFREEKNBRSNVHBRFXVCXPEXTNVLOTEKREKOXVRAILOTIV

Then, we used:
>https://quipqiup.com/

And got this:

>WHEN SOLVIG PROBLEMS DIG AT THE ROOTS INSTEAD OF YIST HACKING AT THE LAVES FLAG IS PIC TIRES WORTH AT HO IS AND WORDS
 
Probably, we made a few mistakes while assigning letters to symbols. However, we can clearly see that our flag is:

>’PICTURES WORTH A THOUSAND WORDS’
