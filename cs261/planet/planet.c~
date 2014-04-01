#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <plot.h>
#include <unistd.h>
#define PLANSCALE 300000000000
#define G .0000000000667259
#define TIMESTEP 1
#define TIMESCALE 3600
#define BORDER 1.1
////////////////// CHANGE THIS TO CHANGE NUMBER OF PLANETS TO PLOT
//////////////////
#define NUMPLANS 7
//////////////////
//////////////////
////////////////// CHANGE THIS TO CHANGE NUMBER OF PLANETS TO PLOT
/*Casey Gilray
ASSignement 6
Last edit: Mar 6, 2013

Usage: ./planet planets.txt

Change the NUMPLANS in the code and recompile to change the number of planets to be ploted.
*/


typedef struct planet{
	char name[20];
	char color[20];
	double size;
	double mass;
	double xPos;
	double yPos;
	double xVel;
	double yVel;
    	double nextXpos;
    	double nextYpos;
    	double nextXvel;
    	double nextYvel;
    	double xStartPos;
    	int completedOrb;
}planet;



planet* populatePlanets(FILE* fd){
	//skips the first 7 words
	planet* planets = (planet*)malloc(sizeof(planet)*12);
	char sLine[256];
	fgets(sLine,256,fd);
	/*printf("Top line variables skipped\n");*/
	for (int i = 0 ; i<NUMPLANS;i++){
		fgets(sLine, 256, fd);
		sscanf(sLine, "%s %s %lf %lf %lf %lf %lf %lf", planets[i].name, planets[i].color, &planets[i].size,&planets[i].mass, &planets[i].xPos, &planets[i].yPos,&planets[i].xVel, &planets[i].yVel);
		planets[i].xStartPos = planets[i].xPos;
		planets[i].completedOrb = 0;
		/*printf("%s Inserted\n", planets[i].name);
		printf("%s Inserted\n", planets[i].color);
		printf("%lf Inserted\n", planets[i].size);
		printf("%lf Inserted\n", planets[i].mass);
		printf("%lf Inserted\n", planets[i].xPos);
		printf("%lf Inserted\n", planets[i].yPos);
		printf("%lf Inserted\n", planets[i].xVel);
		printf("%lf Inserted\n", planets[i].yVel);
		*/
	}
	return planets;
}

void drawPlanets(plPlotter *plotter, planet* planets){
	pl_erase_r(plotter);
	for(int i = 0;i<NUMPLANS;i++){
		//draws each of the 12 planets in accordance with their x and y positions and relative size
		pl_flushpl_r(plotter);
		pl_colorname_r(plotter,planets[i].color);
		pl_fcircle_r(plotter,planets[i].xPos, planets[i].yPos,(planets[i].size*PLANSCALE));
		pl_flushpl_r(plotter);
	}
}

void updatePositions(planet* planets, int timestep){
	//updates positions of the planets by adding the differeince in time by the velocity
	for (int i = 0;i<NUMPLANS;i++){
		//enacts the function xpos = xpos + time*xvel
		planets[i].nextXpos =timestep * planets[i].xVel + planets[i].xPos;
		planets[i].nextYpos =timestep * planets[i].yVel + planets[i].yPos;
	}
	for (int i = 0;i<NUMPLANS;i++){
		//swaps next with current as all values are updated
		planets[i].xPos = planets[i].nextXpos;
		planets[i].yPos = planets[i].nextYpos;
	}
	
}

double mag(planet this,planet other){
	//obtains the magnitude of the distances of the planets
	double xdist = this.xPos - other.xPos;
	double ydist = this.yPos - other.yPos;
	double magnitude = sqrt((xdist*xdist)+(ydist*ydist));
	return magnitude;
}

double summationX(planet currPlan, planet* planets){
	//enacts the function Summation of all other planets of (xother-xthis)*mass other * G / mag^3
	double xsummation = 0;
	double magn;
	double xdist;
	for (int x = 0;x<NUMPLANS;x++){
	//if x is this planet, skip it!
		if (strcmp(currPlan.name,planets[x].name)!=0){
			xdist = planets[x].xPos - currPlan.xPos;
			magn =  mag(currPlan, planets[x]);
			magn = magn*magn*magn;
			//else enact the summation function
			xsummation += ((xdist*(planets[x].mass)*G)/magn);
		} 
	}
	return xsummation;
}

double summationY(planet currPlan, planet* planets){
	//enacts the function Summation of all other planets of (yother-ythis)*mass other * G / mag^3
	double ysummation = 0;
	double magn;
	double ydist; 
	for (int y = 0;y<NUMPLANS;y++){
	//if y is this planet, skip it!
		if (strcmp(currPlan.name,planets[y].name)!=0){
			ydist = planets[y].yPos - currPlan.yPos;
			magn =  mag(currPlan, planets[y]);
			magn = magn*magn*magn;
			//else enact the summation function
			ysummation += ((ydist*planets[y].mass*G)/magn);
		} 
	}
	return ysummation;
}

void updateVelocities(planet* planets, int timestep){
	//updates the velocities using a summation function
	for (int j = 0;j<NUMPLANS;j++){
		planets[j].nextXvel =timestep*summationX(planets[j],planets)+ planets[j].xVel;
		planets[j].nextYvel =timestep*summationY(planets[j],planets)+ planets[j].yVel;
	}
	for (int j = 0;j<NUMPLANS;j++){
		planets[j].xVel = planets[j].nextXvel;
		planets[j].yVel = planets[j].nextYvel;
	}
}

void checkOrbits(planet* planets, int t){
	//checks all the planets current positions with their original positions.
	//if the planet is within a threshhold, an orbit is considered completed and will print out how many days it took for that orbit.
	for (int k = 1;k<NUMPLANS;k++){
		//only waste time checkingf for one orbit
		if (planets[k].completedOrb != 1){
		double xdist = planets[k].xPos - planets[k].xStartPos;
		double ydist = planets[k].yPos;
		double magnitude = sqrt((xdist*xdist)+(ydist*ydist));
		//printf("%lf is the distance from the current posiion\n",magnitude);	
			if (magnitude < 7900000000){
				//printf("%lf is the distance from the current posiion\n",magnitude);
				//time passed is equal to how many iterations of hours ive done(t) dvided by 24, hours in a day
				float timediff = t/24.0;
				//planet is within threshhold
				printf("%s has completed an orbit %f days after start.\n", planets[k].name,timediff);
				planets[k].completedOrb = 1;
		}
		}
	}
}

void animPlanets(plPlotter *plotter, planet* planets){
	//animates the planets by updating their x and y positions with respect to their  xand y velocities for each timestep
	for (int t = 0; t<100000; t++){
		for (int g=0;g<TIMESCALE;g++){
			updateVelocities(planets,TIMESTEP);
			updatePositions(planets,TIMESTEP);
		}
		drawPlanets(plotter, planets);
		if (t > 1900){
			checkOrbits(planets,t);
		}
	}
}


int main(int argc, char* argv[]){
    //checks for the correct number of args or throws a usage error
	if (argc != 2){
		printf("Usage: %s, planetdata.txt", argv[0]);
		return 1;
	}
	FILE* datafile = fopen(argv[1],"r");
	//populates planets from the opened datafile above
	planet* planets = populatePlanets(datafile);
	fclose(datafile);
	double MAXPLANDIST = planets[NUMPLANS-1].xPos;
	plPlotter *plotter;
	plPlotterParams *plotterParams;
	//setting plotter parameters
	//USE_DOUBLE_BUFFERING = no
	//BG_COLOR
	//BITMAPSIZE = 750x750
	plotterParams = pl_newplparams();
	pl_setplparam(plotterParams, "USE_DOUBLE_BUFFERING", "no");
	pl_setplparam(plotterParams, "BG_COLOR", "black");
	pl_setplparam(plotterParams, "BITMAPSIZE", "750x750");

	
	//create a plotter that writes to X11
	if ((plotter = pl_newpl_r("X",stdin, stdout, stderr, plotterParams))==NULL){
		fprintf(stderr, "Coulden't create plotter\n");
		return 1;
	}
	if (pl_openpl_r(plotter)<0){
		fprintf(stderr, "Coulden't open plotter\n");
		return 1;	
	}
	pl_fspace_r(plotter,-MAXPLANDIST*BORDER,-MAXPLANDIST*BORDER,MAXPLANDIST*BORDER,MAXPLANDIST*BORDER);//sets coordinate system
	pl_filltype_r(plotter,1);
	pl_erase_r(plotter);
	
	drawPlanets(plotter,planets);
	pl_flushpl_r(plotter);
	animPlanets(plotter,planets);
	
	sleep(4);

	pl_erase_r(plotter);
	
	if (pl_closepl_r(plotter)<0){
		fprintf(stderr,"Couldent close plotter\n");
		return 1;
	}
	if (pl_deletepl_r(plotter)<0){
		fprintf(stderr, "Coulden't delete\n");
		return 1;	
	}
	
	return 0;
}
