#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;


// Sort by Criterion
void sortByLen(vector<string>& words) {
    // words里包含一些string，按照string的长度，由大到小进行排序
    sort(words.begin(), words.end(), [](const string &a, const string &b) {
            return a.size() < b.size();
    });
}


// 自定义sort算法
// 此sort达到的效果是: 按照heights排序，但是同时也把heights对应的indices
// 也按照heights排序后的变动跟着变动了
void sortByHeights(vector<int> heights) {
    int n = heights.size();

    // Create a vector of indices from 0 to n-1
    vector<int> indices(n);
    iota(indices.begin(), indices.end(), 0);

    // `[&]` is a lambda function that captures all variables used in
    // the function by reference
    sort(indices.begin(), indices.end(), [&](int x, int y) {
        return heights[x] > heights[y];
    });
}
