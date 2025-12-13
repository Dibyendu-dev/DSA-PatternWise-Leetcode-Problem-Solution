class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>st;
        for(string& token :tokens){
            if(isOperator(token)){
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                int result = applyOperator(token,a,b);
                st.push(result);
            }else{
                st.push(stoi(token));
            }
        }
        return st.top();
    }

    bool isOperator(string& token){
        return token == "+" || token == "-" || token == "*" || token == "/" ;
    }

    int applyOperator(string& op, int a , int b){
        if(op == "+") return a+b;
        else if (op == "-") return a-b;
        else if (op == "*") return a*b;
        else if (op == "/") return a/b;
        return 0;
    }
};