# NeverLan CTF 2018: dot dot dashish
**Category:** Cryptography 
**Points:** 200

**Description:**

>>97316965853979963985499179367294639394818957686961793985758977285755179717668146351797581542771573123768175949171639399579635857539139371589197916944146353461537149577161797698979
>>For this cipher you might need our NEVERLANCtf to See!

## Write-up

In this problem the title gives away a hint. After googling phrase ‘dot dot dash’ one of the things that pop out is Morse Code. Obviously, Morse Code doesn’t contain numbers, so we searched a tool on https://www.dcode.fr with keyword: ‘morse’ and one of the options was Morbit Cipher:

>https://www.dcode.fr/morbit-cipher#0

On the website you can see that the KEYWORD to decryption needs to have 9 digits. Also, in the word ‘NEVERLANCtf’ first 9 digits are capital letters. It was clear that:

> our keyword is: NEVERLANC

Applying Morbit Decoder we got:

> EVEN MORSE CODE HAD ENCRYPTION THROUGH OUT HISTORY HUMAN HAVE LOVED SECRETS YOUR FLAG IS ENCRYPTALLTHETHINGS

So our flag is:

>’encryptallthethings'
