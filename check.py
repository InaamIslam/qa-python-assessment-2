def six(string):
    if string[-2:] == "py":
        return True
    else:
        return False

testing = six("welovepyforreal")
print(testing)
