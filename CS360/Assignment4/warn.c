//Casey Gilray
// CS 360
//Assignment 5, warn
//This programm will run the warning program,

//INCLUDES
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <ctype.h>
//debugging mode "if(DEBUG){printf("\n");}"
#define DEBUG 0
#define defaultDelay 1
#define maxInputLength 256

//void changeMessage(int * delay, char* message){
    //replaces the values using the pipe(from the child)
//    fscanf(fd[0],"%d %s\n",&delay,&message);
//}


int loopStatus;

static void pauseHandler(int type){
    return;
}

void loopBreaker(){
    loopStatus= 0;
}
void snore(int seconds){
    signal(SIGINT,loopBreaker);
    signal(SIGALRM, pauseHandler);
    alarm(seconds);
    pause();
    alarm(0);

}

int getInt(char* message){
    char* tempInt =(char*)malloc(sizeof(char)*maxInputLength);
    int returnInt;
    for (int i = 0;i<strlen(message);i++){
        if (isdigit(message[i])){
            strcat(tempInt,message[i]);
        }else{
            break;
        }
    }
    returnInt = atoi(tempInt);
    return returnInt;
}
char* getMessage(char* unparsedmessage){
    char* tempMessage = (char*)malloc(sizeof(char)*maxInputLength);
    
    int i;
    for (i = 0;i<strlen(unparsedmessage);i++){
        if (!isdigit(unparsedmessage[i])){
            break;
        }
    }
    for(int j = i;j<strlen(unparsedmessage);j++){
        if(isalnum(unparsedmessage[j])){
            strcat(tempMessage,unparsedmessage[j]);
        }
    }
    return tempMessage;
}
int main(int argc, char* argv[]){
	//argc gives the umber of arguments and should be 1
	//argv only contains the self-refrence
	
	//Logic/Code:
	int fd[2];
    char input[maxInputLength];
    int child;
    
	//check argc input
	if (argc > 1){printf("Usage: %s\n",argv[0]);exit(1);}
        //makes pipe
		if(DEBUG){printf("set up pipe\n");}		
		pipe(fd);
		//make a new pipe to the "last" function as the parent
		if(DEBUG){printf("fork\n");}
        child = fork();
		if(child != 0){
			//parent
            close(fd[0]);
            while(1){
                signal(SIGINT,pauseHandler);
                //CODE TO HANDLE READING FROM STDIN
                printf("\nPlease enter string to be repeated: ");
                fgets(input,maxInputLength, stdin);
                //check if exit signal recived from user
                if((strcmp(input,"exit\n"))==0){printf("exit confirmed.\n");exit(1);}
                //set up the pause handler, signal the child, write to buffer, then wait
                write(fd[1],input, maxInputLength);
                kill(child,SIGFPE);
                pause();
                
            }
            
           
		}else{
			//child
            close(fd[1]);
            int delay = defaultDelay;
            char * message;
            int tempInt;
            char  unparsedmessage[maxInputLength];
            signal(SIGFPE,pauseHandler);
            pause();
            
            //outer while loop, will not break form this, child dies when parent dies
            while(1){
                //read from pipe into unparsed message
                read(fd[0],unparsedmessage,maxInputLength);
                message = (char*)malloc(sizeof(char)*maxInputLength);
                
                tempInt = getInt(unparsedmessage);
                if (tempInt != 0 && tempInt != delay){
                    delay = tempInt;
                }
                message = getMessage(unparsedmessage);
                /*if(sscanf(unparsedmessage,"%d %[^\n]s",&delay,message)!=2){
                    //only found one retry with no %d
                    sscanf(altUnprocMess,"%[^\n]s",message);
                
                }
                 */
                //set looping variable, begin loop
                loopStatus = 1;
                while(loopStatus){
                    signal(SIGINT,loopBreaker);
                    printf("%s",message);
                    snore(delay);
                    
                }
                signal(SIGFPE,pauseHandler);
                pause();
                
            }
        }
}
