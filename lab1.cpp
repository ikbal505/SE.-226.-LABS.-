#include <iostream>
#include <string>

using namespace std;
int main() {
    // question1
    string name;
    string student_id;

    cout << "What is your name?" << endl;
    cin >> name;
    cout << "Hello " << name << "." << endl;

    cout << "What is your Student ID?" << endl;
    cin >> student_id;
    cout << "Your ID is " << student_id << "." << endl;

    cout << "-----" << endl;

    // question2
    int total;
    cout << "Enter total seconds: ";
    cin >> total;

    int hours = total / 3600;
    int remaining = total % 3600;
    int minutes = remaining / 60;
    int seconds = remaining % 60;

    cout << total << " seconds is " << hours << " hours " << minutes << " minutes and " << seconds << " seconds" << endl;

    cout << "---" << endl;

    // question3
    double x1, y1, x2, y2;
    cout << "Enter x1: "; cin >> x1;
    cout << "Enter y1: "; cin >> y1;
    cout << "Enter x2: "; cin >> x2;
    cout << "Enter y2: "; cin >> y2;

    double dx = x2 - x1;
    double dy = y2 - y1;
    double square = (dx * dx) + (dy * dy);
    double a = square / 2.0;
    for(int i = 0; i < 10; i++) {
        a = (a + square/ a) / 2.0;
    }

    cout << "Distance is approximately: " << a<< endl;

    cout << "------" << endl;

    // question4

    string pattern = "";
    int star = 7;
    int gap = 0;

    while (star >= 1) {
        // Boşlukları ekle
        for (int i = 0; i <gap; i++) {
            pattern = pattern + " ";
        }
        // Yıldızları ekle
        for (int j = 0; j < star; j++) {
            pattern = pattern + "*";
        }
        // Satır sonu ekle
        pattern= pattern + "\n";

        star = star - 2; gap= gap+ 1;
    }

    cout <<pattern;

    return 0;
}