"""
Quick Sort Implementation
Time Complexity: O(n log n) average, O(n²) worst
Space Complexity: O(log n)
Stable: No
"""

from typing import Any


def quick_sort(arr: list[int]) -> list[int]:
    """
    Standard quick sort implementation.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list of integers
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_with_steps(arr: list[int]) -> list[dict[str, Any]]:
    """
    Quick sort with step-by-step tracking for visualization.

    Args:
        arr: List of integers to sort

    Returns:
        List of steps, each containing array state, highlights, and description
    """
    steps = []
    arr = arr.copy()

    # Initial state
    steps.append(
        {
            "array": arr.copy(),
            "highlights": [],
            "description": f"Starting quick sort with {len(arr)} elements",
        }
    )

    def partition(arr: list[int], low: int, high: int) -> int:
        """Partition function for quick sort."""
        pivot = arr[high]

        steps.append(
            {
                "array": arr.copy(),
                "highlights": [high],
                "description": f"Pivot selected: {pivot} at position {high}",
            }
        )

        i = low - 1  # Index of smaller element

        for j in range(low, high):
            steps.append(
                {
                    "array": arr.copy(),
                    "highlights": [j, high],
                    "description": f"Comparing {arr[j]} with pivot {pivot}",
                }
            )

            if arr[j] <= pivot:
                i += 1
                if i != j:
                    steps.append(
                        {
                            "array": arr.copy(),
                            "highlights": [i, j],
                            "description": f"Swapping {arr[i]} and {arr[j]}",
                        }
                    )
                    arr[i], arr[j] = arr[j], arr[i]

        # Place pivot in correct position
        if i + 1 != high:
            steps.append(
                {
                    "array": arr.copy(),
                    "highlights": [i + 1, high],
                    "description": f"Placing pivot {pivot} at position {i + 1}",
                }
            )
            arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def quick_sort_recursive(arr: list[int], low: int, high: int) -> None:
        """Recursive quick sort function."""
        if low < high:
            pi = partition(arr, low, high)

            steps.append(
                {
                    "array": arr.copy(),
                    "highlights": [pi],
                    "description": f"Partition complete. Pivot {arr[pi]} is in final position",
                }
            )

            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    if len(arr) > 1:
        quick_sort_recursive(arr, 0, len(arr) - 1)

    # Final state
    steps.append(
        {"array": arr.copy(), "highlights": [], "description": "Quick sort complete!"}
    )

    return steps
