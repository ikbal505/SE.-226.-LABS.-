#include <iostream>

using namespace std;
double solve_it_recursive(int n) {

    if (n == 1) {
        return 1.0;
    }

    double current_term;


    if (n % 2 == 0) {
        current_term = -1.0 / n;
    } else {
        current_term = 1.0 / n;
    }

    return current_term + solve_it_recursive(n - 1);
}

int main() {
    int n;
    cout << "Enter n value: ";
    cin >> n;

    if (n > 0) {
        cout << "result: " << solve_it_recursive(n) << endl;
    }
    return 0;
}
