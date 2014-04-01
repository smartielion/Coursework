//Casey Gilray
//3/13/2014
//cgilray@gmail.com

/*This program simulates the diniing philosiphers problem by
spawning 5 child processes, the philosphers, and making a random generator(with their pid as a seed)
The processes will try to access a 2 semaphores(#3 will try 3 and 4) When both semaphores are aquired they will "eat" for roughly 9 seconds and replace the semaphores, then think for roughly 11 seconds. */
//INCLUDE BLOCK
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/sem.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <errno.h>
#include "random.h"

void errorHandler(){
    printf("Semop Failed, ERROR %d ~  %s\n",errno,strerror(errno));

}

void pauseHandler(int code){
    return;
}

void philoStart(int shareID,int pid){
    //starts the looping of eating and thinking
    srand(getpid());
    int eatDur;
    int timeEaten = 0;
    struct sembuf takeChop[2] = {{pid,-1,0},{((pid+1)%5),-1,0}};
    struct sembuf giveChop[2] = {{pid,1,0},{((pid+1)%5),1,0}};
    while(timeEaten < 100){
        //wait on my two semaphores
        if(semop(shareID,takeChop,2)==-1){
            errorHandler();
        };
        //got them, time to eat
        eatDur = randomGaussian(9,3);
        if (eatDur < 0)eatDur = 0;
        printf("I am Philospher %d and I am eating for %d seconds, so far ive eaten for %d seconds\n",pid,eatDur,timeEaten);
        timeEaten += eatDur;
        sleep(eatDur);
        if(semop(shareID,giveChop,2)==-1){
            errorHandler();
        };
        //done eating time to sleep
        eatDur = randomGaussian(11,7);
        if (eatDur < 0)eatDur = 0;
         printf("I am Philospher %d and I am thinking for %d seconds\n",pid,eatDur);
        sleep(eatDur);
    }
    printf("I am Philospher %d and I an done eating\n",pid);
    exit (0);
}

int main(int argc, char* argv[]){
    //set up shared memory space
    int semID = semget(IPC_PRIVATE,5,SEM_R|SEM_A);
    //init to 1 for all sems
    struct sembuf initChop[5] = {{0,1,0},{1,1,0},{2,1,0},{3,1,0},{4,1,0}};
    semop(semID,initChop,5);
    //fork five times then wait on 5 signals saying the child died
    for(int i=0;i<5;i++){
        if(fork()==0){
            //calls philosipher helper method with the child's pid
            printf("Philo #%d is being made\n",i);
            philoStart(semID,i);
            printf("Philo %i exited",i);
            exit(1);
        }
    }
    //wait on children to die
    for(int j = 0;j<5;j++){
        wait(NULL);
    }
    printf("All philosophers are done.\n");
    //SEMCTL to CLEAN UP
    semctl(semID,0,IPC_RMID);
    return 0;
}