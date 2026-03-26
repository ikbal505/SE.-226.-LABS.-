//TASK1
#include <iostream>
using namespace std;
int lab2() {
    int x;
    int steps = 0;
    cout << "Enter a number greater than 1: ";
    cin >> x;

    while (x!= 1) {
        cout << x << " -> ";

        if (x% 2 == 0) {
            x= x / 2;
        }
        else {
            x = 3 * x + 1;
        }
        steps++;
    }
    cout << "1" << endl;
    cout << "Total steps: " << steps << endl;

    return 0;

}


#include <iostream>
using namespace std;

int lab2() {
    int n;

    int fizz = 0;
    int buzz = 0;
    int fizzbuzz = 0;

    while (true) {
        cout << "Enter a number between 10 and 100: ";
        cin >> n;

        if (n >= 10 && n <= 100)
            break;

        cout << "Invalid input!" << endl;
    }

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0)
            continue;

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "--- Summary ---" << endl;
    cout << "Fizz count: " << fizz << endl;
    cout << "Buzz count: " << buzz << endl;
    cout << "FizzBuzz count: " << fizzbuzz << endl;

    return 0;

}

#include <iostream>
using namespace std;

int lab2() {
    int n;

    cout << "Enter a number between 3 and 9: ";
    cin >> n;

    for (int i = 1; i <= 2 * n - 1; i++) {

        int k = n - abs(n - i);

        for (int j = 1; j <= k; j++) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}