section .data
    hello db "Hello", 0
    no db "No", 0
section .text
global main

main:
    ; Initialize x to 5
    mov rax, 5

    ; Check if x is equal to 15
    cmp rax, mov rax, 20
    je truthy_block  ; Jump if equal

    ; If not equal (falsy), print "No"
    mov rax, 1            ; syscall number for write
    mov rdi, 1            ; file descriptor (stdout)
    mov rsi, no           ; pointer to the string
    mov rdx, 2            ; length of the string
    syscall
    jmp end_if

truthy_block:
    ; If equal (truthy), print "Hello"
    mov rax, 1            ; syscall number for write
    mov rdi, 1            ; file descriptor (stdout)
    mov rsi, hello        ; pointer to the string
    mov rdx, 5            ; length of the string
    syscall

end_if:
    ; Exit the program
    mov rax, 60           ; syscall number for exit
    xor rdi, rdi          ; exit status: 0
    syscall
