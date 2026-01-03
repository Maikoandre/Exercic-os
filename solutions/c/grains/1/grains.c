#include "grains.h"
#include <math.h>

uint64_t square(uint8_t index){
    uint64_t output = pow(2, index - 1);
    return output;
}

uint64_t total(void){
    return (uint64_t) pow(2, 64);
}