from typing import List

def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Фильтрует список, возвращая только четные числа.
    
    Args:
        numbers: Список целых чисел.
        
    Returns:
        Список четных чисел.
    """
    return [num for num in numbers if num % 2 == 0] 
