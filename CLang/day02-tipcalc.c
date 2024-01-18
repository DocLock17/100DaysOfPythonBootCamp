#include <stdio.h>

int main(){
    float bill;
    // int tip; // < -- Turns to 0 when divided by more than tip amount
    float tip;
    int people;
    float bill_with_tip;
    float bill_per_person;
    
    printf("Welcome to the tip calculator!\n\n");
    

    printf("What was the total bill? $");
    scanf("%f", &bill);
    
    printf("How much tip would you like to give? 10, 12, 15, or more? ");
    scanf("%d", &tip);

    printf("How many people to split the bill?");
    scanf("%d", &people);

    bill_with_tip = (bill*(1+(tip/100)));
    // bill_with_tip = (bill*(100+tip))/100; // <-- Alternative math to support int type tip
    printf("The total bill was $%0.2f\n",bill_with_tip);

    bill_per_person = bill_with_tip / people;
    printf("Each person should pay $%0.2f\n",bill_per_person);

    return 0;
}