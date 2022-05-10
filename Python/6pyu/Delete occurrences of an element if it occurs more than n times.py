'https://www.codewars.com/kata/554ca54ffa7d91b236000023'

def delete_nth(order,max_e):
    new_order=[]
    for index,x in enumerate(order):
        if order[0:index+1].count(x) > max_e:
            continue
        else:
            new_order.append(x)
    return new_order