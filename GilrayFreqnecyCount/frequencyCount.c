#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include "hashTable.h"
#define MAX_WORD_SIZE  256
/* Casey Gilray
   ASsignment #5
   2/20/13
*/

char* getNextWord(FILE* fd){
 char word[MAX_WORD_SIZE];
 int wordlen = 0;
 char c;
 while ((c=fgetc(fd))!=EOF){
   // printf("%c",c);
   //if the word is at max length, return it with an appending null character
   //while we have not reached the end of file yet, if the character is a space, append a \0 to the current spot in the file and return
   if (isspace(c)){
     if (wordlen >0){
     word[wordlen]='\0';
     return (char*)strdup(word);
     }
   }
   if(isalnum(c)&&(wordlen<=((MAX_WORD_SIZE)-1))){
     //if it is alphanumeric, put it into the word and incriment the "wordlen".
     
     word[wordlen]= tolower(c);
     wordlen++;
   }
 }
 //returns null when EOF is hit
 return NULL;
}



void applyPrint(node* node, int x){
	//defines an apply function to iterate over the hashtable with
	//int x is unused in this function, but can be added later.
	printf("Key: %16s || Value: %8d\n",node->key,(int)node->value);
}

int nodeComp(const void* aNode,const void* bNode){
	//provides qsort with a node comparator, returns <0 if a is less than b, returns 0 if a = b,returns >0 if a > b
	//cast sequence void* > node** => node* -> int* value -> derefrence
	node** nodeA = (node**)aNode;
	node** nodeB = (node**)bNode;
	node* parseNodeA = *nodeA;
	node* parseNodeB = *nodeB;
	int  a = (int)parseNodeA->value;
	int  b = (int)parseNodeB->value;
	if (a>b){return -1;}
	if (a==b){return 0;}
	return 1;
}	

int main(int argc, char* argv[]){
	if (argc < 2){
		printf("Usage: %s, -[int #of lines to print], arguments\n", argv[0]);
		return(1);
	}
	char* charCheck;
	int printLim=0;
	
	for (int i=1;i<argc;i++){
		charCheck = (argv[i]);
		if (strncmp(charCheck,"-",1)==0){
			//should set the argument in printLimfor printing a limited amount of lines
			sscanf(argv[i],"-%d",&printLim);
			break;			
		}	
	}

  FILE* filename; //used to hold the current filename
  char* sword;
  void* searchResult;
	hashtable* table = construct(101);
  for (int i = 1;i<argc;i++){ 
	charCheck = (argv[i]);
	if (strncmp(charCheck,"-",1)!=0){	//big outer loop to handle opening files
    filename = fopen(argv[i],"r");
    if (filename==NULL){return 1;}
  while ((sword = getNextWord(filename)) != NULL){
	searchResult = search(table,sword);
	//first will be NULL if the word was not found, otherwise it will return a postivive value that was held in the key.
	//EDited here, liniar search a linked list to find the word, if it is not foiund append it to tjhe start of the word.
   	if (searchResult != NULL){
		searchResult = (searchResult)++;
		insert(table,sword,searchResult);
	}
	else
	{
	//make this node the first node
		insert(table,sword,(int *)1);
	}
  }
	//applysfunction to the hashtable to fill the searchresult array with node pointers and sorts using the given function and qsort	
	if (printLim==0){printLim = table->entries;}	
	node** sortList;	
	sortList = makeArray(table);
	qsort(sortList,(table->entries-1),sizeof(node*),nodeComp);
  	for (int p = 0;p<printLim;p++){
	node* node = sortList[p];	
	printf("Key: %16s || Value: %8d\n",node->key,(int)node->value);
	}
	printf("done printing, closing file\n");
  fclose(filename);
  }
}	
  return 0;
}
