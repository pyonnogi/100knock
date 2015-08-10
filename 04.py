# coding: utf-8

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = text.split()

a = 0
genso = {}

while a < len(words):
	word = words[a]
	if a == 0 or a == 4 or a == 5 or a == 6 or a == 7 or a == 8 or a == 14 or a == 15 or a == 18:
		w = word[0]
	else:
		w1 = word[0]
		w2 = word[1]
		w = w1 + w2
	genso[a] = w
	a += 1

print genso