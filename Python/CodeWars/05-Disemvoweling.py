vowels = ['A', 'E', 'I', 'O', 'U','a', 'e', 'i', 'o', 'u']
word2 = []
word = input()

for i in word:
	word2.append(i)

for x in word2:
	if x in vowels:
		index = word2.index(x)
		word2.remove(x)
		word2.insert(index, '*')
	else:
		continue

print(''.join(word2))