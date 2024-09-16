"""
希尔排序，先将待排序列进行预排序，使待排序列接近有序，然后再对该序列进行一次插入排序，此时插入排序的时间复杂度为O(N)，
时间复杂度平均:O(N^1.3)
空间复杂度:O(1)
"""


def shellSort(arr: list):
    length = len(arr)
    gap = length
    while gap > 1:
        # 每次对gap折半操作
        gap = gap // 2

        for i in range(length - gap):
            end = i
            temp = arr[end + gap]
            while length >= 0:
                if temp < arr[end]:
                    arr[end + gap] = arr[end]
                    end -= gap
                else:
                    break
            arr[end + gap] = temp


if __name__ == "__main__":
    arr = [1, 3, 5, 0, -4, 10, 5, -100]
    shellSort(arr)
    print(arr)  # [-100, -4, 0, 1, 3, 5, 5, 10]
