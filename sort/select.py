"""
选择排序
时间复杂度:最坏情况:O(N^2)
            最好情况:O(N^2)
空间复杂度:O(1)
"""


def upSelectSort(arr: list):
    length = len(arr)
    for i in range(length - 1):
        choice = i  # 认为第i个是最大/最小的
        for j in range(i + 1, length):
            if arr[choice] > arr[j]:  # 升序,降序唯一的差别
                choice = j
        # 移动之后改变
        if choice != i:
            arr[choice], arr[i] = arr[i], arr[choice]


if __name__ == "__main__":
    arr = [1, 3, 5, 0, -4, 10, 5, -100]
    upSelectSort(arr)
    print(arr)  # [-100, -4, 0, 1, 3, 5, 5, 10]
