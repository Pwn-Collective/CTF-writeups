# NeverLan CTF 2018: The Password Manager

**Category:** Passwords
**Points:** 300

**Description:**

>Description: Here's a password manager vault. We picked this up through a compromised dropbox account. They should have enabled 2-FA.

**Prerequisites:**

>pip install opvault

>hashcat

**Writeup author:**

chudy

## Write-up

This task can be solved with at least two approaches. The first one is very simple - perform dictionary/brute force attack on the vault. I have assumed that this master password may be harder, so I have decided to perform master password cracking with the hashcat. So, this writeup will show how to crack 1Password OPVault master passwords.

Going back to the task, we have a **neverlan.opvault** with the **profile.js** file and **band_9.js**. After a bit of research, it occurs that this is the OPVault format for the 1Password. Details can be found in [here](https://support.1password.com/opvault-design/). If we read the OPVault documentation carefully (especially **_profile.js_** and **_key derivation_** parts), we can find out that all we need for the password cracking is **profile.js** file. We are dealing with PBKDF2-HMAC-SHA512 here.

Yeah, but almost everything in _profile.js_ is base64 encoded, plus this _masterKey_ has a weird length and this is definetely not a hash. Moreover, what about the hashcat? There is this 8200 mode:

> 8200 | 1Password, cloudkeychain                         | Password Managers

Still, we don't know how to derive the proper data from the _profile_ JSON. That was the hardest part of the challenge for me. After a bit of googling and code reading, I have found out that _hashcat -m 8200_ takes the following input:

>hash:salt:iterations:data

Salt and iterations are clearly visible in the provided JSON, what about hash and data? It occurs, that hash is stored in the last 32 bytes of _masterKey_, whereas rest of the _masterKey_ is the "data".

Now, let's write a simple python code to prepare _in.txt_ for password cracking in hashcat 8200 mode. Whole code can be found [here](https://github.com/Pwn-Collective/CTF-writeups/tree/master/NeverLan-CTF-2018-writeup/Passwords/The-Password-Manager/op2hashcat.py).

```python
import json
import binascii
import base64

if __name__ == "__main__":
	
	#import json
	with open('neverlan.opvault/default/profile.js') as f:
		profile = json.loads(f.read()[12:-1])

	#get data for hashcat input
	out = list()
	#hash - last 32 bytes of masterKey - decode from base64 and save as hex
	out.append(binascii.hexlify(base64.decodestring(profile['masterKey'])[-32::]))
	#salt - decode from base64 and save as hex
	out.append(binascii.hexlify(base64.decodestring(profile['salt'])))
	#iterations
	out.append(str(profile['iterations']))
	#data - rest of the masterKey - decode from base64 and save as hex
	out.append(binascii.hexlify(base64.decodestring(profile['masterKey'])[0:-32]))

	#create output
	out_str = ':'.join(out)

	with open('in.txt','w+') as f:
		f.write(out_str)

	print out_str
```

The input to the hashcat is:

>e4eafa77baa7211b70394190de95cecc815987559830afe0f77fd42c3f230a58:60a1d2264df6376b0242d4db1cc1fac3:100000:6f70646174613031000100000000000072687222ed2ee1208f3a926c82ab710f75b1809fbb49edd8b2408d127673d585e7c685dae9c183258f67c1aba148becc29271d90df7697c17fde9643aeb41681d688b08beb27dbf8d91663ab58830837ee60d3741b15ce9aba32a809f13c8ac960aa9100911ef665cd6a5795405cb5b0bf1de20e04c757032d44a394a71fc84c29a06217607697ee23c0231d3065b12b80bf9c5c2aa6133ffd33f8c412d62c6884a9201322e36b3a278426a1851c09b846accd32b1d77861121954d0df789e7edda01112e2972b819eee32cad4476b73ca0fbb810cc5ea74b2bc29b2c039f8031b426b8f0d23cfb89abbd3b6f8b773c4cefa1f43ceb27bd42dc5fba5a2ae7f19a62ca06b5942096c0ae724a388fef6996c891f26792ca26bbb513736ab8c1267


So, let us confront hashcat -m 8200 mode armed with the standard Kali Linux wordlists dictonary _fasttrack.txt_ with the prepared input file:

>hashcat -m 8200 in.txt fasttrack.txt

**if hashcat** returns some GPU related errors, you can try running it with manual workload tuning

>hashcat -m 8200 -n 1 -u 1024 in.txt fasttrack.txt --force

After a while, hashcat returns a password:

>starwars

Well, that was not a hard password and in fact a simple dictionary attack on opvault would be efficient. Now, run opvault-cli and provide a _starwars_ password:

>opvault-cli neverlan.opvault flag

>1Password master password:

>Username: flag

>Password: flag{Wow_You_CRACKED-the-VAULT}

Well done! This way was definetely harder and longer way, but you have learned something about 1Password and hashcat.
