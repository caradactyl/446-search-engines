# test textprocess.py output for correctness

toke = ['early', 'examples', 'of', 'abbreviation', 'in', 'english', 'source', 'http', 'en', 'wikipedia', 'org', 'wiki', 'acronym', 'and', 'initialism', '1', 'the', 'use', 'of', 'latin', 'and', 'neo', 'latin', 'terms', 'in', 'vernaculars', 'has', 'been', 'pan', 'european', 'and', 'predates', 'modern', 'english', 'some', 'examples', 'of', 'initialisms', 'in', 'this', 'class', 'are', 'a', 'a', 'm', 'from', 'latin', 'ante', 'meridiem', 'before', 'noon', 'and', 'p', 'm', 'from', 'latin', 'post', 'meridiem', 'after', 'noon', 'b', 'a', 'd', 'from', 'latin', 'anno', 'domini', 'in', 'the', 'year', 'of', 'our', 'lord', 'whose', 'complement', 'in', 'english', 'b', 'c', 'is', 'english', 'sourced', '2', 'o', 'k', 'a', 'term', 'of', 'disputed', 'origin', 'dating', 'back', 'at', 'least', 'to', 'the', 'early', '19th', 'century', 'now', 'used', 'around', 'the', 'world', '3', 'n', 'g', 'for', 'no', 'good', 'from', '1838', 'nowadays', 'commonly', 'expanded', 'to', 'n', 'b', 'g', 'no', 'bloody', 'good', '4', 'the', 'etymology', 'of', 'the', 'word', 'alphabet', 'itself', 'comes', 'to', 'middle', 'english', 'from', 'the', 'late', 'latin', 'alphabetum', 'which', 'in', 'turn', 'derives', 'from', 'the', 'ancient', 'greek', 'alphabetos', 'from', 'alpha', 'and', 'beta', 'the', 'first', 'two', 'letters', 'of', 'the', 'greek', 'alphabet', 'colloquially', 'learning', 'the', 'alphabet', 'is', 'called', 'learning', 'one', 's', 'a', 'b', 'c', 's']
toke_stem = ['earli', 'exampl', 'of', 'abbrevi', 'in', 'english', 'sourc', 'http', 'en', 'wikipedia', 'org', 'wiki', 'acronym', 'and', 'initi', '1', 'the', 'us', 'of', 'latin', 'and', 'neo', 'latin', 'term', 'in', 'vernacular', 'ha', 'been', 'pan', 'european', 'and', 'predat', 'modern', 'english', 'some', 'exampl', 'of', 'initi', 'in', 'thi', 'class', 'ar', 'a', 'a', 'm', 'from', 'latin', 'ant', 'meridiem', 'befor', 'noon', 'and', 'p', 'm', 'from', 'latin', 'post', 'meridiem', 'after', 'noon', 'b', 'a', 'd', 'from', 'latin', 'anno', 'domini', 'in', 'the', 'year', 'of', 'our', 'lord', 'whose', 'complement', 'in', 'english', 'b', 'c', 'is', 'english', 'sourc', '2', 'o', 'k', 'a', 'term', 'of', 'disput', 'origin', 'date', 'back', 'at', 'least', 'to', 'the', 'earli', '19th', 'centuri', 'now', 'us', 'around', 'the', 'world', '3', 'n', 'g', 'for', 'no', 'good', 'from', '1838', 'nowadai', 'commonli', 'expand', 'to', 'n', 'b', 'g', 'no', 'bloodi', 'good', '4', 'the', 'etymolog', 'of', 'the', 'word', 'alphabet', 'itself', 'come', 'to', 'middl', 'english', 'from', 'the', 'late', 'latin', 'alphabetum', 'which', 'in', 'turn', 'deriv', 'from', 'the', 'ancient', 'greek', 'alphabeto', 'from', 'alpha', 'and', 'beta', 'the', 'first', 'two', 'letter', 'of', 'the', 'greek', 'alphabet', 'colloqui', 'learn', 'the', 'alphabet', 'is', 'call', 'learn', 'on', 's', 'a', 'b', 'c', 's']
toke_stem_stop = ['earli', 'exampl', 'abbrevi', 'english', 'sourc', 'http', 'en', 'wikipedia', 'org', 'wiki', 'acronym', 'initi', '1', 'latin', 'neo', 'latin', 'term', 'vernacular', 'ha', 'pan', 'european', 'predat', 'modern', 'english', 'exampl', 'initi', 'thi', 'class', 'ar', 'm', 'latin', 'ant', 'meridiem', 'befor', 'noon', 'p', 'm', 'latin', 'post', 'meridiem', 'noon', 'b', 'd', 'latin', 'anno', 'domini', 'lord', 'complement', 'english', 'b', 'c', 'english', 'sourc', '2', 'o', 'k', 'term', 'disput', 'origin', 'date', 'back', 'least', 'earli', '19th', 'centuri', 'world', '3', 'n', 'g', 'good', '1838', 'nowadai', 'commonli', 'expand', 'n', 'b', 'g', 'bloodi', 'good', '4', 'etymolog', 'word', 'alphabet', 'come', 'middl', 'english', 'late', 'latin', 'alphabetum', 'turn', 'deriv', 'ancient', 'greek', 'alphabeto', 'alpha', 'beta', 'two', 'letter', 'greek', 'alphabet', 'colloqui', 'learn', 'alphabet', 'call', 'learn', 's', 'b', 'c', 's']
toke_stop = ['early', 'examples', 'abbreviation', 'english', 'source', 'http', 'en', 'wikipedia', 'org', 'wiki', 'acronym', 'initialism', '1', 'use', 'latin', 'neo', 'latin', 'terms', 'vernaculars', 'been', 'pan', 'european', 'predates', 'modern', 'english', 'examples', 'initialisms', 'this', 'class', 'm', 'latin', 'ante', 'meridiem', 'noon', 'p', 'm', 'latin', 'post', 'meridiem', 'noon', 'b', 'd', 'latin', 'anno', 'domini', 'lord', 'complement', 'english', 'b', 'c', 'english', 'sourced', '2', 'o', 'k', 'term', 'disputed', 'origin', 'dating', 'back', 'least', 'early', '19th', 'century', 'used', 'world', '3', 'n', 'g', 'good', '1838', 'commonly', 'expanded', 'n', 'b', 'g', 'no', 'bloody', 'good', '4', 'the', 'etymology', 'the', 'word', 'alphabet', 'comes', 'middle', 'english', 'the', 'late', 'latin', 'alphabetum', 'in', 'turn', 'derives', 'the', 'ancient', 'greek', 'alphabetos', 'alpha', 'beta', 'the', 'first', 'two', 'letters', 'of', 'the', 'greek', 'alphabet', 'colloquially', 'learning', 'the', 'alphabet', 'called', 'learning', 's', 'a', 'b', 'c', 's']
stopwords = ['a', 'about', 'above', 'according', 'across', 'after', 'afterwards', 'again', 'against', 'albeit', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'apart', 'are', 'around', 'as', 'at', 'av', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both', 'but', 'by', 'can', 'cannot', 'canst', 'certain', 'cf', 'choose', 'contrariwise', 'cos', 'could', 'cu', 'day', 'do', 'does', "doesn't", 'doing', 'dost', 'doth', 'double', 'down', 'dual', 'during', 'each', 'either', 'else', 'elsewhere', 'enough', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'except', 'excepted', 'excepting', 'exception', 'exclude', 'excluding', 'exclusive', 'far', 'farther', 'farthest', 'few', 'ff', 'first', 'for', 'formerly', 'forth', 'forward', 'from', 'front', 'further', 'furthermore', 'furthest', 'get', 'go', 'had', 'halves', 'hardly', 'has', 'hast', 'hath', 'have', 'he', 'hence', 'henceforth', 'her', 'here', 'hereabouts', 'hereafter', 'hereby', 'herein', 'hereto', 'hereupon', 'hers', 'herself', 'him', 'himself', 'hindmost', 'his', 'hither', 'hitherto', 'how', 'however', 'howsoever', 'i', 'ie', 'if', 'in', 'inasmuch', 'inc', 'include', 'included', 'including', 'indeed', 'indoors', 'inside', 'insomuch', 'instead', 'into', 'inward', 'inwards', 'is', 'it', 'its', 'itself', 'just', 'kind', 'kg', 'km', 'last', 'latter', 'latterly', 'less', 'lest', 'let', 'like', 'little', 'ltd', 'many', 'may', 'maybe', 'me', 'meantime', 'meanwhile', 'might', 'moreover', 'most', 'mostly', 'more', 'mr', 'mrs', 'ms', 'much', 'must', 'my', 'myself', 'namely', 'need', 'neither', 'never', 'nevertheless', 'next', 'no', 'nobody', 'none', 'nonetheless', 'noone', 'nope', 'nor', 'not', 'nothing', 'notwithstanding', 'now', 'nowadays', 'nowhere', 'of', 'off', 'often', 'ok', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'own', 'per', 'perhaps', 'plenty', 'provide', 'quite', 'rather', 'really', 'round', 'said', 'sake', 'same', 'sang', 'save', 'saw', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'seldom', 'selves', 'sent', 'several', 'shalt', 'she', 'should', 'shown', 'sideways', 'since', 'slept', 'slew', 'slung', 'slunk', 'smote', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'spake', 'spat', 'spoke', 'spoken', 'sprang', 'sprung', 'stave', 'staves', 'still', 'such', 'supposing', 'than', 'that', 'the', 'thee', 'their', 'them', 'themselves', 'then', 'thence', 'thenceforth', 'there', 'thereabout', 'thereabouts', 'thereafter', 'thereby', 'therefore', 'therein', 'thereof', 'thereon', 'thereto', 'thereupon', 'these', 'they', 'this', 'those', 'thou', 'though', 'thrice', 'through', 'throughout', 'thru', 'thus', 'thy', 'thyself', 'till', 'to', 'together', 'too', 'toward', 'towards', 'ugh', 'unable', 'under', 'underneath', 'unless', 'unlike', 'until', 'up', 'upon', 'upward', 'upwards', 'us', 'use', 'used', 'using', 'very', 'via', 'vs', 'want', 'was', 'we', 'week', 'well', 'were', 'what', 'whatever', 'whatsoever', 'when', 'whence', 'whenever', 'whensoever', 'where', 'whereabouts', 'whereafter', 'whereas', 'whereat', 'whereby', 'wherefore', 'wherefrom', 'wherein', 'whereinto', 'whereof', 'whereon', 'wheresoever', 'whereto', 'whereunto', 'whereupon', 'wherever', 'wherewith', 'whether', 'whew', 'which', 'whichever', 'whichsoever', 'while', 'whilst', 'whither', 'who', 'whoa', 'whoever', 'whole', 'whom', 'whomever', 'whomsoever', 'whose', 'whosoever', 'why', 'will', 'wilt', 'with', 'within', 'without', 'worse', 'worst', 'would', 'wow', 'ye', 'yet', 'year', 'yippee', 'you', 'your', 'yours', 'yourself', 'yourselves']
intersect = []
nostopwords = []

def textprocesstest():
	print '\nlength of toke = ',len(toke)
	print 'length of toke_stop = ', len(toke_stop), '\n'

	found = []
	for word in toke:
		if word in stopwords:
			found.append(word)
		if word in toke_stop:
			intersect.append(word)
	print "# that were removed: ", len(toke)-len(intersect)
	print ' '.join(intersect)

	print '\nstopwords found: ', len(found), '\n', ' '.join(found)


def removestopword():
	same = 0
	intersect[:] = []
	for word in toke_stop:
		if word not in stopwords:
			nostopwords.append(word)
	for word in nostopwords:
		if word in toke_stop:
			intersect.append(word)
	print '\nmissed ', len(toke_stop)-len(nostopwords), ' stopwords'
	print 'missing stopwords: ', '\n', ' '.join(nostopwords)

def comparison():
	tct = 0
	for word in toke:
		if word in stopwords:
			tct+=1
	sct = 0
	for word in toke:
		if word in stopwords:
			sct+=1
	print '\nlength of toke = ',len(toke)
	print '# of stopwords found before stem = ', tct
	print 'length of toke_stem = ', len(toke_stem)
	print '# of stopwords found after stem = ', sct
	print 'length of toke_stem_stop = ', len(toke_stem_stop), '\n'



if __name__ == '__main__':
	comparison()
