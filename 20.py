# coding: utf-8
import json

search = u"イギリス"
f = open('jawiki-country.json', 'r') #ファイルの読み込み
t = open('england.txt', 'w')
for line in f:
	data = json.loads(line)
	if data['title'] == search:
		d = json.dumps(data, ensure_ascii=False)
		#print d.encode('utf-8')
		print >> t, d.encode('utf-8') #すいません、コマンドプロンプトで文字化けさせない方法がわかりませんでした
