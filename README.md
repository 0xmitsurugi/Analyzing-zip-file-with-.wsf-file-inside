# Analyzing-zip-file-with-.wsf-file-inside

Between the 13 and 16 of july, I've received of lot of spams, all based
on the same, now classical, pattern. A zip file, containing a .wsf file.

This is Locky malware. I published some scripts in order to help people
to analyze it.

You can use the script with zip files or .wsf file. It works only with Locky.

You can find here:
 * analyze.py : it tries to extract and find malicious URL from where malicious data is downloaded. Warning: it uses an eval() on parts of the .wsf file. Give a zip or .wsf as an argument.
 * unxor.py : it tries to unxor the malicious data in order to give you back the original exe file
 * 6A28B_mitsu.zip : a zip file with a .msf file inside. It's protected with the pass "infected". WARNING: this file can harm your computer. Treat it with caution.
 * UHE_prng.js : this file will print 200k random numbers seeded with a spcific value.
 * prng_js : 200k random numbers seeded the default value.
 * o54b6 : an encrypted file. WARNING: this file can harm your computer once un-xored.

You can read http://0x90909090.blogspot.fr/2016/07/analyzing-zip-with-wsf-file-inside.html for more information and http://0x90909090.blogspot.com/2016/07/update-about-locky-xoring-data-scheme.html.
