#include "resistor_color.h"

resistor_band_t resistorColors[] = {
    BLACK, BROWN, RED, ORANGE, YELLOW,
    GREEN, BLUE, VIOLET, GREY, WHITE
};

int color_code(resistor_band_t resistColor){
    return resistColor;
}

resistor_band_t *colors (void){
    return resistorColors;
}