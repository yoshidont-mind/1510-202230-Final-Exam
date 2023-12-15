"""

FUNCTION:
_________

Define a function called merge(first, second). This function accepts two sorted lists called
first and second and returns a new sorted list that contains the elements from first and second.

ASSUMPTIONS (PRECONDITIONS):
____________

The lists passed as parameters, first and second, may not be modified, not even temporarily.

The lists passed as parameters must be pre-sorted.

The lists will always be homogenous and the same types, so they are sortable and can be merged.

The lists can be strings or some other sortable like numbers.

Sample usage example 1:

some_list = [1, 5, 9]
some_other_list = [-10, 44, 100]
sorted_merge = merge(some_list, some_other_list)
print(sorted_merge)
[-10, 1, 5, 9, 44, 100]

Sample usage example 2:

some_list = ["apple", "orange", "tamarind"]
some_other_list = ["applesauce", "bread", "watermelon"]
sorted_merge = merge(some_list, some_other_list)
print(sorted_merge)
["apple", "applesauce", "bread", "orange", "tamarind", "watermelon"]

DOCSTRING:
__________

Yes. Docstrings are needed.

DOCTESTS:
_________

Yes. Two doctests are needed.

UNIT TESTS:
___________

No. No unit tests are needed.

MAIN FUNCTION AND IF-STATEMENT BELOW IT
_______________________________________

Yes. The main function should invoke your function with a simple example.

"""


def merge(first, second):
    """
    Merge the given lists.

    :param first: a list of sortable object that is pre-sorted
    :param second: a list of sortable object that is pre-sorted
    :precondition: first must be a list
    :precondition: elements of first must be sortable
    :precondition: elements of first must be pre-sorted
    :precondition: second must be a list
    :precondition: elements of second must be sortable
    :precondition: elements of second must be pre-sorted
    :postcondition: a new sorted list that contains the elements from first and second is returned
    :return: a new sorted list that contains the elements from first and second
    >>> some_list = [1, 5, 9]
    >>> some_other_list = [-10, 44, 100]
    >>> merge(some_list, some_other_list)
    [-10, 1, 5, 9, 44, 100]
    >>> some_list = ["apple", "orange", "tamarind"]
    >>> some_other_list = ["applesauce", "bread", "watermelon"]
    >>> merge(some_list, some_other_list)
    ['apple', 'applesauce', 'bread', 'orange', 'tamarind', 'watermelon']
    """
    # set initial values
    new_list = []
    index_first = 0
    index_second = 0

    # append elements to new_list until reaching end of either first or second
    while index_first < len(first) and index_second < len(second):
        if first[index_first] < second[index_second]:
            new_list.append(first[index_first])
            index_first += 1
        else:
            new_list.append(second[index_second])
            index_second += 1

    # append remaining elements
    new_list += first[index_first:]
    new_list += second[index_second:]

    return new_list


def main():
    some_list = ["chris", "nabil", "sam"]
    some_other_list = ["hoda", "maryam"]
    print(f"When you merge {some_list} and {some_other_list}, the result is:\n {merge(some_list, some_other_list)}")


if __name__ == "__main__":
    main()
