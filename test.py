from classes import BidDig, BigArr
from tqdm import tqdm


# Test Adding
def test_adding(file_in='1_1.in', file_out='1_1.out'):
    with open(file_in, 'r') as f_in:
        with open(file_out, 'r') as f_out:
            num_add = int(f_in.readline())
            answer = []
            right_answer = []
            for i in range(num_add):
                a, b = f_in.readline().split()
                answer.append(BidDig(a) + BidDig(b))
                right_answer.append(f_out.readline()[:-1])

    print(answer == right_answer)


# Test Insertion
def test_binary_search(file_in='2_5.in', file_out='2_5.out'):
    with open(file_in, 'r') as f_in:
        with open(file_out, 'r') as f_out:
            num_add = int(f_in.readline())
            arr = f_in.readline().split()
            arr = [int(i) for i in arr]
            k = int(f_in.readline())
            answer = []
            right_answer = []
            # print(arr)
            for i in tqdm(range(k)):
                el = int(f_in.readline())
                big_arr = BigArr(arr)
                right_answer.append(int(f_out.readline()))
                answer.append(big_arr.binary_search(0, len(arr) - 1, el))

    print(answer == right_answer)


# Test Insertion
def test_binary_search_on_answer(file_in='3_1.in', file_out='3_1.out'):
    with open(file_in, 'r') as f_in:
        with open(file_out, 'r') as f_out:
            n = int(f_in.readline())
            k = int(f_in.readline())
            arr = []
            for i in range(n):
                arr.append(int(f_in.readline()))

            big_arr = BigArr(arr)
            answer = big_arr.binary_search_on_answer(k, 0, big_arr.arr[n-1])
            print(answer)
            # answer = []
            # right_answer = []
            # # print(arr)
            # for i in tqdm(range(k)):
            #     el = int(f_in.readline())
            #     big_arr = BigArr(arr)
            #     right_answer.append(int(f_out.readline()))
            #     answer.append(big_arr.binary_search_on_answer(0, len(arr) - 1, el))


if __name__ == "__main__":
    test_adding()
    # test_binary_search()
    test_binary_search_on_answer()
