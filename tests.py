from src.dig_add import BidDigit
from src.BinTree import BinaryTree
from src.CartTree import Cartesian
from src.DisjointSet import DisSet
from src.BinSearch import BigArr
from tqdm import tqdm
import glob2
import os

ADDING_IN = glob2.glob(os.path.join('tests\\addition', "*.in"))
ADDING_OUT = glob2.glob(os.path.join('tests\\addition', "*.out"))
BINARY_SEARCH_IN = glob2.glob(os.path.join('tests\\binary-search', "*.in"))
BINARY_SEARCH_OUT = glob2.glob(os.path.join('tests\\binary-search', "*.out"))
BINARY_SEARCH_BY_RESULTS_IN = glob2.glob(os.path.join('tests\\binary-search-by-results', "*.in"))
BINARY_SEARCH_BY_RESULTS_OUT = glob2.glob(os.path.join('tests\\binary-search-by-results', "*.out"))
UFF_IN = glob2.glob(os.path.join('tests\\uff', "*.in"))
UFF_OUT = glob2.glob(os.path.join('tests\\uff', "*.out"))
BLOCKS_ON_THE_PICTURE_INT = glob2.glob(os.path.join('tests\\blocks', "*.in"))
BLOCKS_ON_THE_PICTURE_OUT = glob2.glob(os.path.join('tests\\blocks', "*.out"))
BINARY_TREE_IN = glob2.glob(os.path.join('tests\\binary-tree', "*.in"))
BINARY_TREE_OUT = glob2.glob(os.path.join('tests\\binary-tree', "*after.out"))
BINARY_TREE_OUT2 = glob2.glob(os.path.join('tests\\binary-tree', "*contains.out"))


# Test Adding
def test_adding():
    for file_in, file_out in zip(ADDING_IN, ADDING_OUT):
        with open(file_in, 'r') as f_in:
            with open(file_out, 'r') as f_out:
                num_add = int(f_in.readline())
                answer = []
                right_answer = []
                for i in range(num_add):
                    a, b = f_in.readline().split()
                    answer.append(BidDigit(a) + BidDigit(b))
                    right_answer.append(f_out.readline()[:-1])

                print(answer == right_answer)


# Test bin search
def test_binary_search():
    for file_in, file_out in zip(BINARY_SEARCH_IN, BINARY_SEARCH_OUT):
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


# Test bin search in answer
def test_binary_search_on_answer():
    for file_in, file_out in zip(BINARY_SEARCH_BY_RESULTS_IN, BINARY_SEARCH_BY_RESULTS_OUT):
        with open(file_in, 'r') as f_in:
            with open(file_out, 'r') as f_out:
                n = int(f_in.readline())
                k = int(f_in.readline())
                arr = []
                for i in range(n):
                    arr.append(int(f_in.readline()))

                big_arr = BigArr(arr)
                answer = big_arr.binary_search_on_answer(k, 0, big_arr.arr[n-1])
                right_answer = int(f_out.readline())

        print(answer == right_answer)


# Test trees
def test_tree(Tree):
    """
    Общий тест для тестирования деревьев бинарного поиска и декартовых деревьев
    :param Tree: дерево бинарного поиска или декартово дерево
    :return:
    """
    for file_in, file_out, file_out2 in zip(BINARY_TREE_IN, BINARY_TREE_OUT, BINARY_TREE_OUT2):
        with open(file_in, 'r') as f_in:
            with open(file_out, 'r') as f_out:
                with open(file_out, 'r') as f_out2:
                    n = int(f_in.readline())
                    current_value = int(f_in.readline())
                    tree = Tree(current_value)
                    # get_result_contains = '-'
                    # get_result_min_after = '- -'
                    right_answer_contains: str = f_out.readline().replace('\n', '')
                    right_answer_min_after: str = f_out2.readline().replace('\n', '')
                    flag = True
                    for i in tqdm(range(n - 1)):
                        right_answer_contains: str = f_out.readline().replace('\n', '')
                        right_answer_min_after: str = f_out2.readline().replace('\n', '')
                        current_value = int(f_in.readline())
                        try:
                            get_result_contains: str = tree.text_find_node(current_value)
                            if get_result_contains == '-':
                                tree.insert(current_value)
                            get_result_min_after = '{} {}'.format(get_result_contains, tree.text_find_next_node(current_value))
                        except RecursionError:
                            flag = False
                            print("Слишком большая глубина дерева")
                            break
                        if get_result_contains != right_answer_contains and get_result_min_after != right_answer_min_after:
                            flag = False
                            break

        print(flag)


def test_disjoint_set():
    for file_in, file_out in zip(UFF_IN, UFF_OUT):
        with open(file_in, 'r') as f_in:
            with open(file_out, 'r') as f_out:
                data = f_in.readline().split(' ')
                n, m = int(data[0]), int(data[1])
                disjoint = DisSet(n)
                flag = True
                for i in tqdm(range(m)):
                    data = f_in.readline().split(' ')
                    x, y = int(data[0]), int(data[1])
                    answer = f_out.readline().replace("\n", "")
                    result = disjoint.is_one_subset(x, y)
                    if result != answer:
                        flag = False
                        break

                print(flag)


if __name__ == "__main__":
    print("Test adding")
    test_adding()
    print("Test binary search")
    test_binary_search()
    print("Test binary search on answer")
    test_binary_search_on_answer()
    print("Test binary tree")
    test_tree(BinaryTree)
    print("Test cartesian tree")
    test_tree(Cartesian)
    print("Test system of disjoint sets")
    test_disjoint_set()
