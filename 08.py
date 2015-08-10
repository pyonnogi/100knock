# coding: utf-8
import re

text = "Danmitsu usually eat eroticisms as the center of the eating habits."
a = 0
res = ""
az = r"[a-z]" #正規表現
while a < len(text):
	c = text[a]
	i = ord(c)
	s = 219 - i
	mat = re.match(az, c)
	if mat:
		res += unichr(s)
	else:
		res += c
	a += 1
print res
