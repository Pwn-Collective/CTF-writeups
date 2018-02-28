# NeverLan CTF 2018: Das_blog

**Category:** Web Exploitation
**Points:** 200

**Description:**

>John made a new web site go check it out

>http://neverlanctf-challenges-elb-2146429546.us-west-2.elb.amazonaws.com:14054

## Write-up

In source of login.php we have login & password for dev account:
><!-- Development test account: user: JohnsTestUser, pass: AT3stAccountForT3sting -->

If we look at the cookies we will find this:
>permissions=user

So, mabye we change it to admin?

Yes! After change and reload main site we have:
>You have ADMIN permissions

And our flag is:
`flag{C00ki3s_c4n_b33_ch4ng3d_?}`
