sent = input("Sentence:").split()
lkupwrd = str(input("What word do you want to look up?")).lower()

wordList = [word.lower() for word in sent]

if lkupwrd in wordList:
    print([i for i,j in enumerate(wordList) if j == lkupwrd])