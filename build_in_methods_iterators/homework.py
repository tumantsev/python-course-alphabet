from typing import List, Dict, Union, Generator
import string
import random

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for d in data:
        if d.get('name') is not None:
            d['name'] = d['name'].title()
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for key in redundant_keys:
        for x in range(len(data)):
            if key in data[x].keys():
                del data[x][key]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [d for d in data if value in d.values()]


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    return min(data, default=None)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shortest string
    """

    return min((str(i) for i in data), default=None, key=len)


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    check_data = [x for x in data if x.get('age', None)]
    return min(check_data, key=lambda x: x.get(key))


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    return max([max(x) for x in data if x != []])


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    return sum(ord(i) for i in text)


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    for num in range(2, 201):
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           yield num


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    return list((random.choice(string.ascii_lowercase) for x in range(20) ))
