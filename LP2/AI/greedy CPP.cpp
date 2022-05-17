#include<iostream>
#include<vector>
#define endl '\n'
using namespace std;

void swap(int *p1, int *p2)
{
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void selectionSort(vector<int>& arr, int size)
{
    for(int i=0; i<size-1; i++)
    {
        int select = i;
        for(int j=i; j<size; j++)
        {
            if(arr[select] > arr[j])
            {
                select = j;
            }
        }
        swap(&arr[i], &arr[select]);
    }
}

int main()
{
    int size=0;
    vector<int> arr;
    while(1)
    {
        cout << "----------------- Menu -----------------" << endl;
        cout << "1. Enter/Update size of array." << endl;
        cout << "2. Enter/Update elements of array." << endl;
        cout << "3. Apply selection sort and print array." << endl;
        cout << "4. Terminate the program." << endl;
        cout << "----------------------------------------" << endl;
        int opt;
        cin >> opt;
        switch(opt)
        {
            case 1:
            {
                cout << "Enter size of array: ";
                cin >> size;
                arr.resize(size, 0);
                break;
            }   
            
            case 2:
            {   
                cout << "Enter space separated elements of array: " << endl;
                for(int i=0; i<size; i++)
                {
                    cin >> arr[i];
                }
                break;
            }
            
            case 3:
            {
                selectionSort(arr, size);
                cout << "Sorted array is: ";
                for(int i=0; i<size; i++)
                {
                    cout << arr[i] << " ";
                }
                cout << endl;
                break;
            }
            
            case 4:
            {
                cout << "Terminating the program!" << endl;
                exit(0);
            }
            
            default:
            {
                cout << "Invalid choice!" << endl;
            }
        }
        cout << endl;
    }
    return 0;
}