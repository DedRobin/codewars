'https://www.codewars.com/kata/57e1e61ba396b3727c000251'


def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join(list(filter(lambda x: False if x.isdigit() else True,list(s))))