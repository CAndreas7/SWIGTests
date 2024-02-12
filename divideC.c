double divideC(int num, int den) {
    if (den == 0) {
        printf("Error! Division by zero is not allowed.\n");
        return 0;
    }
    return (double) num / den;
}
