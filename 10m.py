import statistics
import numpy as np

def longest_sequence(numbers):

    diffs = np.diff(numbers)  # Різниця між сусідніми числами
    indices = np.where(diffs > 0)[0]  # Індекси, де числа збільшуються
    sequences = np.split(numbers, indices + 1)  # Розбиваємо список за індексами

    max_sequence = max(sequences, key=len)  # Знаходимо найдовшу послідовність

    return list(max_sequence)

with open('/home/roman/Downloads/10m.txt', 'r') as file:
    content = file.read()
    numbers_str = content.split()
    numbers = [int(num) for num in numbers_str]
    print(max(numbers), min(numbers), statistics.median(numbers), statistics.mean(numbers), longest_sequence(numbers)[::-1], longest_sequence(numbers))