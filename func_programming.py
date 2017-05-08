def toUpper(arg):
    return arg.upper()
names = map(toUpper, ["test", "Mary", "TERRY", "kevin"])
print names

words = map(lambda x: x.upper(), ["test", "Mary", "TERRY", "kevin"])
print words

squares = map(lambda x: x * x, [1,3,5,7,9])
print squares

num = [1, -10, 5, -21, 16, -33, 14]
positive_num = filter(lambda x: x > 0, num)
avg = reduce(lambda x, y: x + y, positive_num) / len(positive_num)
print avg

tags = ["oscar", "epl", "presidentelection"]
tags = [t.upper() for t in tags]
print tags

tags = ["oscar", "epl", "presidentelection"]
upper_tages = map(lambda x: x.upper(), tags)
print upper_tages
