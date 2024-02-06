#include "divideC.h"

%module divide
%{
extern double divideC(int num, int den);
%}

extern double divideC(int num, int den);
