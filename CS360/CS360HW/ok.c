//Casey Gilray
//CS360 ASsignment 2
//This program is intended to open a dictionary file "webster", and compare a command line argument to the master dictionary
//to decide if the command line word is a word spelled correctly

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <ctype.h>

int compare(char* sword, int fd){
	//format the sword
	char want[16] = {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\0'};
 	for (int i = 0;isalpha(sword[i]);i++){
 		want[i] = sword[i];
 	}
	//this method is used to trace through a dictionary and find the word using a binary search recursivly
	int left = 0;
	//finds the last bit of the file
	int right = lseek(fd,0,SEEK_END);
	right = right - (right % 16);
	int center;
	int wordSize = 15;
	int actual;
	char have[15];
	//fprintf(stdout,"%d left %d right\n",left,right);
	while(left <= right){
		center = (right+left)/2;	
		//repositions center to the start of the word
		center = center - (center%16);
		//printf("center is %d)",center);	
		lseek(fd,center,SEEK_SET);
		//attempt to read the word at center
		actual = read(fd,have,wordSize*sizeof(char));
		//printf("actual is %d",actual);
		//not enough characters read, musta broke
		if(actual < wordSize){break;}
		//fprintf(stdout,"%s compared woith %s",want,have);
		int strCompResult = strcmp(want,have);
		//fprintf(stdout,"%d strcomp\n",strCompResult);
		if(strCompResult == 0){return 0;}
		if(left == right){break;}
		//printf("need to move pointer in some direction");
		if(strCompResult > 0){left = center+16;}
		else {right = center-16;}
		 
	}
	return 1;
}	

int main(int argc, char* argv[]){
	//checks to see if argc is 2, if not, then the command line was used wrong
	if (argc != 2){fprintf(stderr,"Erorr - Usage, %s word\n", argv[0]);exit(-1);}
	//stores the char* in argv
	char* compword = argv[1];
	int openTry = open("./webster", O_RDONLY,0);
	if (openTry < 0){fprintf(stderr,"%s: Can't open webster for reading -- %s\n", argv[0],strerror(errno));exit(1);}
	int result = compare(compword,openTry);
	if (result == 0){fprintf(stdout,"yes\n");}
	else{fprintf(stdout,"no\n");}
	return 0;
}
