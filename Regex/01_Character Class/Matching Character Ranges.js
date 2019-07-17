// Problem Link: https://www.hackerrank.com/challenges/matching-range-of-characters/problem
// ----------------------------------------------------------------------------------------


var Regex_Pattern = /^[a-z][1-9][^a-z][^A-Z][A-Z].*/; //Do not delete '/'.


/*

	No need to give {5, } at the end of regex pattern, as the below regex pattern ensures the length should be at least 5.
	Also .* means any character except new line can occur 0 or more times. 
	Thus the below pattern ensures length can be at least 5 or more than 5. 

*/