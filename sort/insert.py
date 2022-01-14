'''
插入排序
插入排序。注意，若后面一个元素比其前面一个元素小，则将这两个元素交换位置，然后再来比较这个插入元素与前面一个元素的大小，
若小，则还需要交换这两个元素位置，一直到这个插入元素在正确的位置为止
时间复杂度: 最坏情况下为O(N*N)，此时待排序列为逆序，或者说接近逆序
           最好情况下为O(N)，此时待排序列为升序，或者说接近升序。
空间复杂度: O(1)
'''

def upInsertSort(arr: list):
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]   # 获取初值

        flag = False    # 判断有无交换的条件

        l = [t for t in range(-1, i)]   # j从i-1开始,往左找到第0个
        l.reverse()  # 倒序

        # 从右往左比较,直到最左侧
        for j in l:
            if arr[j] > temp:   # 升序降序只要改这里的大于号就可以
                arr[j+1] = arr[j]
                flag = True
            else:
                break   # 说明当前在对的位置,前面的都比temp小
        if flag:
            arr[j+1] = temp #j运行完之后会-1,到要交换的前一个位置, 所以要+1


if __name__ == "__main__":
    arr = [1, 3, 5, 0, -4, 10, 5, -100]
    upInsertSort(arr)
    print(arr)  # [-100, -4, 0, 1, 3, 5, 5, 10]