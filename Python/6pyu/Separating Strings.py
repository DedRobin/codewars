#https://www.codewars.com/kata/5977ef1f945d45158d00011f

def sep_str(st):
    st=[list(x) for x in st.split()]
    max_lenght=max([len(row) for row in st])
    for x in st:
        if len(x)<max_lenght:
            x.extend(['']*(max_lenght-len(x)))
    new_st=[]
    for column in range(max_lenght):
        new_st.append([row[column] for row in st])
    return new_st