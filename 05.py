# coding: utf-8
import re

text = "I am an NLPer"

def ngram(doc,n): #doc:文書, n:区切り値
	a = 0
	result_t = {}
	words = filter(lambda w: len(w) > 0, re.split(r"\s|,|\.",doc))
	print u"単語","-",n,"gram:"
	#print words
	while a < len(words):
		tg = words[a]
		b = 1
		while b < n:
			if a + b < len(words):
				tb = words[a + b]
				tg += "-" + tb
			else:
				tb = "(.)"
				tg += "-" + tb
			b += 1
		if result_t.has_key(tg): # has_keyで辞書内にキーがあるか確認できる
			result_t[tg] = result_t[tg] + 1
		else:
			result_t[tg] = 1
		a += 1
	print result_t

	result = {}
	a = 0
	lit = ""
	while a < len(words):
		lit += words[a]
		a += 1
	print u"文字","-",n,"gram:"
	print lit
	a = 0
	while a < len(lit):
		tg = lit[a:a+n]
		if result.has_key(tg): # has_keyで辞書内にキーがあるか確認できる
			result[tg] = result[tg] + 1
		else:
			result[tg] = 1
		a += 1

	print result

ngram(text,2)