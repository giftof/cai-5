import math


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

def is_sorted(list: list[float], asc: bool = True) -> bool:
    if len(list) == 1:
        return True
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

def insert_sort(list: list[float]) -> list[float]:
    if is_sorted(list):
        return list
    return list

def main():
    try:
        chunk = input('Enter numeric values only: ')
        converted = converter([n for n in chunk.split(' ') if n.strip()])
        sorted = insert_sort(converted)
        print(f'Sorted: {sorted}')
    except ValueError as e:
        print(f'Invalid input: {e}')

if __name__ == '__main__':
    main()
