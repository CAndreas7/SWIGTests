#include <stdio.h>

double divide(double num, double den) {
    if (den == 0) {
        printf("Error! Division by zero is not allowed.\n");
        return -1;
    }
    return num / den;
}

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    double result = 0;
    if (b < 0) b = b * -1;
    for (int i = 0; i < b; i++) {
        result = add(result, a);
    }
    return result;
}