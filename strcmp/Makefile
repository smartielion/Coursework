SYMFORMAT=dwarf
FORMAT=elf

mystery: mystery.o
	gcc -m32 -nostartfiles -g -o mystery mystery.o

mystery.o: mystery.asm
	nasm -f $(FORMAT) -g -F $(SYMFORMAT) mystery.asm

clean:
	rm mystery mystery.o


