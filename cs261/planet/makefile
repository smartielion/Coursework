planet: planet.o
	gcc -o planets planet.o -dynamic -lplot -lXaw -lXmu -lXt -lXext -lSM -lICE -lX11 -lpng -lz -lm

planet.o: planet.c
	gcc -std=c99 -Wall -pedantic -c planet.c


