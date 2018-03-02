# NeverLan CTF 2018: Zip Attack
**Category:** Passwords 
**Points:** 100

**Description:**
>>Description: We intercepted this encrypted zip.<br> And we noticed it had a file inside that we have previously seen. Will that help you crack it open?

## Write-up
So we have a copy of the same file in password protected zip and normal zip. 
After googling "zip same file attack" we spotted "Cracking Zip files (known-plaintext attack)" this is what we were looking for.
After reading the story at:
> http://www.securiteam.com/tools/5NP0C009PU.html
we decided to give pkcrack a try. Both files were commpressed with the same method, so we were good to go. Command:
./pkcrack -C encrypted.zip -P known-file.zip  -c supersecretstuff/sw-iphone-wallpaper-first-order.jpg -p sw-iphone-wallpaper-first-order.jpg  -d output.zip -a

pkcrack saved a copy of the decrypted zip in output.zip, after unziping we got:
flag{plaintext-attacks-are-cool!}


