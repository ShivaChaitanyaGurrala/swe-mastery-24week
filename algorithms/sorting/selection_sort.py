"""
Selection Sort Implementation
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: No
"""

from typing import Any


def selection_sort(arr: list[int]) -> list[int]:
    """
    Standard selection sort implementation.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list of integers
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_idx = i

        # Find minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def selection_sort_with_steps(arr: list[int]) -> list[dict[str, Any]]:
    """
    Selection sort with step-by-step tracking for visualization.

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
            "description": f"Starting selection sort with {n} elements",
        }
    )

    for i in range(n):
        min_idx = i

        steps.append(
            {
                "array": arr.copy(),
                "highlights": [i],
                "description": f"Finding minimum from position {i}",
            }
        )

        # Find minimum element in remaining unsorted array
        for j in range(i + 1, n):
            steps.append(
                {
                    "array": arr.copy(),
                    "highlights": [j, min_idx],
                    "description": f"Comparing {arr[j]} with current min {arr[min_idx]}",
                }
            )

            if arr[j] < arr[min_idx]:
                min_idx = j
                steps.append(
                    {
                        "array": arr.copy(),
                        "highlights": [min_idx],
                        "description": f"New minimum found: {arr[min_idx]}",
                    }
                )

        # Swap if necessary
        if min_idx != i:
            steps.append(
                {
                    "array": arr.copy(),
                    "highlights": [i, min_idx],
                    "description": f"Swapping {arr[i]} and {arr[min_idx]}",
                }
            )

            steps.append(
                {
                    "array": arr.copy(),
                    "highlights": [i],
                    "description": f"Placed {arr[i]} in position {i}",
                }
            )

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Final state
    steps.append(
        {
            "array": arr.copy(),
            "highlights": [],
            "description": "Selection sort complete!",
        }
    )

    return steps
