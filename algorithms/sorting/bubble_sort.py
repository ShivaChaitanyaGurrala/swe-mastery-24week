"""
Bubble Sort Implementation
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

from typing import Any


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Standard bubble sort implementation.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list of integers
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Early termination if no swaps occurred
        if not swapped:
            break

    return arr


def bubble_sort_with_steps(arr: list[int]) -> list[dict[str, Any]]:
    """
    Bubble sort with step-by-step tracking for visualization.

    Args:
        arr: List of integers to sort

    Returns:
        List of steps, each containing array state, highlights, and description
    """
    steps = []
    arr = arr.copy()
    n = len(arr)

    # Initial state
    steps.append(
        {
            "array": arr.copy(),
            "highlights": [],
            "description": f"Starting insertion sort with {n} elements",
        }
    )

    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparison step
            steps.append(
                {
                    "array": arr.copy(),
                    "highlights": [j, j + 1],
                    "description": f"Comparing {arr[j]} and {arr[j + 1]}",
                }
            )

            if arr[j] > arr[j + 1]:
                # Do the swap FIRST
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # THEN record the step
                steps.append(
                    {
                        "array": arr.copy(),
                        "highlights": [j, j + 1],
                        "description": f"Swapped {arr[j + 1]} and {arr[j]}",  # Note: values are swapped now
                    }
                )

    # Final state
    steps.append(
        {"array": arr.copy(), "highlights": [], "description": "Bubble sort complete!"}
    )

    return steps
