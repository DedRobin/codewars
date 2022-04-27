'https://www.codewars.com/kata/525f50e3b73515a6db000b83'

def create_phone_number(n: list):
    n=list(map(str,n))
    n.insert(0,'(')
    n.insert(4,')')
    n.insert(5,' ')
    n.insert(9,'-')
    return ''.join(n)