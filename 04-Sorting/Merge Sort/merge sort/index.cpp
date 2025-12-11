#include <iostream>
#include <vector>
using namespace std;

void merge(int arr[], int temp[], int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;
    
    // Merge into temp array
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }
    
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    
    // Copy back to original array
    for (i = left; i <= right; i++) {
        arr[i] = temp[i];
    }
}

void mergeSort(int arr[], int temp[], int left, int right) {
    if (left >= right) return;
    
    int mid = left + (right - left) / 2;
    mergeSort(arr, temp, left, mid);
    mergeSort(arr, temp, mid + 1, right);
    merge(arr, temp, left, mid, right);
}


int main() {
 
    int arr2[] = {38, 27, 43, 3, 9, 82, 10};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    vector<int> temp(n2);
    
    cout << "\nOriginal array : ";
    for (int i = 0; i < n2; i++) cout << arr2[i] << " ";
    cout << endl;
    
    mergeSort(arr2, temp.data(), 0, n2 - 1);
    
    cout << "Sorted array : ";
    for (int i = 0; i < n2; i++) cout << arr2[i] << " ";
    cout << endl;
    
    return 0;
}