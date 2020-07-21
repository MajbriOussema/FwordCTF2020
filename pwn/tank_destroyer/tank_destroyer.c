#include <stdio.h>
#include <stdlib.h>
void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
void win(){
	system("/bin/bash");
}
int main(){
	char buff[60];
	ignore_me_init_buffering();
	printf("welcome, whats ur name ?\n");
	gets(buff);
	return 0;
}