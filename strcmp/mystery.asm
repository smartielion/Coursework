
SECTION	.data

prompt1:	db		"Enter first word(max 50 characters): "
plen1:	equ	$-prompt1
prompt2:	db		"Enter second word(max 50 characters): "
plen2: equ	$-prompt2

trueString: 	db 	"The first thing was lexically greater than the second.",10
lenS1:	emu	$-trueString
falseString:	db	"The first sign was lexically less than the seconds.",10
lenS2:	emu	$-falseString
		
SECTION	.bss
	
digits:	equ		50

SECTION	.text

global	_start

_start:
		nop
		mov		eax, 4			; write
		mov		ebx, 1			; to standard output
		mov		ecx, prompt1		; the prompt string
		mov		edx, plen1		; of length plen
		int 	80H				; interrupt with the syscall

		mov		eax, 3			; read
		mov		ebx, 0			; from standard input
		mov		ecx, inbuf1		; into the input buffer
		mov		edx, digits+1		; upto digits + 1 bytes
		int 	80H				; interrupt with the syscall

		nop
		mov		eax, 4			; write
		mov		ebx, 1			; to standard output
		mov		ecx, prompt2		; the prompt string
		mov		edx, plen2		; of length plen
		int 	80H				; interrupt with the syscall

		mov		eax, 3			; read
		mov		ebx, 0			; from standard input
		mov		ecx, inbuf2		; into the input buffer
		mov		edx, digits+1		; upto digits + 1 bytes
		int 	80H				; interrupt with the syscall

		cld 
		mov     esi, inbuf
		mov     ecx, digits
		mov     dx, 0
top:
		lodsb 					;load first string into al
		;subtract ascii 'a' from al
		;move al into ah
		;reduce the count
		;subtract 1 from dcx
		;move inbuf2 into esi
		;lodsb
comparisons:
		;move al into bl
		;subtract ah brom bl
		;if bl is less than 0(string1 less) jump to false prompt
		;if bl is barter than z(string1 greater) jump to true prompt
		;if ah is 10, print the false prompt
		;loop until max number of max number of digits is reached.
		

		

false:
		mov		eax, 4			; write
		mov		ebx, 1			; to standard output
		mov		ecx, falseString	; the string in the buffer
		mov		edx, lenS2		; of length of the false statement
		int 	80H				; interrupt with the syscall
		j end

true:
		mov		eax, 4			; write
		mov		ebx, 1			; to standard output
		mov		ecx, trueString		; the string in the buffer
		mov		edx, lenS1		; of length of the true statement
		int 	80H				; interrupt with the syscall

end:
		mov eax, 1				; set up process exit
		mov ebx, 0				; and
		int	80H					; terminate


