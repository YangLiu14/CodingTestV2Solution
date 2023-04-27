#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;


// 自定义sort算法
// 此sort达到的效果是: 按照heights排序，但是同时也把heights对应的indices
// 也按照heights排序后的变动跟着变动了
vector<int> sortByHeights(vector<int> heights) {
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
