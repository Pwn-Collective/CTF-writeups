# NeverLan CTF 2018: Can you search it?

**Category:** Trivia
**Points:** 100

**Description:**

>For the Vulnerability you found in question 2, There is a proof of concept. What is the string for TARGET_HAL_HEAP_ADDR_x64?

## Write-up

When I typed in google variable from task the query returned a link to a exploit on github:

>https://github.com/RussianOtter/Mobilesploit/blob/master/exploit/EternalBlue.py

And we have the variable declaration:

>TARGET_HAL_HEAP_ADDR_x64 = 0xffffffffffd00010

So our flag is:

`0xffffffffffd00010`
