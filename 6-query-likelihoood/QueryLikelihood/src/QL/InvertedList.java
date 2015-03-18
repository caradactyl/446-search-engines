package QL;

/**
 * 
 * @author Cara Magliozzi
 *
 * Stores (docid, term frequency) for a given word.
 * Modified to use an ArrayList instead of a HashMap.
 */

import java.util.*;


public class InvertedList {
		
	private String word;
	ArrayList<int[]> list;	// (docid, term frequency)
	
	/**
	 * constructor
	 * @param word : term for which the list is made
	 */
	public InvertedList( String word ) {
		this.word = word;
		list = new ArrayList<int[]>();
	}
	
	/**
	 * 
	 * @return the term for which the list is about
	 */
	public String getWord() {
		return word;
	}
	
	/**
	 * 
	 * @param docid : document id
	 * @param tf : term frequency
	 * @return false if (docid, tf) already exists in list, true otherwise
	 */
	public boolean add( int docid, int tf ) {
		int[] pair = new int[] {docid, tf};
		for (int[] i : list) {
			if (Arrays.equals(pair, i))
				return false;
		}
		list.add(pair);
		return true;
	}
	
	/**
	 * sorts the underlying ArrayList
	 */
	public void sort() {
		Collections.sort(list, new Comparator<int[]>() {
			public int compare(int[] docidA, int[] docidB) {
	                return Integer.valueOf(docidA[0]).compareTo(Integer.valueOf(docidB[0]));
	            }
	        });
	}
	
	/**
	 * 
	 * @return list of document ids containing the term
	 */
	public ArrayList<Integer> getDocIDs() {
		ArrayList<Integer> docids = new ArrayList<Integer>();
		for (int[] entry : list) {
			docids.add(entry[0]);
		}
		return docids;
	}
	
	/**
	 * get the term frequency given a document id
	 * @param docid
	 * @return term frequency for a given docid, 0 if doc doesn't contain the term
	 */
	public int getTF(int docid) {
		for (int[] i : list) {
			if (i[0] == docid)
				return i[1];
		}
		return 0;
	}
	
	/**
	 * 
	 * @param docid
	 * @return true if the term is in the given document, false otherwise
	 */
	public boolean containsDocID(int docid) {
		for (int[] i : list) {
			if (i[0] == docid)
				return true;
		}
		return false;
	}
 
	/**
	 * calculates number of word occurrences in collection.
	 * @return sum of term frequencies
	 */
	public int totalFrequency() {
		int total = 0;
		for (int[] i: list) {
			total += i[1];
		}
		return total;
	}
	
	/**
	 * 
	 * @return the size of the InvertedList
	 */
	public int size() {
		return list.size();
	}
	
	/**
	 * @return the string representation of the InvertedList
	 */
	public String toString() {
		sort();
		StringBuilder sb = new StringBuilder();
		for (int[] i : list) {
			sb.append("("+i[0]+","+i[1]+") ");
		}
		return sb.toString();
	}
}