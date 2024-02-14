#include <stdio.h>
#include "operations.h"

int calculate(char* exp){
    int result = 0;

    int num1 = (int)exp[0];
    int num2 = (int)exp[4];
    char op = exp[2];

    if (op == '+') result = add(num1,num2);
    else if (op == '-') result = subtract(num1, num2);
    else if (op == '*') result = multiply(num1, num2);
    else if (op == '/') result = divide(num1, num2);

    return result;
}
int main() {

    printf("enter and equation in the format <num1> <operator> <num2>: ");
    char* response = malloc(20);
    if (scanf(response)){

        printf("result: %d", calculate(response));
        return 0;
    }
    return 1;
}