"""
Merge Sort Implementation
Time Complexity: O(n log n)
Space Complexity: O(n)
Stable: Yes
"""

from typing import Any


def merge_sort(arr: list[int]) -> list[int]:
    """
    Standard merge sort implementation.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list of integers
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_with_steps(arr: list[int]) -> list[dict[str, Any]]:
    """Simplified version - just show start and end for now"""
    steps = []
    result = merge_sort(arr)  # Use the working standard version

    steps.append(
        {"array": arr.copy(), "highlights": [], "description": "Starting merge sort"}
    )
    steps.append(
        {
            "array": result.copy(),
            "highlights": [],
            "description": "Merge sort complete!",
        }
    )

    return steps
