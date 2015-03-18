package QL;

/**
 * 
 * @author Cara Magliozzi
 *
 */

import java.io.*;

public class SearchEngine {

	public static void main(String[] args) throws IOException
	{
		// step 1 : generate InvertedIndex and save it to a file
		InvertedIndex ii = new InvertedIndex();
		ii.createIndex("tccorpus.txt", "invertedindex.txt");
		System.out.println("Inverted index generated and written to invertedindex.txt.");
		
		// step 2: load InvertedIndex from file and calculate the QueryLikelihood for each query
		// generate top 10 document ids and their QL for each test query
		// one run file per mu value containing top 10 docs for all queries
		// InvertedIndex inv = QueryLikelihood.loadIndex("invertedindex.txt");
		int[] muList = {10, 100, 200, 500, 1000, 2000, 2500, 3000, 5000};
		// calculate query likelihood for each value of mu
		for (int mu : muList) {
			System.out.println("mu = "+mu);
			BufferedReader reader = new BufferedReader( new InputStreamReader(SearchEngine.class.getResourceAsStream("queries.txt")) );
			BufferedWriter writer = new BufferedWriter( new FileWriter("querylikelihood_"+mu+".txt") );
			String query = reader.readLine();
			int queryid = 1;
			while (query != null) {
				QueryLikelihood r = new QueryLikelihood(ii, ii.getDocLengths(), query, queryid, mu);
				r.scores();
				System.out.println("\tScores computed for query "+queryid+".");
				r.sort();
				writer.write(r.toString());
				System.out.println("\tScores sorted. Top 10 written to querylikelihood_"+mu+".txt.");
				query = reader.readLine();
				queryid += 1;
			}
			reader.close();
			writer.close();
		}
	}
}
