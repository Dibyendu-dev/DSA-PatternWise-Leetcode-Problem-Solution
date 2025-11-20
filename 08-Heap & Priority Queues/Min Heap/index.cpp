#include <iostream>
#include <vector>

using namespace std;

class MinHeap
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

        while (i != 0 && heap[parent(i)] > heap[i])
        {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }

    void heapify(int i){
        int smallest = i;
        int l = left(i);
        int r = right(i);

        if(l < heap.size() && heap[l] < heap[smallest]){
            smallest =l;
        }

        if(r < heap.size() && heap[r] < heap[smallest]){
            smallest =r;
        }

        if(smallest != i){
            swap(heap[i], heap[smallest]);
            heapify(smallest);
        }
    }

    void deleteRoot(){
        if(heap.size()==0) return;
        heap[0]= heap.back();
        heap.pop_back();
        heapify(0);
    }

    void printHeap()
    {
        for (int x : heap)
            cout << x << " ";
    }
};

int main()
{
    MinHeap h;

    h.insert(12);
    h.insert(25);
    h.insert(7);
    h.insert(33);
    h.insert(41);

    cout << "Heap elements are: ";
    h.printHeap();
    cout << "\n";
    h.deleteRoot();
    h.printHeap();
    return 0;
}