class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>mp;
        for(int num : nums){
            mp[num]++;
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap;

        for(auto& entry : mp){
            minHeap.push({entry.second, entry.first});
            if(minHeap.size()>k){
                minHeap.pop();
            }
        }

        vector<int>result;
        while(!minHeap.empty()){
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }

        return result;
    }
};