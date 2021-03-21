class BidDig:

    def __init__(self, x):
        self.x = list(x)

    def __add__(self, other):
        a = self.x
        b = other.x
        a_r = a[::-1]
        b_r = b[::-1]
        i = 0
        c = 0

        while i < max(len(a), len(b)) or c:
            add = 0
            if i >= len(a):
                a_r.append(0)
            if i < len(b):
                add = int(b_r[i])
            sum = int(a_r[i]) + add + c
            a_r[i] = str(sum % 10)
            c = sum // 10
            i += 1

        return ''.join(a_r[::-1])


class BigArr:

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
        print(count)
        return count

    def binary_search_on_answer(self, K, left, right):
        # left = 0
        # right = len(self.arr)
        # N = len(self.arr)
        # if right - left >= 1:
        if right > left:
            # middle = left + (right - left) // 2
            middle = (left + right) // 2
            # if self.good(middle, N) >= K:
            #     return self.binary_search_on_answer(K, left, middle)
            #     # return self.arr[middle]
            # elif self.good(middle, N) < K:
            #     return self.binary_search_on_answer(K, middle, right)
            if self.good(middle) > K:
                return self.binary_search_on_answer(K, middle+1, right)
                # return self.arr[middle]
            elif self.good(middle) <= K:
                return self.binary_search_on_answer(K, left, middle)
            # else:
            #     return self.binary_search_on_answer(K, left, middle)
        else:
            return right
            # else:
                # return self.binary_search_on_answer(K, left, middle)


        # while right - left > 1:
        #     middle = (left + right) // 2
        #     if self.good(middle):
        #         right = middle
        #     else:
        #         left = middle

