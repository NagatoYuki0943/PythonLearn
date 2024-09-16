"""
冒泡排序
升序:每次都从第一个开始排序,相邻的比较将最大的放到最后边,每比较一次最大的就放到后边
降序,每次都从最后一个开始排序,相邻的比较将最大的放到最前边,每比较一次最大的就放到前边

时间复杂度:最坏情况:O(N^2)
          最好情况:O(N)
空间复杂度:O(1)
"""


def bubbleSort(arr: list):
    length = len(arr)

    for i in range(length - 1):  # 比较len-1次,比如长度为10,len-1=9,从0-8一共9次
        flag = False

        for j in range(
            length - 1 - i
        ):  # j每次都从第一个开始比,到小于len-1-i,第一次比9次,第二次比8次,以此类推
            # 升序降序只要改这里的大于号就可以
            if arr[j] >= arr[j + 1]:  # 遇到后面比自己小就交换位置
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # 没有发生交换，说明已经排好，退出排序
        if not flag:
            break


if __name__ == "__main__":
    arr = [1, 3, 5, 0, -4, 10, 5, -100]
    bubbleSort(arr)
    print(arr)  # [-100, -4, 0, 1, 3, 5, 5, 10]
