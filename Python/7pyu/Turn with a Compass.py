'https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2'

def direction(facing, turn):
    facings_and_degrees={'N': 0,
                        'NE': 45,
                        'E': 90,
                        'SE': 135,
                        'S': 180,
                        'SW': 225,
                        'W': 270,
                        'NW': 315}
    new_degree=facings_and_degrees[facing]+turn
    if 0>new_degree or new_degree>=360:
        return [x[0] for x in facings_and_degrees.items() if x[1]==new_degree%360][0]
    elif 0<=new_degree<360:
        return [x[0] for x in facings_and_degrees.items() if x[1]==new_degree][0]
    
print(direction('N',360))