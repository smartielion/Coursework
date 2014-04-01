LIBDIR=$(GET_WORD)/lib
INCDIR=$(GET_WORD)/include

all: pairCount clean

JUNK = *.o *~

pairCount: hashTable.o wordpair.o
	gcc -std=c99 -Wall -pedantic -g -L$(LIBDIR) -I$(INCDIR)  hashTable.o wordpair.o -o pairCount -lget -lm
	
wordpair.o: wordPair.c hashTable.c hashTable.h
	gcc -std=c99 -c -Wall -I$(INCDIR) -L$(LIBDIR) -pedantic -g wordpair.c -lm
	
hashTable.o: hashTable.c hashTable.h
	gcc -std=c99 -c -Wall  -pedantic -g  hashTable.c -lm
	
clean:
	rm $(JUNK)
