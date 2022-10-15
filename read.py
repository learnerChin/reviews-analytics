data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print("總共讀取完了,總共",len(data),"筆資料")
print(data[0])

sum_len = 0
for d in data:
	sum_len += len(d)
print("留言平均長度為",sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("一共有",len(new),"筆資料,留言小於100")
print(new[1])

good = []
for d in data:
	if "good" in d:
		good.append(d)
print("一共有",len(good),"筆留言提到good")

good = [d for d in data if "good" in d]
bad = ["bad" in d for d in data]

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word ,wc[word])

print(len(wc))

while True:
	word = input("請輸入要查詢的字:")
	if word == "q":
		break
	if word in wc:
		print(word,"的次數為",wc[word])
	else:
		print("沒有這個字喔!")
		
print("感謝您使用本查詢功能")

