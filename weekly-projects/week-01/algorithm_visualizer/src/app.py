"""
Algorithm Visualizer - Interactive Streamlit Application
Part of the 24-Week SWE Mastery Journey - Week 1, Day 3
"""

import sys
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from algorithms.sorting.bubble_sort import bubble_sort_with_steps
from algorithms.sorting.insertion_sort import insertion_sort_with_steps
from algorithms.sorting.merge_sort import merge_sort_with_steps
from algorithms.sorting.quick_sort import quick_sort_with_steps
from algorithms.sorting.selection_sort import selection_sort_with_steps

# Add the algorithms directory to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.append(str(project_root))


class AlgorithmVisualizer:
    """Interactive algorithm visualization using Streamlit and Plotly."""

    def __init__(self) -> None:
        self.algorithms = {
            "bubble_sort": {
                "func": bubble_sort_with_steps,
                "name": "Bubble Sort",
                "time_complexity": "O(n²)",
                "space_complexity": "O(1)",
                "stable": True,
                "description": "Repeatedly compares adjacent elements and swaps them if they are in the wrong order.",
            },
            "insertion_sort": {
                "func": insertion_sort_with_steps,
                "name": "Insertion Sort",
                "time_complexity": "O(n²)",
                "space_complexity": "O(1)",
                "stable": True,
                "description": "Builds the final sorted array one item at a time, inserting each element into its correct position.",
            },
            "selection_sort": {
                "func": selection_sort_with_steps,
                "name": "Selection Sort",
                "time_complexity": "O(n²)",
                "space_complexity": "O(1)",
                "stable": False,
                "description": "Finds the minimum element from unsorted part and puts it at the beginning.",
            },
            "quick_sort": {
                "func": quick_sort_with_steps,
                "name": "Quick Sort",
                "time_complexity": "O(n log n)",
                "space_complexity": "O(log n)",
                "stable": False,
                "description": "Divides the array into partitions around a pivot and recursively sorts the partitions.",
            },
            "merge_sort": {
                "func": merge_sort_with_steps,
                "name": "Merge Sort",
                "time_complexity": "O(n log n)",
                "space_complexity": "O(n)",
                "stable": True,
                "description": "Divides the array into halves, sorts them separately, and then merges them back together.",
            },
        }

    def generate_data(
        self, data_type: str, size: int, custom_input: str | None = None
    ) -> list[int]:
        """Generate different types of test data."""
        if data_type == "Custom" and custom_input:
            try:
                return [int(x.strip()) for x in custom_input.split(",")]
            except ValueError:
                st.error("Invalid custom input. Using random data instead.")
                return [int(x) for x in np.random.randint(1, 100, size)]

        if data_type == "Random":
            return [int(x) for x in np.random.randint(1, 100, size)]
        elif data_type == "Reverse Sorted":
            return list(range(size, 0, -1))
        elif data_type == "Nearly Sorted":
            data = list(range(1, size + 1))
            # Introduce a few random swaps
            for _ in range(max(1, size // 10)):
                i, j = np.random.choice(size, 2, replace=False)
                data[i], data[j] = data[j], data[i]
            return data
        elif data_type == "Many Duplicates":
            return [int(x) for x in np.random.randint(1, 10, size)]
        else:
            return [int(x) for x in np.random.randint(1, 100, size)]

    def create_visualization(
        self, steps: list[dict], step_idx: int, algorithm_name: str
    ) -> tuple[go.Figure, str]:
        """Create interactive Plotly visualization for current step."""
        if not steps or step_idx >= len(steps):
            return go.Figure(), "No data"

        step_data: dict[str, Any] = steps[step_idx]
        arr: list[int] = step_data["array"]
        highlights: list[int] = step_data.get("highlights", [])
        description: str = step_data.get("description", "")

        # Create colors for bars
        colors = []
        for i in range(len(arr)):
            if i in highlights:
                if len(highlights) > 1 and i == highlights[0]:
                    colors.append("#FF4444")  # Bright red for first highlight
                elif len(highlights) > 1 and i == highlights[1]:
                    colors.append("#44AAFF")  # Bright blue for second highlight
                else:
                    colors.append("#FF8800")  # Orange for other highlights
            else:
                colors.append("#666666")  # Dark gray for normal elements

        # Create the bar chart
        fig = go.Figure(
            data=[
                go.Bar(
                    x=list(range(len(arr))),
                    y=arr,
                    marker_color=colors,
                    text=[str(x) for x in arr],
                    textposition="outside",
                    hovertemplate="Index: %{x}<br>Value: %{y}<extra></extra>",
                )
            ]
        )

        fig.update_layout(
            title=f"{algorithm_name} - Step {step_idx + 1}/{len(steps)}",
            xaxis_title="Array Index",
            yaxis_title="Value",
            height=500,
            showlegend=False,
            plot_bgcolor="#f8f9fa",  # Light gray background instead of white
            paper_bgcolor="white",
            font={"size": 12},
        )

        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="lightgray")
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="lightgray")

        return fig, description


def main() -> None:
    """Main Streamlit application."""
    st.set_page_config(
        page_title="Algorithm Visualizer",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS for better styling
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 3rem;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 1rem;
        }
        .sub-header {
            font-size: 1.2rem;
            color: #666;
            text-align: center;
            margin-bottom: 2rem;
        }
        .algorithm-info {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
        .step-description {
            background-color: #e8f4fd;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #1f77b4;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<h1 class="main-header">🔍 Algorithm Visualizer</h1>', unsafe_allow_html=True
    )
    st.markdown(
        '<p class="sub-header">Interactive visualization of sorting algorithms with step-by-step execution</p>',
        unsafe_allow_html=True,
    )

    # Initialize visualizer
    visualizer = AlgorithmVisualizer()

    # Sidebar configuration
    with st.sidebar:
        st.header("🎛️ Configuration")

        # Algorithm selection
        algorithm_key = st.selectbox(
            "Choose Algorithm",
            list(visualizer.algorithms.keys()),
            format_func=lambda x: str(visualizer.algorithms[x]["name"]),
        )

        algorithm_info: dict[str, Any] = visualizer.algorithms[algorithm_key]

        # Display algorithm information
        st.markdown(
            f"""
        <div class="algorithm-info">
        <h4>{algorithm_info['name']}</h4>
        <p><strong>Time Complexity:</strong> {algorithm_info['time_complexity']}</p>
        <p><strong>Space Complexity:</strong> {algorithm_info['space_complexity']}</p>
        <p><strong>Stable:</strong> {'Yes' if algorithm_info['stable'] else 'No'}</p>
        <p><strong>Description:</strong> {algorithm_info['description']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        # Data configuration
        st.subheader("📊 Data Configuration")

        data_type = st.selectbox(
            "Data Type",
            ["Random", "Reverse Sorted", "Nearly Sorted", "Many Duplicates", "Custom"],
        )

        if data_type != "Custom":
            array_size = st.slider("Array Size", 5, 50, 15)
            custom_input = ""
        else:
            custom_input = st.text_area(
                "Enter numbers (comma-separated)", "64,34,25,12,22,11,90,45,78,23"
            )
            array_size = len(custom_input.split(",")) if custom_input else 10

        # Generate data button
        if st.button("🎲 Generate New Data", type="primary", use_container_width=True):
            st.session_state.pop("visualization_data", None)
            st.session_state.pop("steps", None)
            st.session_state.pop("current_step", None)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🎬 Visualization")

        # Generate or retrieve data
        if "visualization_data" not in st.session_state:
            st.session_state.visualization_data = visualizer.generate_data(
                data_type, array_size, custom_input
            )

        # Display current array
        with col2:
            st.subheader("📋 Current Array")
            st.code(str(st.session_state.visualization_data))

            if st.button(
                "▶️ Start Visualization", type="primary", use_container_width=True
            ):
                with st.spinner("Generating visualization steps..."):
                    try:
                        st.session_state.steps = algorithm_info["func"](
                            st.session_state.visualization_data.copy()
                        )
                        st.session_state.current_step = 0
                        st.session_state.algorithm_name = algorithm_info["name"]
                        st.success("Visualization ready!")
                    except Exception as e:
                        st.error(f"Error generating steps: {str(e)}")

        # Visualization controls and display
        if "steps" in st.session_state and st.session_state.steps:
            # Control buttons
            # Control buttons - simplified
            control_cols = st.columns(3)

            with control_cols[0]:
                if st.button("⏪ Previous", help="Previous Step"):
                    current_step = getattr(st.session_state, "current_step", 0)
                    st.session_state.current_step = max(0, current_step - 1)

            with control_cols[1]:
                if st.session_state.get("auto_play", False):
                    if st.button("⏸️ Pause", help="Pause Animation"):
                        st.session_state.auto_play = False
                else:
                    if st.button("▶️ Play", help="Start Animation"):
                        st.session_state.auto_play = True

            with control_cols[2]:
                if st.button("⏩ Next", help="Next Step"):
                    current_step = getattr(st.session_state, "current_step", 0)
                    st.session_state.current_step = min(
                        len(st.session_state.steps) - 1, current_step + 1
                    )

            # Step slider
            st.session_state.current_step = st.slider(
                "Step",
                0,
                len(st.session_state.steps) - 1,
                st.session_state.current_step,
                help=f"Current step: {st.session_state.current_step + 1} of {len(st.session_state.steps)}",
            )

            # Speed control
            speed = st.select_slider(
                "Animation Speed",
                options=[0.1, 0.3, 0.5, 1.0, 2.0],
                value=1.0,
                format_func=lambda x: f"{x}x",
            )

            # Create and display visualization
            fig, description = visualizer.create_visualization(
                st.session_state.steps,
                st.session_state.current_step,
                st.session_state.algorithm_name,
            )

            st.plotly_chart(fig, use_container_width=True)

            # Display step description
            if description:
                st.markdown(
                    f"""
                <div class="step-description">
                <strong>Step {st.session_state.current_step + 1}:</strong> {description}
                </div>
                """,
                    unsafe_allow_html=True,
                )

            # Auto-play functionality
            if st.session_state.get("auto_play", False):
                time.sleep(1.0 / speed)
                if st.session_state.current_step < len(st.session_state.steps) - 1:
                    st.session_state.current_step += 1
                    st.rerun()
                else:
                    st.session_state.auto_play = False

    # Performance Analysis Section
    st.header("📊 Performance Analysis")
    st.write("Compare algorithm performance with different input sizes and types.")

    if st.button("🏃‍♂️ Run Basic Performance Test", type="secondary"):
        st.subheader("Algorithm Comparison")

        # Simple performance comparison
        test_data = [64, 34, 25, 12, 22, 11, 90, 45, 78, 23]

        results = []
        algo_info: dict[str, Any]
        for _, algo_info in visualizer.algorithms.items():
            try:
                start_time = time.perf_counter()
                func = cast(
                    Callable[[list[int]], list[dict[str, Any]]], algo_info["func"]
                )
                steps = func(test_data.copy())
                execution_time = time.perf_counter() - start_time

                results.append(
                    {
                        "Algorithm": algo_info["name"],
                        "Steps": len(steps),
                        "Time (seconds)": f"{execution_time:.6f}",
                        "Complexity": algo_info["time_complexity"],
                    }
                )
            except Exception:
                results.append(
                    {
                        "Algorithm": algo_info["name"],
                        "Steps": "Error",
                        "Time (seconds)": "Error",
                        "Complexity": algo_info["time_complexity"],
                    }
                )

        df = pd.DataFrame(results)
        st.table(df)


if __name__ == "__main__":
    main()
