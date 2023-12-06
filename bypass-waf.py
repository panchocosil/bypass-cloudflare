import argparse
import subprocess

parser = argparse.ArgumentParser(description='Check if IPs bypass WAF on hosts.')
parser.add_argument('-d', dest='domain', required=True,
                    help='single domain to check')
parser.add_argument('-ip', dest='ips', required=True,
                    help='file with a list of IPs')
parser.add_argument('-match', dest='match', required=True,
                    help='word to match in the host response')

args = parser.parse_args()

with open(args.ips) as ips_file:
    ips = ips_file.read().splitlines()

for ip in ips:
    cmd = f'curl -L --max-time 5 -i -s -k -X $\'GET\' -H $\'Host: {args.domain}\' -H $\'User-Agent: Mozilla/5.0\' $\'https://{ip}/?malicious=../../../etc/passwd\''
    result = subprocess.run(cmd, shell=True, capture_output=True)

    if result.returncode != 0:
        print(f'The IP {ip} did not work')
    elif '403 Forbidden' in result.stdout.decode() or '429 Too Many Requests' in result.stdout.decode():
        print(f'The IP {ip} did not work')
    elif args.match in result.stdout.decode():
        print(f"\033[1;31mThe IP {ip} bypass WAF\033[0m")
        print(cmd)
    else:
        print(f'The IP {ip} did not work')
