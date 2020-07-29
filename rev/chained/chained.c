#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

/*
    gcc Dlinked.c -o Dlinked -s -fstack-protector
*/
struct node{
    int value;
    struct node* next;
    struct node* prev;
};

typedef struct node* list;

int positions[22] = {12, 5, 0, 2, 15, 8, 4, 18, 17, 20, 9, 1, 21, 7, 19, 6, 11, 14, 3, 10, 16, 13};
long xor[4] = {3, 6, 2, 7};
long cipher[44] = {12632184, 17, 42, 16, 52777363488992, 12632093, 61, 19, 3390893860456126, 52777363488932, 12632190, 121, 14902197487230, 3390893860456184, 52777363488929, 12632094, 7138029487723120146, 14902197487144, 3390893860456124, 52777363488999, 27021599602114969, 7138029487723120136, 14902197487128, 3390893860456146, 7626691028189582, 27021599602115066, 7138029487723120146, 14902197487228, 2000619098349789211, 7626691028189644, 27021599602114979, 7138029487723120158, 2170128915016911999, 2000619098349789261, 7626691028189573, 27021599602114964, 3470024340208640044, 2170128915016911900, 2000619098349789201, 7626691028189626, 3470023632489024591, 3470024340208640120, 2170128915016911967, 2000619098349789257};
void insert(list prev_node,int new_value){
    list new_node = (list)malloc(sizeof(struct node)); 
    new_node->value = new_value;
    new_node->prev = prev_node;
    new_node->next = NULL;
    prev_node->next = new_node;
}
list divide(char * password){
    list l = (list)malloc(sizeof(struct node));
    l->value = password[0];
    l->prev = NULL;
    list head = l;
    for(int i=1;i<strlen(password);i++){
        insert(l,password[i]);
        l = l->next;
    }
    return head;
}
void function1(list l){
    int v,w;
    while(l!=NULL){
        if (l->prev==NULL)
            v = 0;
        else
            v = l->prev->value;
        if (l->next==NULL)
            w = 0;
        else
            w = l->next->value; 
        l->value += w+v;
        l->next->value = v;
        l->prev->value = w;
        l = l->next;
    }
}

int getNodeValueAtPosition(list l,int position){
    list tmp = l;
    int i = 0;
    while(i<44){
        if(i==position){
            return tmp->value;
        }
        i++;
        tmp = tmp->next;
    }
    return -1;
}

void function2(list l){
    int tmp[22];
    list head = l;
    for(int i=0;i<22;i++){
        tmp[i] = l->value;
        l->value = getNodeValueAtPosition(head,positions[i]+15);
        l = l->next;
    }
    for(int i=44;i>22;i--){
        l->value = tmp[i-23];
        l = l->next;
    }

}
void xoring(long * tab,long * tb){
    char x[10];
    sprintf(x,"%lld",tb[0]);
    for(int i =0;i<4;i++){
        tab[i] ^= (int)x[i];
    }
}
void xs(long * tab){
    long t,s;
    t = tab[0] ^ (tab[0] << 11);
    s = tab[0];
    tab[3] = tab[2];
    tab[2] = tab[1];
    tab[1] = s;
    t ^= t << 11;
    t ^= t >> 8;
    tab[0] = t ^ s ^ (s >> 19);
}
void function3(list l,long * result){
    list tmp_list;
    tmp_list = l;
    long tmp[4];
    xs(xor);
    for(int i=0;i<11;i++){
        for(int j=0;j<4;j++){
            tmp[j] = tmp_list->value;
            tmp_list = tmp_list->next;
        }
        xoring(tmp,xor);
        for(int k=0;k<4;k++){
            result[i*4+k] = tmp[k];
        }
    }


}
void print(list l){
    list tmp = l;
    printf("list values\n");
    while(tmp!=NULL){
        printf("%d |",tmp->value);
        tmp = tmp->next;
    }
    printf("\n");
}
void main(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    long result[44];
    char buff[60];
    printf("Give me the password : \n");
    fgets(buff,60,stdin);
    buff[44] = '\0';
    if(strlen(buff)!=44){
        exit(1);
    }
    list l = (list)malloc(sizeof(struct node));
    l = divide(buff);
    function1(l);
    function2(l);
    print(l);
    function3(l,result);
    for(int i=0;i<44;i++){
        if(result[i]!=cipher[i]){
            printf("wrong password\n");
            exit(1);
        }
    }
    char flag[34];
    strncpy(flag,buff,34);
    printf("good job, submit FwordCTF{%s}\n",flag);
}//M4r5aGl1a_x0RSh1f7_1s_SuP3r_5EcuR3_415487712