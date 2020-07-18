#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char buffer[40];
/*gcc task1.c -o task1 */
void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
int readSC(){
	printf("Give me your shellcode : \n");
	printf(">>");
	read(0,buffer,40);
	return 0;
}
void runSC(){
	printf("OOOOOPS ! I forgot to make the stack executable :'( \n");
}
void menu(){
	printf("!(I've got everything ready for you) , thank me later\n");
	printf("\t - read\n");
	printf("\t - run\n");
	printf("\t - exit\n");
}

int mugiwara(char * buffer){
	char devilfruit[40];
	int i;
	int len = 40;
	printf("Luffy is amazing, right ? : %lx \n",mugiwara+162);
	for(i=0;*buffer != '\0' && i<sizeof(devilfruit);i++,buffer++){
		devilfruit[i] = *buffer;
		if((*buffer == '\x7a')){
			devilfruit[++i] = '\x89';
		}
	}
	printf("Wanna tell luffy something ? : \n");
	fgets(devilfruit,len,stdin);
	return 0;
}
int choice(){
	char choice[20];
	menu();
	while(1){
		printf("(menu)>>");
		fgets(choice,15,stdin);
		if(!strcmp(choice,"read\n")){
			readSC();
		}
		else if(!strcmp(choice,"run\n")){
			runSC();
		}
		else if(!strcmp(choice,"exit\n")){
			exit(1);
		}
		else if(!strcmp(choice,"gomugomunomi\n")){
			mugiwara(buffer);
		}
		else {
			printf("can you even read ?!\n");
		}
		
	}
}
int main(){
	ignore_me_init_buffering();
	setresuid(getegid(), getegid(), getegid());
	setresgid(getegid(), getegid(), getegid());
	choice();
	return 0;
}