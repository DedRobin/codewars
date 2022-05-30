# https://www.codewars.com/kata/598106cb34e205e074000031
def count_deaf_rats(town):
    # Clean string from whitespaces.
    town = town.replace(" ", "")

    counter = 0  # It's our counter of dear rats.

    # We will compare every rat with rat pattern(dear rat).
    # When we meet Pied Piper rat pattern is changed.
    for rat_pattern in ("O~", "~O"):

        rat = ""  # it's rat for comparing

        # Variable "location" need to slice string "town"
        # when we meet signer Pied Piper.
        for location, piece_of_rat in enumerate(town):
            rat += piece_of_rat
            if rat == rat_pattern:
                counter += 1
                rat = ""
            elif len(rat) >= 2:
                rat = ""
            elif piece_of_rat == "P":  # We meet Pied Piper.
                town = town[location + 1:]
                break

    return counter


"""
This code for optimization:

def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')
"""

if __name__ == "__main__":
    print(count_deaf_rats("~O~O~O~O P"))  # 0
    print(count_deaf_rats("P O~ O~ ~O O~"))  # 1
    print(count_deaf_rats("~O~O~O~OP~O~OO~"))  # 2
