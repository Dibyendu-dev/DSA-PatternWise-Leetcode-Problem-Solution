#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void insertionSort(vector<int>& arr){
    int n = arr.size();

    for(int i=1;i<n;i++){
       int element = arr[i];
       int j=i-1;
       
       while(j>=0 && arr[j]>element){
            arr[j+1]= arr[j];
            j--;
       }
       arr[j+1]= element;
    }

}

int main() {
    vector<int> myVector = {64, 34, 25, 12, 22, 11, 90};
    
   cout << "Original array: ";
    for (int x : myVector) {
        cout << x << " ";
    }
    cout << endl;

    insertionSort(myVector);

    cout << "Sorted array: ";
    for (int x : myVector) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}