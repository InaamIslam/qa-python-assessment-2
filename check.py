def four(string1, string2):
    s1 = list(string1)
    s2 = list(string2)
    s = list(s2)
    for i,a in enumerate(s1):
        s.insert(i*2,a)
    return s
    
testing = four("String","Fridge")
print(testing)
