#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number){
    int sum = 0;
    for(unsigned int i = 0; i <= number; i++){
        sum += i * i;
    }
    return sum;
}

unsigned int square_of_sum(unsigned int number){
    int sum = 0;
    for (unsigned int i = 0; i <= number; i++){
        sum += i;
    }
    int square = sum * sum;
    return square;
}

unsigned int difference_of_squares(unsigned int number){
    return square_of_sum(number) - sum_of_squares(number);
}