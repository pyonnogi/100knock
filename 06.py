# coding: utf-8
import re

text1 = "paraparaparadise"
text2 = "paragraph"
x = []
y = []

def ngram(doc,n,k):
	words = filter(lambda w: len(w) > 0, re.split(r"\s|,|\.",doc))
	result = {}
	a = 0
	lit = ""
	while a < len(words):
		lit += words[a]
		a += 1
	#print "moji","-",n,"gram:"
	#print lit
	a = 0
	while a < len(lit):
		tg = lit[a:a+n]
		if result.has_key(tg): # has_keyで辞書内にキーがあるか確認できる
			result[tg] = result[tg] + 1
		else:
			result[tg] = 1
		a += 1
	k += result.keys()

ngram(text1,2,x)
print "X:", x
ngram(text2,2,y)
print "Y:", y

#和集合
wa = list(set(x + y))
print u"和集合:", wa

#積集合
a = 0
seki = []
while a < len(x):
	if x[a] in y:
		seki.append(x[a])
	a += 1
print u"積集合:", seki

#差集合
a = 0
x1 = x
y1 = y
while a < len(seki):
	if seki[a] in x1:
		x1.remove(seki[a])
	if seki[a] in y1:
		y1.remove(seki[a])
	a += 1
print u"Xの差集合:", x1
print u"Yの差集合:", y1

print u'"se" はXおよびYに含まれるか:', "se" in seki
