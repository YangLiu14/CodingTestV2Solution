#include <iostream>
#include <unordered_map>
using namespace std;

/**
 *
 * 寻找某一个数的二分查找
 */
int binarySearch(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    // 注意点1
    // while (left <= right) 对应闭区间 [left, right]
    // (left < right) 对应开区间 [left, right)
    while (...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = mid + 1 // 对应闭区间，left = mid 对应开区间
        } else if (nums[mid] > target) {
            right = mid - 1 // 对应闭区间，right = mid 对应开区间
        }
    }
    return ...;
}

/**
 * 寻找左侧边界的二分搜索
 */
int left_bound(int[] nums, int target) {
    int left = 0;
    int right = nums.length;  // 注意这里用的是开区间 [left, right)

    while (left < right) {  // 对应开区间
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            right = mid;  // 缩小右边界，没有 -1，对应开区间
        } else if (nums[mid] < target) {
            left = mid + 1; // 对应闭区间
        } else if (nums[mid] > target) {
            right = mid;  // 对应闭区间
        }
    }
    // 此时 target 比所有数都大，返回-1
    if(left == nums.length) return -1;
    // 判断一下 nums[left] 是不是 target
    return nums[left] == target > left : -1;
}

/*
 * 当然也可以将上述情况写成两边都是闭区间[left, right]的情况
 */
int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            right = mid - 1; //缩小右边界
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        }
    }
    // 此时 target 比所有数都大，返回-1
    if(left == nums.length) return -1;
    // 判断一下 nums[left] 是不是 target
    return nums[left] == target > left : -1;
}

/**
 * 寻找右侧边界的二分搜索
 * 这里直接只写闭区间的写法[left, right]
 */
int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {  //循环结束的条件为 `right == left - 1`
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            left = mid + 1;  //缩小左边界
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        }
    }
    if (left - 1 < 0) return -1;
    return nums[left - 1] == target ? (left - 1) : -1;
}