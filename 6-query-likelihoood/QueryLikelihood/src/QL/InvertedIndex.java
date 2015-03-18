package QL;

/**
 * 
 * @author Cara Magliozzi
 *
 * Creates an Inverted Index.
 */

import java.util.*;
import java.io.*;

public class InvertedIndex{
	
	// key = word, value = inverted list
	private Map<String, InvertedList> hm;
	
	// all words in a given document
	private ArrayList<String> words;
	
	// array to store document lengths
	int[] doclens;
	
	// to read in corpus
	private BufferedReader reader;
	// to write inverted index
	private BufferedWriter writer;

	// constructor
	public InvertedIndex()
	{
		hm = new HashMap<String, InvertedList>();
		doclens = new int[3204];
	}
		
	/**
	 * @param fileIn : corpus that the InvertedIndex is built from
	 * @param fileOut : text file that the InvertedIndex is written to
	 * @throws IOException
	 */
	public void createIndex(String fileIn, String fileOut) throws IOException
	{	
		int docid = 0;
		words = new ArrayList<String>();
		reader = new BufferedReader( new InputStreamReader(SearchEngine.class.getResourceAsStream(fileIn)) );
		writer = new BufferedWriter( new FileWriter(fileOut) );
		
		String line = reader.readLine();
		while (line != null) {
			// line contains docid
			if (line.startsWith("#")) {
				String[] theline = line.split(" ");
				docid = Integer.parseInt(theline[theline.length-1]);
				// get all words for a single document
				line = reader.readLine();
				while (line != null && !line.startsWith("#")) {
					for (String s: line.split(" ")) {
						words.add(s);
					}
					line = reader.readLine();	
				}	// words contains all words in a single document
				// length of document added to array
				doclens[docid-1] = words.size();
				for (String word: words) {
					InvertedList ilist = hm.get(word);
					if (ilist == null) {
						ilist = new InvertedList(word);
						hm.put(word, ilist);
					}
					ilist.add(docid, Collections.frequency(words, word));
				}
			}
			words.clear();	// clears words in list to prep for next document
		}
		writer.write(toString());
		reader.close();
		writer.close();
	}
	
	
	/**
	 * @param word in corpus
	 * @return inverted list corresponding to term
	 */
	public InvertedList getInvertedList( String word )
	{
		if (word == null)
			return null;
		else
			return hm.get(word);
	}
	
	/**
	 * @return total number of words in corpus
	 */
	public int totalWords() 
	{
		int sum = 0;
		for (int i : doclens) {
			sum += i;
		}
		return sum;
	}
	
	/**
	 * 
	 * @return the number of unique words in the corpus
	 */
	public int size() {
		return hm.size();
	}
	
	/**
	 * @return number of documents in corpus
	 */
	public int numberOfDocs()
	{
		return doclens.length;
	}
	
	/**
	 * @return array containing document lengths
	 */
	public int[] getDocLengths() 
	{
		return doclens;
	}
	
	public Map<String, InvertedList> getMap() {
		return hm;
	}
	
	/**
	 * @return string representation of InvertedIndex
	 */
	public String toString() 
	{
        StringBuilder sb = new StringBuilder();
        Iterator<Map.Entry<String, InvertedList>> it = hm.entrySet().iterator();
        while (it.hasNext()) {
        	Map.Entry<String, InvertedList> entry = it.next();
        	sb.append(entry.getKey()+"\t");			// term
        	sb.append(entry.getValue().toString());
        	sb.append("\n");
        }
        return sb.toString();
    }
}
