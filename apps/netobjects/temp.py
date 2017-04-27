import re

web_address = 'https://41.207.231.66:981'

pattern_web_address = re.match('(^\w+)://(\d+.\d+.\d+.\d+)', web_address)

dns_check = False  # flag, that show that web_address is IP address or DNS address, by defailt it's IP addres
if not pattern_web_address:
    pattern_web_address = re.match('(^\w+)://(.+):(\d+)', web_address)  # https://blabla.dyndns.org:65550
    dns_check = True
    if not pattern_web_address:
        pattern_web_address = re.match('(^\w+)://(.+)', web_address)  # https://blablabla.dyndns.org
        dns_check = True

# automatically fullfill cli_address, dns_address/ipv4_external_address fields
cli_address = pattern_web_address.group(2) + ':' + str(cli_access_port)
if dns_check:  # fullfill only 1 of 2 fields: or dns or ipv4
    dns_address = pattern_web_address.group(2)
    ipv4_external_address = ""
else:
    ipv4_external_address = pattern_web_address.group(2)
    dns_address = ""
