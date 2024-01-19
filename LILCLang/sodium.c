// #include <sodium.h>
// #include <stdint.h>

// int main(){
//     char myString[32];
//     uint32_t myInt;

//     if (sodium_init() < 0) {
//         /* panic! the library couldn't be initialized, it is not safe to use */
//         return 1; 
//     }


//     /* myString will be an array of 32 random bytes, not null-terminated */        
//     randombytes_buf(myString, 32);

//     /* myInt will be a random number between 0 and 9 */
//     myInt = randombytes_uniform(10);

//     printf("%s\n",myString);
//     printf("%d\n",myInt);

// }