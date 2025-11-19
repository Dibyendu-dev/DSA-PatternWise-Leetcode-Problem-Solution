#include <iostream>
#include <vector>

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

    void printHeap()
    {
        for (int x : heap)
            cout << x << " ";
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
    return 0;
}