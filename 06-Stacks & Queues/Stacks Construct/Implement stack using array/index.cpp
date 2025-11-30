#include <iostream>
using namespace std;

class Mystack
{
    int *arr;
    int capacity;
    int top;

public:
    Mystack(int cap)
    {
        capacity = cap;
        arr = new int[capacity];
        top = -1;
    }

    void push(int elem)
    {
        if (top == capacity - 1)
        {
            cout << "stack overflow\n";
            return;
        }
        arr[++top] = elem;
    }

    int pop()
    {
        if (top == -1)
        {
            cout << "stack is empty\n";
            return -1;
        }
        return arr[top--];
    }

    int peek()
    {
        if (top == -1)
        {
            cout << "stack is empty\n";
            return -1;
        }
        return arr[top];
    }

    bool isEmpty()
    {

        return top == -1;
    }

    bool isFull()
    {
        return top == capacity - 1;
    }

    void print()
    {
        for (int i = 0; i <= top; i++)
        {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }
};

int main()
{
    Mystack st(4);
    st.push(45);
    st.push(12);
    st.push(433);
    st.push(4);
    cout << "poped element:" << st.pop() << "\n";
    cout << "top element:" << st.peek() << "\n";
    st.push(122);
    cout << "is stack full:" << (st.isFull() ? "True" : "False") << "\n";
    st.print();
    cout << "top element:" << st.peek() << "\n";

}