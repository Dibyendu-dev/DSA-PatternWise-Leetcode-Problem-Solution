#include <iostream>
#include <queue>
using namespace std;

int main(){
    priority_queue<int> pq; //max heap
    priority_queue<int, vector<int>, greater<int>> mq;  //min heap

    pq.push(20);
    pq.push(50);
    pq.push(10);
    pq.push(7);

    cout<< "size of priority queue"<<pq.size()<<endl;

    while (!pq.empty())
    {
        cout<<pq.top()<< " ";
        pq.pop();
    }
    
    return 0;
}