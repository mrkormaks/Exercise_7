def WordSearch(length, s, subs):
	resultList = []
	word = ''
	comparisonList = ''
	wordsList = []
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

		if s[length] == ' ':
			word = s[:length]

		wordsList.append(word)

		if word in s:
			s = s.replace(word, '')
		if s[0] == ' ':
			s = s[1:]

	wordsList.append(s)

	for i in range(len(wordsList)):
		comparisonList = wordsList[i].split()

		for j in range(len(comparisonList)):
			if comparisonList[j] == subs:
				subsWasFound = True

		if subsWasFound:
			resultList.append(1)
		else:
			resultList.append(0)
		subsWasFound = False

	return(resultList)
