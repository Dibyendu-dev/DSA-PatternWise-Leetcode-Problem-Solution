class Node {
 public:
    int key;
    int value;
    Node *next;
    Node *prev;

    Node(int k, int v){
         key = k;
         value = v;
         next = nullptr;
         prev = nullptr;
    }

};
class LRUCache {
public:
 unordered_map<int, Node*> mpp;
 Node *head;
 Node *tail;
 int capacity;

    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new Node(-1,-1);
        tail = new Node(-1,-1);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (mpp.find(key) == mpp.end()) return -1;
        Node *node = mpp[key];
        deleteNode(node);
        insertAtFirst(node);
        return node->value;
    }
    
    void put(int key, int value) {
        if (mpp.find(key) != mpp.end()){
            Node *node = mpp[key];
            node->value = value;
             deleteNode(node);
            insertAtFirst(node);
        } else{
            if (mpp.size() == capacity){
                Node *node = tail->prev;
                mpp.erase(node->key);
                deleteNode(node);
                delete node;
            }
            Node *node = new Node(key,value);
            mpp[key] = node;
            insertAtFirst(node);
        }
    }

    void insertAtFirst(Node *node){
    Node *nextNode = head->next;
    head->next = node;
    node->prev = head;
    node->next = nextNode;
    nextNode->prev = node;
}

void deleteNode(Node *node){
    Node *prevNode = node->prev;
    Node *nextNode = node->next;
    prevNode->next = nextNode;
    nextNode->prev = prevNode;
}
};



/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */