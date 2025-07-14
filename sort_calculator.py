import math
import sys
from enum import Enum

class SORT_ORDER(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'

def to_float(user_input: str) -> float:
    try:
        constants = {
            'e': math.e,
            'pi': math.pi,
            'tau': math.tau,
            'inf': math.inf,
            '-inf': -math.inf,
            'infinity': math.inf,
            '-infinity': -math.inf
        }
        val = user_input.strip().lower()
        if val in constants:
            return constants[val]
        if val == 'nan':
            raise ValueError('NaN is short for Not A Number')
        return float(val)
    except ValueError as e:
        raise ValueError(f'[{user_input}] is not number [{e}]')

def converter(list: list[str]) -> list[float]:
    if len(list) == 0:
        raise ValueError(f'Input some values please')
    return [to_float(n) for n in list]

def compare_order(left: float, right: float, order: SORT_ORDER) -> bool:
    if order == SORT_ORDER.ASC:
        return left < right
    return left > right

def is_sorted(list: list[float], order: SORT_ORDER) -> bool:
    if len(list) == 1:
        return True
    for i in range(0, len(list) - 1):
        if not compare_order(list[i], list[i + 1], order):
            return False
    return True

def insert_sort(list: list[float], order: SORT_ORDER) -> list[float]:
    if is_sorted(list, order):
        return list
    for i in range(1, len(list)):
        # print(f'Start index: {i}')
        select = list[i]
        position = i - 1
        # print(f'select: {select}, start_position: {position}')
        while 0 <= position and not compare_order(list[position], select, order):
            # print(f'SHIFT: {list[position]}: {position} -> {position + 1}')
            list[position + 1] = list[position]
            position -= 1
        list[position + 1] = select
        # print(f'FINISH: {select}: {i} -> {position + 1}')
        # print(list)
        # print()
    return list

def define_order(list: list[str]):
    try:
        order = SORT_ORDER(list[1].upper()) if 1 < len(list) else SORT_ORDER.ASC
        if order == SORT_ORDER.ASC:
            message = 'Sorting in ascending order.'
        else:
            message = 'Sorting in descending order.'
        return (order, message)
    except:
        raise ValueError(f"'{sys.argv[1]}' is not a valid SORT_ORDER. Use 'ASC' or 'DESC' (without brackets).")

def main():
    try:
        order, message = define_order(sys.argv)
        print(message)
        chunk = input('Enter numeric values only: ')
        converted = converter([n for n in chunk.split(' ') if n.strip()])
        sorted = insert_sort(converted, order)
        print(f'Sorted: {sorted}')
    except ValueError as e:
        print(f'Invalid input: {e}')

if __name__ == '__main__':
    main()
