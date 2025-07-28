def display(s,ind):
    if ind == -1:
        return
    print(s[ind])
    display(s,ind-1)


s='HELLO BACCHE'
display(s,len(s)-1)