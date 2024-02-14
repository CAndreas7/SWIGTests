#include <stdio.h>

int divide(int num, int den) {
    if (den == 0) {
        printf("Error! Division by zero is not allowed.\n");
        return -1;
    }
    return num / den;
}

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    int result = 0;
    if (b < 0) b = b * -1;
    for (int i = 0; i < b; i++) {
        result = add(result, a);
    }
    return result;
}