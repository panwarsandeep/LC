from collections import defaultdict
import re
class Solution:
    def validIPAddress(self, IP):
        def check_ipv4(IP):
            tup = IP.split(".")
            if len(tup) != 4:
                return "Neither"
            for t in tup:
                try:
                    if int(t) > 255 or \
                        len(t) != len(str(int(t))):
                        return "Neither"
                except ValueError:
                    return "Neither"
            return "IPv4"

        def check_ipv6(IP):
            tup = IP.split(":")
            if len(tup) != 8:
                return "Neither"
            for t in tup:
                if len(t) > 4:
                    return "Neither"
                try:
                    tmp = int(t, 16)
                except ValueError:
                    return "Neither"
            return "IPv6"

        is_dot = True if "." in IP else False
        is_colon = True if ":" in IP else False
        if (is_dot and is_colon) or \
            not (is_dot or is_colon):
            return "Neither"
        if is_dot:
            return check_ipv4(IP)
        return check_ipv6(IP)

if __name__ == '__main__':
    sol = Solution()
    
    ip = "172.16.254.300"
    #ip = "25.25"
    print(ip)
    r = sol.validIPAddress(ip)
    print(r)