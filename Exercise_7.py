def WordSearch(length, s, subs):
	resultList = []
	word = ''
	wordsList = []
	count = 0

	for i in range(len(s)):
		if count < length:
			if s[i] == ' ':
				#word += s[i]
				count = 0
				wordsList.append(word)
				word = ''
			else:
				word += s[i]
				count += 1
		else:
			if s[i] == ' ':
				#word += s[i]
				wordsList.append(word)
				word = ''
				count = 0
			else:
				wordsList.append(word)
				word = s[i]
				count = 1
	wordsList.append(word)

	for i in range(len(wordsList)):
		if subs == wordsList[i]:
			resultList.append(1)
		else:
			resultList.append(0)

	#print(wordsList)

	return(resultList)
