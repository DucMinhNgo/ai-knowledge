#include <iostream>

using namespace std;

int main()
{
    int money;

    cout << "Nhập số tiền:" << endl;
    cin >> money;

    bool flag = 0;

    if (money % 10000 != 0)
    {
        cout << "Số nhập không hợp lệ" << endl;
        return 0;
    }

    cout << money << " = ";

    while (money > 0)
    {
        if (flag == 1)
        {
            cout << " + ";
        }

        if (money >= 500000)
        {
            cout << money / 500000 << " x 500000";
            money = money % 500000;
        }
        else if (money >= 200000)
        {
            cout << money / 200000 << " x 200000";
            money = money % 200000;
        }
        else if (money >= 100000)
        {
            cout << money / 100000 << " x 100000";
            money = money % 100000;
        }
        else if (money >= 50000)
        {
            cout << money / 50000 << " x 50000";
            money = money % 50000;
        }
        else if (money >= 20000)
        {
            cout << money / 20000 << " x 20000";
            money = money % 20000;
        }
        else if (money >= 10000)
        {
            cout << money / 10000 << " x 10000";
            money = money % 10000;
        }

        flag = 1;
    }

    return 0;
}
