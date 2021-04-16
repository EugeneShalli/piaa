class BigArr:
    """
    Класс для реализации рекурсивного бинарного поиска и рекурсивного бинарного поиска по ответу для массива
    """
    def __init__(self, arr):
        self.arr = arr
        self.N = len(self.arr)

    def binary_search(self, left, right, x):
        if right >= left:
            middle = left + (right - left) // 2
            if self.arr[middle] == x:
                return middle
            elif self.arr[middle] > x:
                return self.binary_search(left, middle - 1, x)
            else:
                return self.binary_search(middle + 1, right, x)
        else:
            return -1

    def good(self, length):
        count = 1
        cur_len = self.arr[0] + length
        for i in range(1, self.N):
            if self.arr[i] > cur_len:
                count += 1
                cur_len = self.arr[i] + length
        # print(count)
        return count

    def binary_search_on_answer(self, K, left, right):
        if right > left:
            middle = (left + right) // 2
            if self.good(middle) > K:
                return self.binary_search_on_answer(K, middle+1, right)
            elif self.good(middle) <= K:
                return self.binary_search_on_answer(K, left, middle)
        else:
            return right