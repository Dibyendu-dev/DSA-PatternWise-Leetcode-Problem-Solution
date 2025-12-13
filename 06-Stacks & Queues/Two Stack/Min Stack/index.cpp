class MinStack {
    
private:
    stack<int> valStack;
    stack<int> minStack;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        valStack.push(val);
        
        if (minStack.empty()) {
            minStack.push(val);
        } else {
            minStack.push(min(val, minStack.top()));
        }
    }
    
    void pop() {
        valStack.pop();
        minStack.pop();
    }
    
    int top() {
        return valStack.top(); 
    }
    
    int getMin() {
        return minStack.top();
    }
};