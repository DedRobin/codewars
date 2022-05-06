'https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39'

def zero(x=0): return x if type(x)==int else x(0) 
def one(x=1): return x if type(x)==int else x(1) 
def two(x=2): return x if type(x)==int else x(2) 
def three(x=3): return x if type(x)==int else x(3) 
def four(x=4): return x if type(x)==int else x(4) 
def five(x=5): return x if type(x)==int else x(5) 
def six(x=6): return x if type(x)==int else x(6) 
def seven(x=7): return x if type(x)==int else x(7) 
def eight(x=8): return x if type(x)==int else x(8) 
def nine(x=9): return x if type(x)==int else x(9) 

def plus(right_operand):
    action=lambda left_operand: left_operand+right_operand
    return action
def minus(right_operand):
    action=lambda left_operand: left_operand-right_operand
    return action
def times(right_operand):
    action=lambda left_operand: left_operand*right_operand
    return action
def divided_by(right_operand):
    action=lambda left_operand: left_operand//right_operand
    return action

print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))