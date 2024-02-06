#include <stdio.h>

double divideC(int num, int den) {
    if (den == 0) {
        printf("Error! Division by zero is not allowed.\n");
        return 0;
    }
    return (double) num / den;
}

int main() {
    int num;
    int den;
    printf("Enter the numerator: ");
    scanf("%d", &num);
    printf("Enter the denominator: ");
    scanf("%d", &den);
    double result = divideC(num, den);
    printf("The result is: %.2f\n", result);
    return 0;
}
