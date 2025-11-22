#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class MaxHeap
{
   vector<int> heap;

public:
    int parent(int i)
    {
        return (i - 1) / 2;
    }
    int left(int i)
    {
        return 2 * i + 1;
    }
    int right(int i)
    {
        return 2 * i + 2;
    }

    void insert(int val)
    {
        heap.push_back(val);
        int i = heap.size() - 1;

        while (i != 0 && heap[parent(i)] < heap[i])
        {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }

     void heapify(int i, int n) {
        int largest = i;
        int l = left(i);
        int r = right(i);

        if (l < n && heap[l] > heap[largest]) {
            largest = l;
        }

        if (r < n && heap[r] > heap[largest]) {
            largest = r;
        }

        if (largest != i) {
            swap(heap[i], heap[largest]);
            heapify(largest, n);
        }
    }

    void printHeap()
    {
        for (int x : heap)
            cout << x << " ";
    }

     void heapSort() {
        int n = heap.size();

        // build max-heap
         for (int i =n/2-1; i>= 0; i--) {
            heapify(i, n);
        }

         for (int i=n-1;i>0;i--) {
             swap(heap[0], heap[i]);
              heapify(0, i);
         }
     }
};

int main()
{
    MaxHeap h;

    h.insert(12);
    h.insert(25);
    h.insert(7);
    h.insert(33);
    h.insert(41);

    cout << "Heap elements are: ";
    h.printHeap();
    cout << "\n";
    h.heapSort();
    h.printHeap();
    return 0;
}