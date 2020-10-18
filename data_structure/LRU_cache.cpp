// Reference: https://www.geeksforgeeks.org/lru-cache-implementation/

// 简单来说，对于给定了cache size或者存储的变量数量的LRU cache，
// 它的作用是永远将最近使用的变量放在前面，
// 当需要新加入变量的时候，把新的变量放在top，
// 如果此时cache满了，则把最不常用的那个从cache中移除。

// 这里我们用两个常用的数据结构来实现LRU Cache
// 1. Queue: 底层结构用的是双链表(doubly linked list). queue的max size
//           是预先设定好的，代表cache size. 最近使用的数据会被放在前面，
//           最少使用的数据会被放在queue末尾
// 2. Hash： key是LRU Cache中存储的数据，value存的是queue里面每个node的地址。


#include <bits/stdc++.h>
using namespace std;

class LRUCache {
    // store keys of cache
    list<int> dq; // queue
    
    // store references of key in cache
    unordered_map<int, list<int>::iterator> ma;
    int csize // maximum capacity of cache
    
public:
    LRUCache(int):
    void refer(int);
    void display();
};

// Declare the size
LRUCache::LRUCache(int n) {
    csize = n;
}

// Refers key x with in the LRU Cache
void LRUCache::refer(int x) {
    // x not present in cache
    if (ma.find(x) == ma.end()) {
        // if cache is full
        if (dq.size() == csize) {
            // detele least recently used element
            int last = dp.back();
            dq.pop_back();
            ma.erase(last)
        }
    } else { // x is already in cache
        dq.erase[ma[x]];  // delete x from which its current position
        ma[x] = dq.begin() // and then put in the front
    }
}


// Function to display contents of cache
void LRUCache::display() {
    // Iterate in the deque and print
    // all the elements in it
    for (auto it = dq.begin(); it != dq.end(); it++) {
        cout << (*it) << " ";
    }
    cout << endl;
}
        
    
    

    


