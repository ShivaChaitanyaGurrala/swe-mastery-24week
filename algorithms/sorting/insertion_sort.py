"""
Insertion Sort Implementation
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

from typing import Any


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Standard insertion sort implementation.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list of integers
    """
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def insertion_sort_with_steps(arr: list[int]) -> list[dict[str, Any]]:
    """
    Insertion sort with step-by-step tracking for visualization.

    Args:
        arr: List of integers to sort

    Returns:
        List of steps, each containing array state, highlights, and description
    """
    arr = arr.copy()  # So we don't modify the input array
    steps = [{"array": arr.copy(), "highlights": [], "description": "Initial array"}]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        steps.append(
            {
                "array": arr.copy(),
                "highlights": [j + 1, i],
                "description": f"Inserted element {key} at position {j + 1}",
            }
        )

    return steps
