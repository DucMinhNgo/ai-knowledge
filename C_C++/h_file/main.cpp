#include <iostream>
#include "outsidefile.h"

using namespace std;

int main()
{

    outside_function();

    int number = -4;

    cout << "number before passing into the function = " << number << endl;

    number = absolute(number);

    cout << number << endl;

    return 0;
}