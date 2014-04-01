#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <plot.h>
#define MAXPLANDIST  5870000000000
#define MAX_WORD_SIZE  256

/*Casey Gilray
ASsignement 6
Last edit: Feb 26, 2013
*/

typedef struct planet{
	char* name;
	char* color;
	long size;
	long mass;
	long xPos;
	long yPos;
	long xVel;
	long yVel;
}planet;

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

planet** populatePlanets(FILE* fd){
	//skips the first 7 words
	char* sword; 
	planet** planets = (planet*)malloc(sizeof(planet)*12));
	for ( int i = 0;i<7;i++){
		sword = getNextWord(fd);
		printf("%s Skipped\n", sword);
	}
	for (i = 0 ; i<12;i++){
		planets[i]->name = getNextWord(fd);
		printf("%s Inserted\n", sword);
		planets[i]->color = getNextWord(fd);
		printf("%s Inserted\n", sword);
		planets[i]->size = (long)getNextWord(fd);
		printf("%s Inserted\n", sword);
		planets[i]->mass = (long)getNextWord(fd);
		printf("%s Inserted\n", sword);
		planets[i]->xPos = (long)getNextWord(fd);
		printf("%s Inserted\n", sword);
		planets[i]->yPos = (long)getNextWord(fd);
		printf("%s Inserted\n", sword);
		planets[i]->xVel = (long)getNextWord(fd);
		printf("%s Inserted\n", sword);
		planets[i]->yVel = (long)getNextWord(fd);
		printf("%s Inserted\n", sword);
	}
}


int main(int argc, char* argv[]){
	//checks for the correct number of args or throws a usage error
	if (argc != 2){
		printf("Usage: $s, planetdata.txt", argv[0]);
		return 1;	
	}
	FILE* datafile = fopen(argv[1],"r");
	//populates planets from the opened datafile above
	/*/////////planet[] planets = populatePlanets(datafile);
	plPlotter *plotter;
	plPlotterParams *plotterParams;
	//setting plotter parameters
	//USE_DOUBLE_BUFFERING = no
	//BG_COLOR
	//BITMAPSIZE = 750x750
	plotterParams = pl_newplparams();
	pl_setparam(plotterParams, "USE_DOUBLE_BUFFERING", "no");
	pl_setparam(plotterParams, "BG_COLOR", "blue");
	pl_setparam(plotterParam, "BITMAPSIE", "900x600");

	
	//create a plotter that writes to X11
	if ((plotter = pl_newpl_r("X",stdin, stdout, stderr, plotterParams))==NULL){
		fprintf(stderr, "Coulden't create plotter\n");
		return 1;
	}
	if (pl_openpl_r(plotter)<0){
		fprintf(stderr, "Coulden't open plotter\n");
		return 1;	
	}
	pl_fspace_r(ploter,-MAXPLANDIST,-MAXPLANDIST,MAXPLANDIST,MAXPLANDIST);//sets coordinate system
	pl_flinewidth_r(plotter, 0.25);
	pl_pencolorname_r(plotter, "red");
	pl_erase_r(plotter);
	pl_fmove_r(plotter, 600.0,300.0);
	pl_fcircle_r(plotter, 0.0, 400.0);
	if (pl_closepl_r(plotter)<0){
		fprintf(stderr,"Couldent close plotter\n");
		return 1;
	}
	if (pl_deletepl_r(plotter)<0){
		fprintf(stderr, "Coulden't delete\n");
		return 1;	
	} 
	return 0;
}*//////////////////////
