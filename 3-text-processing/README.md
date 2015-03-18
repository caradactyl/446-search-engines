# Assignment 3 - Text Processing

1.  Implement a text processing module as follows:

	Implement a tokenizer according to the following rules:
		Tokenize all abbreviations containing periods as strings without periods

		Treat the rest of the punctuation as word separators

		Lowercase all letters

		Don’t use software from the web for this.

	Implement a stemmer in one of two ways:
		Use the Porter Stemmer package: http://tartarus.org/~martin/PorterStemmer/

		Or implement the rules in textbook p. 92 Steps 1a & 1b

	Implement stopword removal using the following stopword list: http://bit.ly/1bqQWaV

2.   Run the tokenizer first, then the stopword removal, and finally the stemmer on the text provided in the input file assignment3-input.txt.

3.   Submission

	Submit the code for tokenizing, stopword removal, and stemming

	Report (pdf):

		The output of running the tokenizer, stopword removal, and stemmer in sequence on the provided text

		Based on your experience, discuss two changes you would make in the tokenization or stemming rules to improve the output