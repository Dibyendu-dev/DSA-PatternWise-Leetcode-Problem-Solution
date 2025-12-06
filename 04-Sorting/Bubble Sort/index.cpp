#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void bubbleSort(vector<int>& arr){
    int n = arr.size();
    for(int i=0;i<n;i++){
        bool isSwapped =false;
        for(int j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
                isSwapped = true;
            }
        }
        if(isSwapped == false) break;
    }

}

int main() {
    vector<int> myVector = {64, 34, 25, 12, 22, 11, 90};
    
   cout << "Original array: ";
    for (int x : myVector) {
        cout << x << " ";
    }
    cout << endl;

    bubbleSort(myVector);

    cout << "Sorted array: ";
    for (int x : myVector) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}