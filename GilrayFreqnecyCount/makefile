all: frequencyCount clean

JUNK = *.o *~

frequencyCount: hashTable.o  frequencyCount.o
	gcc  -std=c99 -Wall -pedantic -g hashTable.o frequencyCount.o -o frequencyCount


frequencyCount.o: frequencyCount.c hashTable.c hashTable.h
	gcc -c -Wall -pedantic -g -std=c99 frequencyCount.c


hashTable.o: hashTable.c hashTable.h
	gcc -c -Wall -pedantic -g -std=c99 hashTable.c


clean:
	rm $(JUNK)
