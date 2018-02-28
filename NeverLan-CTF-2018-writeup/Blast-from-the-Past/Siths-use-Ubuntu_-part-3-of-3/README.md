# NeverLan CTF 2018: Siths use Ubuntu (part 3 of 3)

**Category:** Blast from the Past
**Points:** 150

**Description:**

>Ok... So the boss of your company has come to the security team with a problem. His "secure" linux box has been hacked. Password is: neverlan

>There are 3 things we need you to do. This is part 3.

>You've got to figure out how they broke in.
>https://s3-us-west-2.amazonaws.com/neverlanctf/files/neverlan.ova

## Write-up

That was really fast.

1. I downloaded image .ova, imported this to VirtualBox.
2. Logged in and run terminal.
3. Typed in terminal:
>grep ssh /var/log/auth.log
4. After few secs I get something intresting.

>Good Job! It looks like it was brute forced. Your an sw er is: should-have-used-fail2ban

So, our flag is:

`should-have-used-fail2ban`
