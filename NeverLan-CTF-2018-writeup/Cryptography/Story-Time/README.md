# NeverLan CTF 2018: Story Time!
**Category:** Cryptography 
**Points:** 200

**Description:**

>>Are you ready for a story? 
>>-5.;56 76†† ?)8† ;48 3‡0† 2?3 -6.48( ;‡ 46†8 ;48 0‡-5;6‡ ‡1 46) ;(85)?(8 6 5 );‡(: ](6;;8 2: 8†35( 5005 .‡8 6 1053 6) .6(5;8)5*††5338()


## Write-up
The given ciphertext has very distinct syntax. By the look you can tell that it's a GOLD BUG ciphertext, which can be found here: >https://www.dcode.fr/gold-bug-poe.

Using Gold Bug Decoder we got this:

>“CAPTAI KIDD USED THE GOLD BUG CIPHER TO HIDE THE LOCATIO OF HIS TREASURE I A STORY WRITTE BY EDGAR ALLA POE I FLAG IS PIRATESANDDAGGERS”

So our flag is:

>'PIRATESANDDAGGERS'
