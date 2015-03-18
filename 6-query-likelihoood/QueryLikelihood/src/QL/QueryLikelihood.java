package QL;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

/**
 * 
 * @author Cara Magliozzi
 *
 * Computes query likelihood using Dirichlet Smoothing.
 */

/*
 * Change the BM25 formula to Query Likelihood with Dirichlet smoothing
 * tf, dlen are the same as in the case of BM25. 
 * (In the lecture note for language modeling: tf = fqi,d and dlen=|D|.)
 * In addition, you need cqi and |C| (see lecture note for what they are)
 * Can be calculated with just one-pass over all terms in all documents
 * Could be done during the indexing step
 * cqi can be stored in a Hash table.
 * 
 * Vary mu from {10, 100, 200, 500, 1000, 2000, 2500, 3000, 5000}
 */

public class QueryLikelihood {

	String query;
	String[] terms;
	int[] doclens;
	int queryid;
	int mu;
	InvertedIndex ii;
	private Map<Integer, Double> scores;
	private List<Map.Entry<Integer, Double>> sorted;
	
	public QueryLikelihood() {
		
	}
		
	public QueryLikelihood (InvertedIndex ii, int[] doclens, String query, int queryid, int mu) 
	{
		this.ii = ii;
		this.doclens = doclens;
		this.query = query;
		this.queryid = queryid;
		this.mu = mu;
		terms = query.split(" ");
		scores = new HashMap<Integer, Double>();
	}
	
	/**
	 * creates map from InvertedIndex in a file
	 * @param fileIn : file containing InvertedIndex
	 * @throws IOException
	 */
	public static InvertedIndex loadIndex(String fileIn) throws IOException {
		InvertedIndex inv = new InvertedIndex();
		BufferedReader reader = new BufferedReader( new InputStreamReader(SearchEngine.class.getResourceAsStream(fileIn)));
		String line = reader.readLine();
		while (line != null) {
			line = line.replaceAll("\\(|,|\\)", " ");
			String[] arr = line.split("\\s+");
			InvertedList ilist = new InvertedList(arr[0]);
			for (int i = 1; i < arr.length; i=i+2) {
				ilist.add(Integer.parseInt(arr[i]), Integer.parseInt(arr[i+1]));
			}
			inv.getMap().put(arr[0], ilist);
			line = reader.readLine();
		}
		reader.close();
		return inv;
	}

	/**
	 * QL(Q,D) = SUM from i=0 to n [ log (fqiD + mu * (cqi/Clen))/(doclen + mu) ]
	 * need to calculate the QL even when the tf is 0 for a given document
	 */
	public void scores() 
	{
		int fqiD;						// term frequency for a document
		int cqi;						// number of given word occurrences in collection
		int Clen = 0;
		HashSet<Integer> docSet = new HashSet<Integer>();
		ArrayList<Integer> docList = new ArrayList<Integer>();
		for (int i : doclens) {
			Clen += i;					// total number of words in collection
		}

		// make a list of docid containing at least one term of the query
		for (String term : terms) {
			docSet.addAll(ii.getInvertedList(term).getDocIDs());
		}
		docList.addAll(docSet);
		Collections.sort(docList);
			
		// for each of the documents containing at least one query term
		for (Integer docid : docList) {
			// for each of the terms in the query
			double score = 0;
			for (String term : terms) {
				InvertedList ilist = ii.getInvertedList(term);
				// compute the QL
				fqiD = ilist.getTF(docid);
				cqi = ilist.totalFrequency();
				double numerator = fqiD + mu * (cqi/Clen);
				double denominator = doclens[docid-1] + mu;
				if ((numerator / denominator) > 0)
					score += Math.log(numerator/denominator);
			}
			scores.put(docid, score);		
		}
	}
	
	public void sort() {
		sorted = new ArrayList<Map.Entry<Integer, Double>>(scores.entrySet());
		Collections.sort(sorted, new RankCompare());
	}
	
	// calls compareTo for BigDecimal
	public int compareTo(Double o) {
		return this.compareTo(o);
	}
	
	private class RankCompare implements Comparator<Map.Entry<Integer, Double>> {
		
		public int compare(Map.Entry<Integer, Double> e1, Map.Entry<Integer, Double> e2) {
			Double v1 = e1.getValue();
			Double v2 = e2.getValue();
			
			return v2.compareTo(v1);
		}
	}
	
	// format: query_id Q0 doc_id rank QL_score system_name
	public String toString() {
        StringBuilder sb = new StringBuilder();
        int rank = 1;
        for (Map.Entry<Integer, Double> entry : sorted) {
        	if (rank > 10)
        		break;
        	sb.append(queryid+" Q0 ");			// query_id Q0
            sb.append(entry.getKey()+" ");		// doc_id
            sb.append(rank+" ");				// rank
            sb.append(entry.getValue());		// QL_score
            sb.append(" Cara\r");				// system_name
            rank += 1;
        }
        return sb.toString();
    }


}

