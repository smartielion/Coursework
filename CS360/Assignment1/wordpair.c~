//Casey Gilray
//wordPair counts words in pairs from one or multiple text files
//this project was an extenstion form a previous project

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <getWord.h>
#include <assert.h>
#include "hashTable.h"

//node comp function for qsort to use reused from CS261 assignemnt 4
int nodeComp(const void* aNode, const void* bNode){
//printf("Node Comp\n");
 node** nodeA = (node**)aNode;
 node** nodeB = (node**)bNode;
 node* ParseNodeA = *nodeA;
 node* ParseNodeB = *nodeB;
 int a = (int)ParseNodeA->value;
 int b = (int)ParseNodeB->value;
 if (a>b){return -1;}
 if (a==b){return 0;}
 return 1;
}

int main(int argc, char* argv[]){
//Check for invalid operands
if(argc < 2){
	printf("Usage: %s, -[int #of lines to print], arguments\n", argv[0]);
	return (1);
}
char* charCheck;
int optionX = 0;
//Takes in as many files as the user wants, with optional parameter to display only X values
//checks to see if the optional parameter exists
//printf("Char Check\n");
for (int i =1; i<argc;i++){
	charCheck = (argv[i]);
	if (strncmp(charCheck, "-",1)==0){
		//sets the arguemnt to optionX to hold the nukmber of lines user wants to be printed
		sscanf(argv[i],"-%d",&optionX);
		break;
	}
}

//makes a hash table & other large scale variables
//printf("open file\n");
FILE* filename;
hashtable* pairsHash = construct(101);
void* searchResult; 
char* firstWord = NULL;
char* secondWord = NULL;
char* sword;
//printf("word loop\n");
for (int i = 1; i<argc;i++){
	charCheck = argv[i];
	if (strncmp(charCheck,"-",1)!=0){
		filename = fopen(argv[i],"r");
		assert(filename != NULL);
		while (((secondWord=getNextWord(filename))!= NULL)){
//			printf("%d\n",strlen(secondWord));
//			printf("word while loop\n");
			//checks if this is the first word of the file by seeing if first word is currently NULL
			if (firstWord == NULL){
//				printf("first word null\n");
				firstWord = secondWord; //put the new word into first word, and get the next word	
			}
			else{
//				printf("first word not null\n");
				//first word existed, stringcat them then search for them in the array
//				printf("assert\n");
				assert(firstWord != NULL);
				assert(secondWord != NULL);
//				printf("concats %d\n", strlen(firstWord)); 
				sword=(char *)malloc(strlen(firstWord)+strlen(secondWord)+2);
//				printf("sword malloc\n");
				strcpy(sword,firstWord);
//				printf("copy\n");
				strcat(sword, " ");
				strcat(sword, secondWord);
//				printf("assert sword now exists\n");
				assert(sword != NULL);
				//search for the word pair, not concatenated with a space inbetween
//				printf("saerch\n");
				 searchResult = search(pairsHash,sword);
//				 printf("search done\n");
				 //Will be null if the word was not found
				 if (searchResult != NULL){
//				 	printf("incriment and reinsert\n");
				 	//incriment the searchresult(the value being passed back from the hashtable as frequency count
				 	searchResult = (searchResult)++;
				 	//reinsert(this will only update the value)
				 	insert(pairsHash,sword,searchResult);
				 }
				 else
				 {
				 	//word was not found, inserty witha  count of one
//				 	printf("new insert\n");
				 	insert(pairsHash,sword,(int*)1);
				 }//ends search result if
//				 printf("freeing words\n");
                free(firstWord);
                firstWord = secondWord;
				
			}//ends first word being null if
		}//ends nextWord while
//		printf("close\n");
		fclose(filename);
	}//ends optionmal charcheck if
	
}//ends all files
//makes sortable array
printf("Sort\n");
node** sortList;
sortList = makeArray(pairsHash);
qsort(sortList,pairsHash->entries-1,sizeof(node*),nodeComp);
if (optionX ==0){optionX = pairsHash->entries;}
for(int p=0;p<optionX;p++){
	node* node = sortList[p];
	printf("Key: %16s || Value: %8d\n", node->key, (int)node->value);
}
free(sortList);
free(pairsHash);
return 0;		


}
