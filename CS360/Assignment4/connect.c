//Casey Gilray
// CS 360
//Assignment 4, pipe
//This programm will run the connect command, making a makshift pipe connecting two processes

//INCLUDES
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//debugging mode "if(DEBUG){printf("\n");}"
#define DEBUG 0

int lastColon(int argc,char* argv[]){
	//returns the position of the last colon in the array
	int pos = -1;
	for(int i=0;i<argc;i++){
		if (strcmp(argv[i],":")==0){
			if(DEBUG){printf("found colon\n");}
			//Found a colon, update position
			pos = i;
		}
	}
	return pos;
}



int main(int argc, char* argv[]){
	//argc gives the umber of arguments and should be at least 2
	//argv is a list of command line arguments, using colons as sepeartors for commands.
	
	//Logic/Code:
	int colonPos;
	int fd[2];
	//check argc input
	if (argc < 2){printf("Usage: %s program -[arguments] {: program -[arguments]}\n",argv[0]);exit(1);}
	//find the position ofm the LAST colon in argv
	colonPos = lastColon(argc,argv);
	if(DEBUG){printf("colon position retreived at %d\n",colonPos);}
	//WAS THERE A COLON? BASE CAES FOR RECURSION
	if(colonPos>=0){
		if(DEBUG){printf("Colon existed, replace it\n");}
		argv[colonPos] = NULL;
		//remaining now holds the remainig number of arguments up to but not including the last colon
		if(DEBUG){printf("set up pipe\n");}		
		pipe(fd);
		//make a new pipe to the "last" function as the parent
		if(DEBUG){printf("fork\n");}		
		if(fork()==0){
			if(DEBUG){printf("child~ start\n");}
			//CHILD
			//the child will recursivly use main with the rest of the arguments.
			//child writes to pipe, close stdout, dup fd[1],and close the reader side;
			if(DEBUG){printf("child! close 1, & dup\n");}
			close(1);
			dup(fd[1]);
			close(fd[0]);
			//execvp to the connect program
			if(DEBUG){printf("child exec\n");}
			if(execvp(argv[0],&argv[0])==-1){
				//Error running program
				printf("Program %s cannot be run.\n",argv[0]);
				exit(1);
			}
			
		}else{
			if(DEBUG){printf("parent ~ Start\n");}
			//PARENT
			//parent will execlp to the program
			//parent reads from pipe, close stdin, dup fd[0]
			if(DEBUG){printf("parent ~ close 0 & dup\n");}
			close(0);
			dup(fd[0]);
			close(fd[1]);
			if(DEBUG){printf("parent ~ exec\n");}
			if(execvp(argv[colonPos+1],&argv[colonPos+1])==-1){
				//Error running program
				printf("Program %s cannot be run.\n",argv[colonPos+1]);
				exit(1);
			}
			
		}
	}else{ 
	//if there is NO colon exec the program in the commandline
		if(DEBUG){printf("base case\n");}
		if(execvp(argv[1],&argv[1])==-1){
				//Error running program
				printf("Program %s cannot be run.\n",argv[1]);
				exit(1);
		}
	}
}
