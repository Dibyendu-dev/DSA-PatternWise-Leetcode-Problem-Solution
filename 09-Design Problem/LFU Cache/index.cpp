class Node
{
public:
    int key;
    int value;
    int cnt;
    Node *next;
    Node *prev;

    Node(int k, int v)
    {
        key = k;
        value = v;
        next = nullptr;
        prev = nullptr;
        cnt = 1;
    }
};

class LFUCache
{
public:
    unordered_map<int, Node *> mpp;
    unordered_map<int, pair<Node *, Node *>> freqMpp;
    int minFreq;
    int capacity;
    LFUCache(int capacity)
    {
        this->capacity = capacity;
        minFreq = 0;
    }

    int get(int key)
    {
        if (mpp.find(key) == mpp.end())
            return -1;
        Node *node = mpp[key];
        int res = node->value;
        updateFreq(node);
        return res;
    }

    void put(int key, int value)
    {
        if (capacity == 0)
            return;
        if (mpp.find(key) != mpp.end())
        {
            Node *node = mpp[key];
            node->value = value;
            updateFreq(node);
        }
        else
        {
            if (mpp.size() == capacity)
            {
                Node *lfunode = freqMpp[minFreq].second->prev;
                mpp.erase(lfunode->key);
                remove(lfunode);
                if (freqMpp[minFreq].first->next == freqMpp[minFreq].second)
                {
                    freqMpp.erase(minFreq);
                }
                delete lfunode;
            }
            Node *node = new Node(key, value);
            mpp[key] = node;

            minFreq = 1;
            add(node, 1);
        }
    }

    void add(Node *node, int freq)
    {
        if (freqMpp.find(freq) == freqMpp.end())
        {

            Node *head = new Node(-1, -1);
            Node *tail = new Node(-1, -1);

            head->next = tail;
            tail->prev = head;
            freqMpp[freq] = {head, tail};
        }
        Node *head = freqMpp[freq].first;
        Node *temp = head->next;
        node->next = temp;
        node->prev = head;
        head->next = node;
        temp->prev = node;
    }

    void remove(Node *node)
    {
        Node *delPrev = node->prev;
        Node *delNext = node->next;
        delPrev->next = delNext;
        delNext->prev = delPrev;
    }

    void updateFreq(Node *node)
    {
        int oldFreq = node->cnt;
        node->cnt++;
        remove(node);
        if (freqMpp[oldFreq].first->next == freqMpp[oldFreq].second)
        {
            freqMpp.erase(oldFreq);
            if (minFreq == oldFreq)
            {
                minFreq++;
            }
        }
        add(node, node->cnt);
    }
};