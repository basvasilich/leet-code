# https://leetcode.com/problems/validate-ip-address/


import re


class Solution:
    def validIPAddress(self, IP: str) -> str:
        results = ["IPv4", "IPv6", "Neither"]
        hex_c = '123456789ABCDFEabcdfe'

        if IP.count('.') == 3:
            groups = IP.split('.')
            for group in groups:
                if not re.match(r"^[0-9]+$", group):
                    return results[2]
                if len(group) > 1 and group[0] == '0':
                    return results[2]
                if int(group) < 0 or int(group) > 255:
                    return results[2]

            return results[0]
        elif IP.count(':') == 7:
            groups = IP.split(':')
            for group in groups:
                if len(group) > 4:
                    return results[2]
                if not re.match(r"^[0-9a-fA-F]+$", group):
                    return results[2]
            return results[1]
        else:
            return results[2]
