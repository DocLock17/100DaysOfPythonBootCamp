#include<stdio.h>

#define MAX 100

int main(int argc, char *argv[]){
    char city[MAX];
    char pet[MAX];

    printf("Welcome to the Band Name Generator.\n");
    printf("\n");

    printf("What City did you grow up in?: ");
    scanf("%s", &city);
    printf("\n");

    printf("What was your childhood pet's name?: ");
    scanf("%s", &pet);
    printf("\n");

    printf("Your band\x20name should be: %s %s\n", city, pet);
    printf("\n");

    return 0;
}

