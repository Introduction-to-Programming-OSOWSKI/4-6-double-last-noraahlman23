def doubleLast(j):
    j.append(j[len(j)-1])
    return j

print (doubleLast(["cat", "dog", "bird", "squirrel"]))