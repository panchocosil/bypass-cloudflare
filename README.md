This Python script is designed to bypass Cloudflare protection by accessing the server's direct IP address instead of the protected domain name. It can be used by specifying the path to the files containing a list of hosts and IPs.

To obtain the IPs, the script can make use of resources like https://search.censys.io/. Subdomains can be gathered using tools like https://github.com/owasp-amass/amass or similar.

The usage of the script is as follows: 

*bypass-cloudflare.py:*

python3 bypass-cloudflare.py -H hosts-file.txt -ip ips-file.txt

*bypass-waf.py:*

python3 bypass-cloudflare.py -d example.com -ip IPs.txt -match "Login Page"
