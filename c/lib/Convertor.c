#include <stdio.h>                                                               
#include <stdlib.h>   
#include <string.h>   

void print_as_int(char *str_input){
    for(int i=0; i<strlen(str_input); i++){
        printf("%u", str_input[i]);
    }
    printf("\n");
}

void print_as_hexa(char *str_input){
    for(int i=0; i<strlen(str_input); i++){
        printf("%x", str_input[i]);
    }
    printf("\n");
}

void print_as_binary(char *str_input){
    char mask;
    for(int i=0; i<strlen(str_input); i++){
        mask = 1;
        for(int j=0; j<8; j++){
            printf("%u", (str_input[i]&mask)>>j);
            mask += mask;
        }
    }
    printf("\n");
}

void print_as_binary(char *str_input){

}

int main(){
	char *in = "I'm killing your brain like a poisonous mushroom";
    print_as_binary(in);
    print_as_hexa(in);
    print_as_int(in);

    return 0;
}
