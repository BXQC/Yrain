def break_words(stuff):
	'''这个函数是用来返回单词给我们的'''
	words = stuff.split(' ')
	return(words)

def sort_words(words):
	'''这个函数是用来适应单词的'''
	return(sorted(words))

def print_first_word(words):
	'''输出第一个单词'''
	word = words.pop(0)
	print(word)

def print_last_word(words):
	'''输出最后一个单词'''
	word = words.pop(-1)
	print(word)

def sort_sentence(sentence):
	'''由完整的句子分出每一个单词'''
	words = break_words(sentence)
	return(sort_words(words))

def print_first_and_last(sentence):
	'''用来输出第一个和最后一个单词'''
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	'''输出适应好的最后一个和第一个单词'''
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

