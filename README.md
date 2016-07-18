# Analyzing-zip-file-with-.wsf-file-inside

Between the 13 and 16 of july, I've received of lot of spams, all based
on the same, now classical, pattern. A mail body with wording like:
"How is it going?
Please find attached document you asked for and the latest payments report

Hope that helps. Drop me a line if there is anything else you want to know"
or
"Please find the reference letter I attached."
and a zip file attached containing a .wsf file.

You can find here:
 * analyze.py : it tries to extract and find malicious URL from where malicious data is downloaded
 * unxor.py : it tries to unxor the malicious data in order to give you back the original exe file
 * 6A28B_mitsu.zip : a zip file with a .msf file inside. It's protected with the pass "infected". WARNING: this file can harm your computer. Treat it with caution.
 * UHE_prng.js : this file will print 200k random numbers seeded with 256
 * prng_js : 200k random numbers seeded with 256.

You can read http://0x90909090.blogspot.fr/2016/07/analyzing-zip-with-wsf-file-inside.html for more information.
