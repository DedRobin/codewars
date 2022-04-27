"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
"""

import re

def is_valid_IP(s):
    print(s)
    if s.isalpha() or s.count('.')!=3:
        return False
    s=s.split('.')
    for octet in s:
        if len(octet)==1:
            match=re.match(r'[0-9]',octet)
            if not match:
                return False
        elif len(octet)==2:
            match=re.match(r'[1-9][0-9]',octet)
            if not match:
                return False
        elif len(octet)==3:
            match=re.match(r'1[0-9]{2}|2[0-4][0-9]|25[0-5]',octet)
            if not match:
                return False
        elif not len(octet) or len(octet)>3:
            return False
    return True

print(is_valid_IP('129.70.193.111d'))