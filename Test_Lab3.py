import Lab3

print("Test_Lab3")


#def test_bubble_sort_ascending():
    #result = []
    #input_arr = [64, 34, 25, 12, 22, 11, 90]
    #test_arr = [11, 12, 22, 25, 34, 64, 90]

    #result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    #assert (result == test_arr)

#def test_bubble_sort_descending():
    #result = []
    #input_arr = [64, 34, 25, 12, 22, 11, 90, 91, 92]
    #test_arr = [92, 91, 90, 64, 34, 25, 22, 12, 11]

    #result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    #assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_REQ01ASCEND():
    result =[]
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    test_arr = [1,2,3,4,5,6,7,8,9,10]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == test_arr)

def test_bubble_sort_REQ01DESCEND():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_arr = [10,9,8,7,6,5,4,3,2,1]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == test_arr)
def test_bubble_sort_REQ02():
    result = []
    input_arr=[1,2,3,4,5,6,7,8,9,10,11]
    test_result=1
    result=Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert(result == test_result)
def test_bubble_sort_REQ03():
    result=[]
    input_arr=[1]
    test_result=2
    result=Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert(result==test_result)
def test_bubble_sort_REQ04():
    result=[]
    input_arr=[]
    test_result=0
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert(result==test_result)
def test_bubble_sort_REQ05():
    result=[]
    input_arr=['gay']
    test_result=3
    result=Lab3.bubble_sort(input_arr,Lab3.SORT_NOINT)
    assert(result==test_result)

