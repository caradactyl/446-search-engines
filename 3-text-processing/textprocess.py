# Cara Magliozzi, Spring 2014

import string
from porterstemmer import PorterStemmer

# used 3 separate lists to check correctness at each step

tokens = []			# list tokenized
stemmed = []		# list tokenized and stemmed
nostopwords = []	# list tokenized, stemmed, and stopwords removed

# list of provided stopwords
stopwords = ['a', 'about', 'above', 'according', 'across', 'after', 'afterwards', 'again', 'against', 'albeit', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'apart', 'are', 'around', 'as', 'at', 'av', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both', 'but', 'by', 'can', 'cannot', 'canst', 'certain', 'cf', 'choose', 'contrariwise', 'cos', 'could', 'cu', 'day', 'do', 'does', "doesn't", 'doing', 'dost', 'doth', 'double', 'down', 'dual', 'during', 'each', 'either', 'else', 'elsewhere', 'enough', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'except', 'excepted', 'excepting', 'exception', 'exclude', 'excluding', 'exclusive', 'far', 'farther', 'farthest', 'few', 'ff', 'first', 'for', 'formerly', 'forth', 'forward', 'from', 'front', 'further', 'furthermore', 'furthest', 'get', 'go', 'had', 'halves', 'hardly', 'has', 'hast', 'hath', 'have', 'he', 'hence', 'henceforth', 'her', 'here', 'hereabouts', 'hereafter', 'hereby', 'herein', 'hereto', 'hereupon', 'hers', 'herself', 'him', 'himself', 'hindmost', 'his', 'hither', 'hitherto', 'how', 'however', 'howsoever', 'i', 'ie', 'if', 'in', 'inasmuch', 'inc', 'include', 'included', 'including', 'indeed', 'indoors', 'inside', 'insomuch', 'instead', 'into', 'inward', 'inwards', 'is', 'it', 'its', 'itself', 'just', 'kind', 'kg', 'km', 'last', 'latter', 'latterly', 'less', 'lest', 'let', 'like', 'little', 'ltd', 'many', 'may', 'maybe', 'me', 'meantime', 'meanwhile', 'might', 'moreover', 'most', 'mostly', 'more', 'mr', 'mrs', 'ms', 'much', 'must', 'my', 'myself', 'namely', 'need', 'neither', 'never', 'nevertheless', 'next', 'no', 'nobody', 'none', 'nonetheless', 'noone', 'nope', 'nor', 'not', 'nothing', 'notwithstanding', 'now', 'nowadays', 'nowhere', 'of', 'off', 'often', 'ok', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'own', 'per', 'perhaps', 'plenty', 'provide', 'quite', 'rather', 'really', 'round', 'said', 'sake', 'same', 'sang', 'save', 'saw', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'seldom', 'selves', 'sent', 'several', 'shalt', 'she', 'should', 'shown', 'sideways', 'since', 'slept', 'slew', 'slung', 'slunk', 'smote', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'spake', 'spat', 'spoke', 'spoken', 'sprang', 'sprung', 'stave', 'staves', 'still', 'such', 'supposing', 'than', 'that', 'the', 'thee', 'their', 'them', 'themselves', 'then', 'thence', 'thenceforth', 'there', 'thereabout', 'thereabouts', 'thereafter', 'thereby', 'therefore', 'therein', 'thereof', 'thereon', 'thereto', 'thereupon', 'these', 'they', 'this', 'those', 'thou', 'though', 'thrice', 'through', 'throughout', 'thru', 'thus', 'thy', 'thyself', 'till', 'to', 'together', 'too', 'toward', 'towards', 'ugh', 'unable', 'under', 'underneath', 'unless', 'unlike', 'until', 'up', 'upon', 'upward', 'upwards', 'us', 'use', 'used', 'using', 'very', 'via', 'vs', 'want', 'was', 'we', 'week', 'well', 'were', 'what', 'whatever', 'whatsoever', 'when', 'whence', 'whenever', 'whensoever', 'where', 'whereabouts', 'whereafter', 'whereas', 'whereat', 'whereby', 'wherefore', 'wherefrom', 'wherein', 'whereinto', 'whereof', 'whereon', 'wheresoever', 'whereto', 'whereunto', 'whereupon', 'wherever', 'wherewith', 'whether', 'whew', 'which', 'whichever', 'whichsoever', 'while', 'whilst', 'whither', 'who', 'whoa', 'whoever', 'whole', 'whom', 'whomever', 'whomsoever', 'whose', 'whosoever', 'why', 'will', 'wilt', 'with', 'within', 'without', 'worse', 'worst', 'would', 'wow', 'ye', 'yet', 'year', 'yippee', 'you', 'your', 'yours', 'yourself', 'yourselves']

# step 1
def tokenize(line):
	# strings with periods --> strings without periods
	no_periods = line.replace('.','')
	# make all remaining punctuation whitespace with translation table
	replace = string.maketrans(string.punctuation, ' '*len(string.punctuation))
	# split line by whitespace (consecutive whitespace acts as single sep), and add tokens to list
	tokens.extend(line.lower().translate(replace).split())
	return

# step 2
def runStemmer():
	p = PorterStemmer()
	# run through tokenized list
	for word in tokens:
		stemmed.append(p.stem(word, 0, len(word)-1))
	return

# step 3
def removeStopwords():
	# run through tokenized and stemmed list
	for word in stemmed:
		if word not in stopwords:
			nostopwords.append(word)
	return

# method for testing stopword removal at different steps
def countStopwords(alist):
	ct = 0
	for word in alist:
		if word in stopwords:
			ct+=1
	return ct

if __name__ == '__main__':
	with open('input.txt', 'r') as filein:
		for line in filein:
			tokenize(line)

		print '\ntokenized:\n', ' '.join(tokens)
		print '\n# of stopwords counted = ', countStopwords(tokens)
		
		runStemmer()
		print '\ntokenized & stemmed:\n', ' '.join(stemmed)
		print '\n# of stopwords counted = ', countStopwords(stemmed)
		
		removeStopwords()
		print '\ntokenized, stemmed, & stopwords removed:\n', ' '.join(nostopwords)
		print '\n# of stopwords counted = ', countStopwords(nostopwords)