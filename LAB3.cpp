#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2)
{
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout<< *(arr + i) << " ";
    }
    cout<<endl;

}

int findSum(int* arr, int size)
{
    int sum = 0;

    for (int i = 0; i < size; i++)
    {
        sum += *(arr + i);
    }
    return sum;
}

void shiftRight(int* arr, int size)
{
    int last = arr[size - 1]; 
    for (int i = size - 1; i > 0; i--)
    {
        arr[i] = arr[i - 1];
    }
    arr[0] = last;
}

int* createArray(int size)
{
    int* arr = new int[size];

    cout << "Enter values:  ";

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
    return arr;
}

void deleteArray(int* arr)
{
    delete[] arr;
}

int main()
{
    cout << "Creating dynamic array..." << endl;

    int size;

    cout << "Enter array size: ";    cin >> size;

    int* arr = createArray(size);

    cout << endl;
    cout << "Array elements:" << endl;
    printArray(arr, size);

    int sum = findSum(arr, size);

    cout << endl;
    cout << "Sum of elements: " << sum << endl;

    cout << "------" << endl;

    cout << "Swapping two numbers" << endl;

    int a = 5;
    int b = 8;

    cout << endl;
    cout << "Before swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    swapValues(&a, &b);

    cout << endl;
    cout << "After swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    cout << "---" << endl;

    cout << "Shifting array to the right..." << endl;

    shiftRight(arr, size);

    cout << endl;
    cout << "Array after shiftRight:" << endl;
    printArray(arr, size);

    cout << "----" << endl;

    cout << "Deleting array..." << endl;

    deleteArray(arr);

    cout << "Memory released successfully." << endl;

    return 0;
}