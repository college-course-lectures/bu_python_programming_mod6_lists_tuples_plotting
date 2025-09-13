import matplotlib.pyplot as plt


def explore_list_iteration():
    colors = ["purple", "orange", "blue"]
    print(colors)
    print(colors[0])
    print(colors[2])

    for c in colors:
        print("color is: " , c)


#Syntax list[start:end:step]  #end is exclusive
#Slicing - creates a sublist
def explore_slice_builtins():
    #Index:  0   1   2   3   4   5
    nums = [50, 60, 30, 40, 10, 20]

    # print(nums[1:4])
    # print(nums[:3])
    # print(nums[::2])

    # #checking for membership
    # print(30 in nums)
    # print(99 not in nums)
    #

    # #built-in for list
    print(nums)
    nums.insert(0,5)
    print(nums)
    nums.remove(40)
    print(nums)
    print(nums.count(30))
    print(nums.index(50))
    nums.sort()
    print(nums)
    nums.reverse()
    print(nums)
    #
    print("len: ", len(nums))
    print("min: ", min(nums), "max: ", max(nums), "sum:", sum(nums))

'''
Assignment
List
Iteration
Concatenation
List Comprehension

'''
def explore_list_copy_comprehensions():
    original_list = [1,2,3,4]
    # alias_list = original_list
    # print(f'Original ,{original_list}, Alias,{alias_list}')
    # original_list.append(77)
    # print(f'Original ,{original_list}, Alias,{alias_list}')

    # b_list = list(original_list)
    # print(f'Original ,{original_list}, b_list ",{b_list}')
    # original_list.append(89)
    # print(f'Original ,{original_list}, b_list ",{b_list}')

    # c_list = []
    # for item in original_list:
    #     c_list.append(item)
    # print(f'Original ,{original_list}, c_list ",{c_list}')
    # original_list.append(98)
    # print(f'Original ,{original_list}, c_list ",{c_list}')

    # d_list = [] + original_list
    # print(f'Original ,{original_list}, d_list ,{d_list}')
    # original_list.append(100)
    # print(f'Original ,{original_list}, d_list ,{d_list}')

    #List Comprehensions
    squares = [n**2 for n in original_list]  # 1*1, 2*2, 3*3 ...
    small = [n for n in original_list if n < 10]
    lengths = [len(s) for s in ["Computer", "Macbook", "iPad"]]
    print(squares)
    print(small)
    print(lengths)

def calc_avg():
    grades = [88, 92,79,85]
    total = 0
    for g in grades:
        total += g
    avg = total/len(grades)
    print("total:", total, "avg:", round(avg, 2))

    with open("grades.txt", "w") as f:
        for g in grades:
            f.write(str(g) + "\n")

    with open("grades.txt", "r") as f:
        lines = f.readlines()
    loaded = [int(line.strip()) for line in lines]
    print("Loaded file:", loaded)

def explore_2d_list():
    matrix = [
        [1, 2, 3],   # row 0
        [4, 5, 6],   # row 1
        [7, 8, 9],   # row 2
    ]

    #access cell value
    # print(matrix[1][2])
    # print(matrix)

    #iterate all elements
    for r in range(len(matrix)):
        print(r)
        for c in range(len(matrix[r])):
            print(f"matrix[{r}][{c}] = {matrix[r][c]}" )



def explore_tuples():
     a_tuple = (40.0, -75.0)
    # print(a_tuple[1])
    #a_tuple[0] = 41.0

    # # tuple with mutable item
    #  t = (10, 20, [97, 98, 99])
    #  t[2].append(100)
    #  print(t)
    #
    # # conversions
    #  as_list = list(a_tuple)
    #  as_tuple = tuple(as_list)
    #  print(as_list, as_tuple)

def explore_plots():
    x = [0, 1, 2, 3, 4]
    y = [0, 3, 1, 5, 2]

#Line Chart
    # plt.plot(x, y, marker="o")
    # plt.title("Sales by Year")
    # plt.xlabel("Year")
    # plt.ylabel("Sales")
    # plt.xticks([0,1,2,3,4], ["2016","2017","2018","2019","2020"])
    # plt.yticks([0,1,2,3,4,5], ["$0m","$1m","$2m","$3m","$4m","$5m"])
    # plt.grid(True)
    # plt.show()

    #Bar Chart
    # left_edges = [0, 10, 20, 30, 40]
    # heights = [100, 200, 300, 400, 500]
    # plt.bar(left_edges, heights, width=5)
    # plt.xlabel("Category"); plt.ylabel("Value")
    # plt.show()

    #Pie chart
    values = [20, 60, 80, 40]
    labels = ["Q1", "Q2", "Q3", "Q4"]
    plt.pie(values, labels=labels)
    plt.title("Sales by Quarter")
    plt.show()



