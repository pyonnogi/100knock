# coding: utf-8

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = text.split()

a = 0
list1 = []
while a < len(words):
	t1 = words[a]
	t2 = t1.split(",")
	t3 = t2[0]
	t4 = t3.split(".")
	num = len(t4[0])
	list1.append(num)
	a += 1
print list1