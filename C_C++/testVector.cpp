#include <iostream>
#include <vector>

using namespace std;

void arrayInput(vector<float> &a)
{
    int n;
    cin >> n;
    if (n < 1)
        return;

    a.resize(n);

    for (int i = 0; i < a.size(); i++)
    {
        cin >> a[i];
    }
}

void arrayOutput(const vector<float> &a)
{
    for (int i = 0; i < a.size(); i++)
        cout << a[i] << "";
}

int main()
{
    vector<float> a;
    arrayInput(a);
    arrayOutput(a);
    return 0;
}