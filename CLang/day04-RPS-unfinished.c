#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 20

struct all_hands {
    char* rock_hand;
    char* paper_hand;
    char* scissors_hand;
};

char* lower(char *myString) {
  for (size_t i = 0; i < strlen(myString); i++) {
    // Access each char in the string and lowering as needed.
    myString[i] = tolower(myString[i]);
    }  
    return myString;
}

int main(){

    struct all_hands ah;

    ah.rock_hand = "\n"
    "    _______\n" 
    "---'   ____)\n"
    "      (_____)\n"
    "      (_____)\n"
    "      (____)\n"
    "---.__(___)\n"
    "\n";

    ah.paper_hand = "\n"
    "     _______\n"
    "---'    ____)____\n"
    "           ______)\n"
    "          _______)\n"
    "         _______)\n"
    "---.__________)\n"
    "\n";

    ah.scissors_hand = "\n"
    "    _______\n"
    "---'   ____)____\n"
    "          ______)\n"
    "       __________)\n"
    "      (____)\n"
    "---.__(___)\n"
    "\n";

    printf("%s", ah.rock_hand);
    printf("%s", ah.paper_hand);
    printf("%s", ah.scissors_hand);
    char player_selection[MAX];
    char* bot_selection;
    printf("Rock, Paper, Scissors, SHOOT!\n");
    printf("What is your selection? (Try r, p, or s) :");
    scanf("%s", player_selection);

    bot_selection = "Tofu";

    printf("%s", player_selection);
    printf("%s", bot_selection);

    return 0;

}



// all_hands = [rock_hand, paper_hand, scissors_hand]

// print(")
// player_selection = input("What is your selection? (Try r, p, or s) :")
// if player_selection.lower() == "r":
//     player_selection = 0
// elif player_selection.lower() == "p":
//     player_selection = 1
// elif player_selection.lower() == "s":
//     player_selection = 2

// bot_selection = random.randint(0, 2)
// # bot_selection = all_hands[random_selection]
// print("\n")
// print("Your Selection:")
// print(all_hands[player_selection])
// print("\n")
// print("Computer Selection:")
// print(all_hands[bot_selection])
// print("\n")
// if player_selection == 0 and bot_selection == 0 or player_selection == 1 and bot_selection == 1 or player_selection == 2 and bot_selection== 2:
//     print("Selections Draw, NO Winner this round")

// elif player_selection == 0 and bot_selection == 1 or player_selection == 1 and bot_selection == 2 or player_selection == 2 and bot_selection == 0:
//     print("You Lose! Please Try Again!")

// elif player_selection == 0 and bot_selection == 2 or player_selection == 1 and bot_selection == 0 or player_selection == 2 and bot_selection == 1:
//     print("You Win! Great Work!!!")

