#include<iostream>
using namespace

private static void printFreq(char){
	int[] freq = new int[256];
	for (int i = 0; i<str.length;i++){
		freq[str[i]]++;
	}
	for(int i=0;i<256;i++){
		if(freq[i]>0){
			System.out.printf((char)(i)+freq[i]);
		}
	}
}

public static void main(String[] args){
	char[] str = "Hello world".toCharArray();
	printFreq(str);
}