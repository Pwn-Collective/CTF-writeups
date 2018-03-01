# NeverLan CTF 2018: Always in a rush to find it...
**Category:** Cryptography 
**Points:** 200

**Description:**

>>MGPVHSYSYHDZJZTKSNDSSZGJYJXCVJLVSIENBEDVUDJYTSVRFKEJFISLXBSFTOEELYXFWPRNGJYJXCVJJIUZODYA


## Write-up

We see that this ciphertext has a very low coincidence score. So you can guess that this cipher uses multiple alphabets or it's keyed.

Another characteristics of the given text is that it contains only letters.

This is how you can recognize it’s a Jefferson’s Wheel ciphertext. After applying Jefferson’s Wheel decoder, which can be found here:
>https://www.dcode.fr/jefferson-wheel-cipher

We got:

>FOURTHREEDOTEIGHTSEVENNINEZEROONESIXCOMMASPACETACONEZEROTHREEDOTFOURFIVENINEZEROZEROFOUR

Writing down the numbers we got: 
> 43.879016, TAC 103.459004

This immediately looked like coordinates! Since the coordinates don’t specify the cardinal directions, by default Google sent us to Mongolia! However, we noticed that our task was heavily “American themed”, the only reasonable direction was North-West. We arrived at Mt. Rushmore!

So what’s the flag?

>'mount Rushmore’
