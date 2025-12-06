#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int get_min(vector<int>& arr, int idx){
     int n =arr.size();
     int result = INT_MAX;
     int result_idx = -1;
     for(int i=idx;i<n;i++){
        if(arr[i]<result){
            result= arr[i];
            result_idx=i;
        }
     }
     return result_idx;
}

void selectionSort(vector<int>& arr){
    int n =arr.size();
    for(int i=0;i<n;i++){
        int min_idx = get_min(arr,i);
        if (min_idx != i){
            swap(arr[min_idx],arr[i]);
        }
    }
    
}



int main() {
    vector<int> myVector = {64, 34, 25, 12, 22, 11, 90};
    
   cout << "Original array: ";
    for (int x : myVector) {
        cout << x << " ";
    }
    cout << endl;

    selectionSort(myVector);

    cout << "Sorted array: ";
    for (int x : myVector) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}