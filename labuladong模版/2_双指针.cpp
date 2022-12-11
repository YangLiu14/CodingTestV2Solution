/**
 * 快慢指针
 * 通常用来原地修改数组
 */

/**
 * 删除排序数组中的重复项
 * 要求原地修改
*/
int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;

    int slow = 0, fast = 0;
    while (fast < nums.length) {
        if (nums[fast] != nums[slow]) {  // 这里输入一些条件，可以是检测重复、可以是特殊数值等等
            slow++;
            nums[slow] = nums[fast]; //维护slow指针指向的永远是需要保留下来的位置
        }
        fast++;
    }
    // 数组长度为索引 + 1
    return slow + 1;
}

/**
 * 首尾双指针，通常用来判断
 * 1. 回文: 左右指针同时向中间移动
 * 2. 最长回文子串: 从中心向两端扩散
 */
