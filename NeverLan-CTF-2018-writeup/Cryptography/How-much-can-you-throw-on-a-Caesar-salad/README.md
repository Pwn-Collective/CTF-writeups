# NeverLan CTF 2018: How much can you throw on a Caesar salad?
**Category:** Cryptography 
**Points:** 300

**Description:**
>>Cryptography is the art of hiding things. there are multiple ways to do it. There are multiple layers to this message. When you find the answer then make it a flag.. mihi nomen latine! Example: flag{WORDS_WORDS_WORDS}

## Write-up
In this problem we were given a photograph of Albert Einstein with a quote. When seeing a photograph the first thing that comes to mind is steganography. However, in order to use this cipher you need to have a password. 

> website: https://futureboy.us/stegano/decinput.html

Guessing the password was quite a process, we put everything that was connected to Einstein or to Caesar. After many attempts we changed “our password theme” into everything connected to organizers and the event itself.

Finally, it turned out to be:

>pass: neverlanctf

And after applying the steganography decoder we got this:

> MDEwMDExMDAgMDExMDAxMDEgMDExMTAxMTEgMDExMDExMDAgMDExMTEwMDEgMDExMTAwMDAgMDExMDExMDAgMDExMTAxMDEgMDExMDEwMTAgMDExMDExMDAgMDAxMDAwMDAgMDExMTAwMDAgMDExMTEwMTAgMDAxMDAwMDAgMDExMDAwMDEgMDExMDExMTEgMDExMDExMDAgMDAxMDAwMDAgMDEwMDAwMDEgMDExMDExMDAgMDExMDEwMDAgMDExMDEwMTAgMDExMDExMTEgMDExMDExMDAgMDExMTEwMDEgMDAxMDAwMDAgMDExMTAxMTAgMDExMDExMDEgMDAxMDAwMDAgMDExMDEwMDAgMDExMTAwMTEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDAwMDEgMDExMDExMTEgMDExMTAwMDAgMDExMTAxMDEgMDExMDExMTAgMDExMTEwMTAgMDAwMTAxMA==

You see the letters with ‘==’ at the end? That’s definitely base64! We converted Base64 to ASCII, and ended up with this:

>01001100 01100101 01110111 01101100 01111001 01110000 01101100 01110101 01101010 01101100 00100000 01110000 01111010 00100000 01100001 01101111 01101100 00100000 01000001 01101100 01101000 01101010 01101111 01101100 01111001 00100000 01110110 01101101 00100000 01101000 01110011 01110011 00100000 01100001 01101111 01110000 01110101 01101110 01111010 0001010

There’s no need to explain that this text is binary, so we converted Binary to Ascii, and got this:

>  Lewlyplujl pz aol Alhjoly vm hss aopunz

Nothing readable! But… it looks like something we can put into our favourite online cryptogram:

> https://quipqiup.com/

Yes! We managed to find the quote!

> Experience is the Teacher of all things

But that’s not the end! The question says:  mihi nomen latine! , which means name it in latin. So we named it! Who said the quote? It was Gaius Julius Caesar, but that’s not in latin!

So the flag is: 

>CAIVS_IVLIVS_CAESAR
