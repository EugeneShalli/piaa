class BidDigit:
    """
    Класс для сложения больших чисел с перегруженным сложением
    """
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