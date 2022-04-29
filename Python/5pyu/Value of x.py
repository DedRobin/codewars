'https://www.codewars.com/kata/614ac445f13ead000f91b4d0'

def solve(eq: str):

    # 1)We divide the equation into left and right parts.

    eq=eq.replace('- ','-')
    eq=eq.replace('+ ','+')
    eq=eq.split('=')
    left_eq=eq[0].split()
    right_eq=eq[1].split()

    # 2)determine the arithmetic sign of the answer

    minus=False
    if '-x' in left_eq or '-x' in right_eq:
        minus=True
    
    # 3)remove 'x','+x','-x' from left and right lists

    x_in_left_eq=False
    x_in_right_eq=False
    if 'x' in left_eq or '-x' in left_eq or '+x' in left_eq:
        x_in_left_eq=True
        if 'x' in left_eq:
            left_eq.remove('x')
        elif '+x' in left_eq:
            left_eq.remove('+x')
        else:
            left_eq.remove('-x')        
    else:
        x_in_right_eq=True
        if 'x' in right_eq: 
            right_eq.remove('x')
        elif '+x' in right_eq:
            right_eq.remove('+x')
        else:
            right_eq.remove('-x')

    # 4)convert: str -> int

    if left_eq: left_eq=list(map(int,left_eq))
    if right_eq: right_eq=list(map(int,right_eq))

    # 5)find the difference between the two parts of the equation

    if x_in_left_eq:
        answer=sum(right_eq)-sum(left_eq)
    else:
        answer=sum(left_eq)-sum(right_eq)

    #giving answer(change the arithmetic sign if '-x')

    return -answer if minus else answer