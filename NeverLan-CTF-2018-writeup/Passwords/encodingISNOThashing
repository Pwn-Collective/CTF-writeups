# NeverLan CTF 2018: Encoding != Hashing
**Category:** Passwords 
**Points:** 100

**Description:**
>>Description: Here's a PCAP. Get BashNinja's Password to the Jedi Archives. Profit

## Write-up
After opening downladed packet in wireshark we looked into protocol hierarchy (it is under Statistics->Protocol Hierarchy). 
One of the protocols that cought our attention was HTTP.
After applying http filter we also searched payload of remaining packets for words: ninja, bash, jedi. 
You can do id with: edit->find packet and select String,Packet bytes.

We found a packet with :

GET / HTTP/1.1
Accept: text/html, application/xhtml+xml, */*
Accept-Language: en-US
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
Accept-Encoding: gzip, deflate
Host: bashthebest.ninja
Authorization: Basic YmFzaE5pbmphOmZsYWd7aGVscC1tZS1vYml3YW59
Connection: Keep-Alive
DNT: 1

googling "basic authorization http" we found out that Basic Authorization is juse base64 encoded. So using http://rumkin.com/tools/cipher/base64.php
we docoded password to : 
>bashNinja:flag{help-me-obiwan}

