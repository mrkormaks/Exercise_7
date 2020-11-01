def WordSearch(length, s, subs):
	resultList = []
	word = ''
	subWord = ''
	wordsList = []
	count = 0
	subsWasFound = False

	while (len(s) > length):
		lastSpaceIndex = 0
		if s[length-1] != ' ':
			for i in range(length):
				if s[i] == ' ':
					lastSpaceIndex = i
			if lastSpaceIndex > 0:
				word = s[:lastSpaceIndex]
			else:
				word = s[:length]
		else:
			word = s[:length]

		wordsList.append(word)

		if word in s:
			s = s.replace(word, '')
		if s[0] == ' ':
			s = s[1:]

	wordsList.append(s)

	for i in range(len(wordsList)):
		subWord = wordsList[i].split()

		for j in range(len(subWord)):
			if subWord[j] == subs:
				subsWasFound = True

		if subsWasFound:
			resultList.append(1)
		else:
			resultList.append(0)
		subsWasFound = False

	return(resultList)
