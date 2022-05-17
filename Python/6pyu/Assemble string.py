"""
Task
In this task, you need to restore a string from a list of its copies.

You will receive an array of strings. All of them are supposed to be the same as the original but, unfortunately, they were corrupted which means some of the characters were replaced with asterisks ("*").

You have to restore the original string based on non-corrupted information you have. If in some cases it is not possible to determine what the original character was, use "#" character as a special marker for that.

If the array is empty, then return an empty string.

Examples:
input = [
  "a*cde",
  "*bcde",
  "abc*e"
]
result = "abcde"


input = [
  "a*c**",
  "**cd*",
  "a*cd*"
]
result = "a#cd#"
"""


def assemble(arr):
    print(arr)
    temp = []
    if arr == []:
        return ""
    while len(arr) != 1:
        for index, letter in enumerate(arr.pop(0)):
            if letter == "*" and arr[0][index] == "*":
                temp.append("*")
            elif letter != "*" and arr[0][index] == "*":
                temp.append(letter)
            elif letter == "*" and arr[0][index] != "*":
                temp.append(arr[0][index])
            else:
                temp.append(letter)
        arr[0] = "".join(temp)
        temp = []
        if "*" not in arr[0]:
            return arr[0]
    else:
        return arr[0].replace("*", "#")
