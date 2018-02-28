# NeverLan CTF 2018: tik-tik-boom

**Category:** Web Exploitation
**Points:** 300

**Description:**

#UPDATE!
>$$$$$ Correction a Player found a bug can you find it???

>http://neverlanctf-challenges-elb-2146429546.us-west-2.elb.amazonaws.com:14065/

## Write-up

In source we have some credentials:

>admin:hahahaN0one1s3verGett1ngTh1sp@ssw0rd

We can set it in cookies. But when in source we have:

>Close, but your timing is off purvesta...

First clue is 'purvesta's time.'

Tanner Purves aka Puvesta is NeverLan CTF Team member:

>https://neverlanctf.com/Purvesta

From his twitter we know He is from Idaho.

>https://twitter.com/purvesta0704

We are in Poland, so we have -7 hours to Idaho. If we wait and reload site in right time we get the flag!

`flag{You_are_really_good_at_this_timing_thing}`

We probably also have a bug (see #UPDATE) which allow download source code.
