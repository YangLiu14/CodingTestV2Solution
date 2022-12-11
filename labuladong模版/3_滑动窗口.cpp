#include <iostream>
#include <unordered_map>
using namespace std;

/**
 * 滑动窗口一般是用来应对【子串问题】
 * 但是里面有许多细节：
 * 1. 如何向窗口添加新元素
 * 2. 如何缩小窗口
 * 3. 在窗口滑动的哪个阶段更新结果
 */

void slidingWindow(string s) {
    unordered_map<char, int> window;
    int left = 0, right = 0;

    while (right < s.size()) {
        // c是将要移入窗口的字符
        char c = s[right];
        // 增大窗口
        right++;
        // 进行窗口内数据的一系列更新
        /** ... **/

        /*** debug ***/
        printf("window: [%d, %d]\n", left, right);
        /*** End of debug ***/

        // 判断左侧窗口是否要收缩
        while (/* window needs to shrink */) {
            // d 是将要被移出窗口的字符
            char d = s[left];
            // 缩小窗口
            left++;
            // 进行窗口内数据的一系列更新
            /** ... **/
        }
    }
}
