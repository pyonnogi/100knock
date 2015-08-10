# coding: utf-8
import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = text.split()

a = 0
res = ""
while a < len(words):
	w = words[a]
	if len(w) >= 5:
		b = w[1:-1]
		listb = list(b)
		random.shuffle(listb)
		texb = "".join(listb)
		bond = w[0] + texb + w[-1]
		res += bond.ljust(len(bond)+1) #l.just()　左寄せ
	else:
		res += w.ljust(len(w)+1)
	a += 1

print res