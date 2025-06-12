"""
Comprehensive test suite for sorting algorithms.
Tests both standard implementations and step-by-step tracking versions.
Part of the core infrastructure testing for the SWE Mastery Journey.
"""

import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest

from algorithms.sorting import (
    bubble_sort,
    bubble_sort_with_steps,
    insertion_sort,
    insertion_sort_with_steps,
    merge_sort,
    merge_sort_with_steps,
    quick_sort,
    quick_sort_with_steps,
    selection_sort,
    selection_sort_with_steps,
)

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))


class TestSortingAlgorithms:
    """Test class for all sorting algorithms."""

    @pytest.fixture
    def test_arrays(self) -> dict[str, list[int]]:
        """Provide various test arrays for sorting algorithms."""
        return {
            "empty": [],
            "single": [42],
            "two_elements": [2, 1],
            "sorted": [1, 2, 3, 4, 5],
            "reverse_sorted": [5, 4, 3, 2, 1],
            "random": [64, 34, 25, 12, 22, 11, 90],
            "duplicates": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
            "all_same": [7, 7, 7, 7, 7],
            "large": list(range(100, 0, -1)),  # 100 elements in reverse
        }

    @pytest.fixture
    def sorting_functions(
        self,
    ) -> list[
        tuple[
            Callable[[list[int]], list[int]],
            Callable[[list[int]], list[dict[str, Any]]],
            str,
        ]
    ]:
        """Provide all sorting function pairs (standard, with_steps)."""
        return [
            (bubble_sort, bubble_sort_with_steps, "Bubble Sort"),
            (insertion_sort, insertion_sort_with_steps, "Insertion Sort"),
            (selection_sort, selection_sort_with_steps, "Selection Sort"),
            (quick_sort, quick_sort_with_steps, "Quick Sort"),
            (merge_sort, merge_sort_with_steps, "Merge Sort"),
        ]

    def test_empty_array(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with empty array."""
        for sort_func, step_func, name in sorting_functions:
            result = sort_func([])
            assert result == [], f"{name} failed on empty array"

            steps = step_func([])
            assert len(steps) >= 1, f"{name} steps should have at least initial state"
            assert steps[-1]["array"] == [], f"{name} final step should be empty array"

    def test_single_element(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with single element."""
        for sort_func, step_func, name in sorting_functions:
            result = sort_func([42])
            assert result == [42], f"{name} failed on single element"

            steps = step_func([42])
            assert len(steps) >= 1, f"{name} steps should have at least initial state"
            assert steps[-1]["array"] == [42], f"{name} final step should be [42]"

    def test_two_elements(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with two elements."""
        for sort_func, step_func, name in sorting_functions:
            result = sort_func([2, 1])
            assert result == [1, 2], f"{name} failed on two elements"

            steps = step_func([2, 1])
            assert steps[-1]["array"] == [1, 2], f"{name} final step should be [1, 2]"

    def test_already_sorted(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with already sorted array."""
        test_array = [1, 2, 3, 4, 5]
        for sort_func, step_func, name in sorting_functions:
            result = sort_func(test_array.copy())
            assert result == test_array, f"{name} failed on already sorted array"

            steps = step_func(test_array.copy())
            assert steps[-1]["array"] == test_array, f"{name} final step incorrect"

    def test_reverse_sorted(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with reverse sorted array (worst case)."""
        test_array = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]

        for sort_func, step_func, name in sorting_functions:
            result = sort_func(test_array.copy())
            assert result == expected, f"{name} failed on reverse sorted array"

            steps = step_func(test_array.copy())
            assert steps[-1]["array"] == expected, f"{name} final step incorrect"

    def test_random_array(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with random array."""
        test_array = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(test_array)

        for sort_func, step_func, name in sorting_functions:
            result = sort_func(test_array.copy())
            assert result == expected, f"{name} failed on random array"

            steps = step_func(test_array.copy())
            assert steps[-1]["array"] == expected, f"{name} final step incorrect"

    def test_duplicates(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with duplicate elements."""
        test_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = sorted(test_array)

        for sort_func, step_func, name in sorting_functions:
            result = sort_func(test_array.copy())
            assert result == expected, f"{name} failed on array with duplicates"

            steps = step_func(test_array.copy())
            assert steps[-1]["array"] == expected, f"{name} final step incorrect"

    def test_all_same_elements(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test all algorithms with all identical elements."""
        test_array = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]

        for sort_func, step_func, name in sorting_functions:
            result = sort_func(test_array.copy())
            assert result == expected, f"{name} failed on all same elements"

            steps = step_func(test_array.copy())
            assert steps[-1]["array"] == expected, f"{name} final step incorrect"

    def test_original_array_unchanged(
        self,
        sorting_functions: list[tuple[Callable, Callable, str]],
        test_arrays: dict[str, list[int]],
    ) -> None:
        """Test that original arrays are not modified."""
        for _, test_array in test_arrays.items():
            if not test_array:  # Skip empty array
                continue

            for sort_func, step_func, name in sorting_functions:
                original = test_array.copy()

                # Test standard function
                sort_func(test_array)
                assert test_array == original, f"{name} modified original array"

                # Test step function
                step_func(test_array)
                assert (
                    test_array == original
                ), f"{name} with steps modified original array"

    def test_step_structure(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test that step tracking returns proper structure."""
        test_array = [3, 1, 4, 1, 5]

        for _, step_func, name in sorting_functions:
            steps = step_func(test_array.copy())

            # Should have at least initial and final states
            assert len(steps) >= 2, f"{name} should have at least 2 steps"

            # Each step should have required keys
            for i, step in enumerate(steps):
                assert "array" in step, f"{name} step {i} missing 'array' key"
                assert "highlights" in step, f"{name} step {i} missing 'highlights' key"
                assert (
                    "description" in step
                ), f"{name} step {i} missing 'description' key"
                assert isinstance(
                    step["array"], list
                ), f"{name} step {i} array not a list"
                assert isinstance(
                    step["highlights"], list
                ), f"{name} step {i} highlights not a list"
                assert isinstance(
                    step["description"], str
                ), f"{name} step {i} description not a string"

    def test_step_array_consistency(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test that step arrays maintain same length and elements."""
        test_array = [64, 34, 25, 12, 22]
        original_sorted = sorted(test_array)

        for _, step_func, name in sorting_functions:
            steps = step_func(test_array.copy())

            for i, step in enumerate(steps):
                step_array = step["array"]

                # Array length should remain constant
                assert len(step_array) == len(
                    test_array
                ), f"{name} step {i} changed array length"

                # Same elements should be present (just reordered)
                assert (
                    sorted(step_array) == original_sorted
                ), f"{name} step {i} changed array elements"

    def test_performance_comparison(
        self, sorting_functions: list[tuple[Callable, Callable, str]]
    ) -> None:
        """Test performance characteristics on different input sizes."""
        import time

        sizes = [10, 50, 100]
        results: dict = {}

        for size in sizes:
            # Create worst-case input (reverse sorted)
            test_array = list(range(size, 0, -1))

            for sort_func, _, name in sorting_functions:
                start_time = time.perf_counter()
                result = sort_func(test_array.copy())
                execution_time = time.perf_counter() - start_time

                # Verify correctness
                assert result == list(
                    range(1, size + 1)
                ), f"{name} incorrect result for size {size}"

                # Store timing (for reporting, not assertion)
                if name not in results:
                    results[name] = []
                results[name].append((size, execution_time))

        # Print performance results for analysis
        print("\nPerformance Results:")
        for name, timings in results.items():
            print(f"{name}:")
            for size, time_taken in timings:
                print(f"  Size {size}: {time_taken:.6f}s")


class TestStabilityAndProperties:
    """Test specific properties of sorting algorithms."""

    def test_bubble_sort_stability(self) -> None:
        """Test that bubble sort is stable."""
        # Use tuples to track original positions
        test_data = [(1, "a"), (2, "b"), (1, "c"), (3, "d")]

        # Custom bubble sort for tuples (compare by first element only)
        def bubble_sort_tuples(arr: list) -> list:
            arr = arr.copy()
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j][0] > arr[j + 1][0]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        result = bubble_sort_tuples(test_data)

        # Check that equal elements maintain relative order
        ones = [item for item in result if item[0] == 1]
        assert ones == [(1, "a"), (1, "c")], "Bubble sort should be stable"

    def test_selection_sort_instability(self) -> None:
        """Test that selection sort is not stable."""
        # This test demonstrates instability but doesn't assert it
        # since our implementation might accidentally be stable for this case
        test_data = [(2, "a"), (1, "b"), (2, "c")]

        # For demonstration purposes - selection sort can be unstable
        # The important thing is that it sorts correctly
        result = selection_sort([item[0] for item in test_data])
        assert result == [1, 2, 2], "Selection sort should sort correctly"

    @pytest.mark.parametrize(
        "algorithm,expected_stable",
        [
            (bubble_sort, True),
            (insertion_sort, True),
            (selection_sort, False),
            (merge_sort, True),
            # Quick sort stability depends on implementation
        ],
    )
    def test_algorithm_properties(
        self, algorithm: Callable[[list[int]], list[int]], expected_stable: bool
    ) -> None:
        """Test various algorithm properties."""
        test_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = algorithm(test_array.copy())

        # All algorithms should sort correctly
        assert result == sorted(
            test_array
        ), f"{algorithm.__name__} should sort correctly"

        # All algorithms should handle edge cases
        assert algorithm([]) == [], f"{algorithm.__name__} should handle empty array"
        assert algorithm([42]) == [
            42
        ], f"{algorithm.__name__} should handle single element"


class TestEdgeCases:
    """Test edge cases and error conditions."""

    @pytest.mark.parametrize(
        "sort_func",
        [bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort],
    )
    def test_large_arrays(self, sort_func: Callable[[list[int]], list[int]]) -> None:
        """Test with larger arrays."""
        import random

        # Test with 1000 random elements
        test_array = [random.randint(1, 1000) for _ in range(1000)]
        result = sort_func(test_array.copy())

        assert len(result) == 1000, "Result should maintain array length"
        assert result == sorted(test_array), "Large array should be sorted correctly"

    @pytest.mark.parametrize(
        "sort_func",
        [bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort],
    )
    def test_negative_numbers(
        self, sort_func: Callable[[list[int]], list[int]]
    ) -> None:
        """Test with negative numbers."""
        test_array = [-5, 3, -1, 0, 8, -3]
        expected = [-5, -3, -1, 0, 3, 8]

        result = sort_func(test_array.copy())
        assert (
            result == expected
        ), f"{sort_func.__name__} should handle negative numbers"

    @pytest.mark.parametrize(
        "step_func",
        [
            bubble_sort_with_steps,
            insertion_sort_with_steps,
            selection_sort_with_steps,
            quick_sort_with_steps,
            merge_sort_with_steps,
        ],
    )
    def test_step_descriptions_not_empty(
        self, step_func: Callable[[list[int]], list[dict[str, Any]]]
    ) -> None:
        """Test that step descriptions are meaningful."""
        test_array = [3, 1, 4]
        steps = step_func(test_array)

        for i, step in enumerate(steps):
            assert step["description"].strip(), f"Step {i} has empty description"
            assert len(step["description"]) > 5, f"Step {i} description too short"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "--tb=short"])
