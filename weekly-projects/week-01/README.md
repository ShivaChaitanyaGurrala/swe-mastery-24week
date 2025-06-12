# Algorithm Visualizer - Week 1, Day 3

Interactive visualization of sorting algorithms with step-by-step execution and performance analysis.

## 🎯 Project Overview

This project is part of the **24-Week SWE Mastery Journey** and demonstrates professional-level algorithm implementation with interactive visualization capabilities. Built using Streamlit and Plotly, it provides an educational platform for understanding how sorting algorithms work internally.

## 🚀 Features Completed

### ✅ Algorithm Implementations
- **Bubble Sort** - O(n²) time complexity, stable sorting
- **Insertion Sort** - O(n²) time complexity, stable sorting
- **Selection Sort** - O(n²) time complexity, unstable sorting
- **Quick Sort** - O(n log n) average time complexity, unstable sorting
- **Merge Sort** - O(n log n) time complexity, stable sorting ⚠️ *Simplified implementation*

### ✅ Interactive Visualization
- **Step-by-step execution** with visual highlighting of compared elements
- **Smooth animations** with adjustable speed control (0.1x to 2.0x)
- **Interactive controls**: Previous, Play/Pause, Next buttons
- **Real-time step descriptions** explaining each operation
- **Progress slider** for jumping to any step in the visualization

### ✅ Data Generation Options
- **Random Data**: Randomly generated integer arrays
- **Reverse Sorted**: Worst-case scenario for most algorithms
- **Nearly Sorted**: Best-case scenario for adaptive algorithms
- **Many Duplicates**: Testing edge cases with repeated values
- **Custom Input**: User-defined comma-separated integers

### ✅ Performance Analysis
- **Execution time measurement** for algorithm comparison
- **Step count analysis** showing algorithm efficiency
- **Complexity information** for each sorting method
- **Comparative performance table** with timing results

### ✅ Professional Code Quality
- **Type safety** with comprehensive MyPy annotations
- **Error handling** with graceful fallbacks
- **Code linting** with Ruff compliance
- **Comprehensive testing** with pytest coverage
- **Clean architecture** with separation of concerns

## 📸 Screenshots

### Main Interface with Algorithm Selection
![Algorithm Visualizer Interface](screenshot1.png)
*The main interface showing algorithm configuration, complexity information, and data generation options*

### Step-by-Step Visualization
![Quick Sort Visualization](screenshot2.png)
*Interactive bar chart showing Quick Sort in action with highlighted elements being compared*

### Performance Analysis Results
![Performance Comparison](screenshot3.png)
*Comprehensive performance analysis comparing all algorithms with execution times and step counts*

## 🛠 How to Run

### Prerequisites
- Python 3.11+
- Poetry (for dependency management)
- Git

### Installation & Setup

1. **Navigate to the project directory:**
   ```bash
   cd "D:\Software_Engineering_Resources\Course\Development\projects\swe-mastery-24week"
   ```

2. **Ensure dependencies are installed:**
   ```bash
   poetry install
   ```

3. **Launch the visualizer:**
   ```bash
   poetry run streamlit run weekly-projects/week-01/algorithm_visualizer/src/app.py
   ```

4. **Access the application:**
   - The app will open in your default browser
   - URL: `http://localhost:8501`

### Usage Instructions

1. **Select an Algorithm**: Choose from 5 sorting algorithms in the sidebar
2. **Configure Data**: Select data type and size (or input custom data)
3. **Generate Data**: Click "Generate New Data" to create test arrays
4. **Start Visualization**: Click "Start Visualization" to begin
5. **Control Playback**: Use Previous/Play/Pause/Next buttons to navigate
6. **Analyze Performance**: Run performance tests to compare algorithms

## 🧪 Testing

### Run Algorithm Tests
```bash
# Run comprehensive test suite
poetry run pytest tests/test_sorting_algorithms.py -v

# Run with coverage report
poetry run pytest tests/test_sorting_algorithms.py --cov=algorithms --cov-report=html
```

### Code Quality Checks
```bash
# Type checking
poetry run mypy weekly-projects/week-01/algorithm_visualizer/src/app.py

# Code linting
poetry run ruff check weekly-projects/week-01/algorithm_visualizer/src/app.py

# Code formatting
poetry run black weekly-projects/week-01/algorithm_visualizer/src/
```

## 📁 Project Structure

```
weekly-projects/week-01/algorithm_visualizer/
└── src/
└── app.py                  # Main Streamlit application


Core Infrastructure (Shared):
├── algorithms/sorting/         # Reusable algorithm implementations
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── quick_sort.py
│   └── merge_sort.py
└── tests/
└── test_sorting_algorithms.py  # Comprehensive algorithm tests
```

## ⚡ Performance Results

Based on test runs with 10-element arrays:

| Algorithm      | Steps | Time (seconds) | Time Complexity | Space Complexity | Stable |
|----------------|-------|----------------|-----------------|------------------|--------|
| Bubble Sort    | 70    | 0.000122      | O(n²)           | O(1)             | ✅ Yes |
| Insertion Sort | 10    | 0.000080      | O(n²)           | O(1)             | ✅ Yes |
| Selection Sort | 85    | 0.000050      | O(n²)           | O(1)             | ❌ No  |
| Quick Sort     | 46    | 0.000466      | O(n log n)      | O(log n)         | ❌ No  |
| Merge Sort     | 2     | 0.000017      | O(n log n)      | O(n)             | ✅ Yes |

*Results may vary based on input data and system performance*

## ⚠️ Known Issues

### Merge Sort Step Tracking
- **Issue**: The merge sort implementation has a bug in step-by-step tracking that causes element duplication in visualization steps
- **Current Status**: Simplified to show only start and end states to prevent crashes
- **Impact**: Users can see the final sorted result but not the detailed merge process
- **Workaround**: The standard merge sort algorithm works correctly; only the step tracking is affected
- **Future Fix**: Planned for Week 2 when revisiting algorithm implementations

### Browser Compatibility
- **Recommendation**: Use Chrome, Firefox, or Edge for best experience
- **Known Issue**: Safari may have minor CSS rendering differences

## 🎓 Learning Outcomes

By completing this project, you will understand:

- **Algorithm Implementation**: Deep knowledge of 5 fundamental sorting algorithms
- **Time/Space Complexity**: Practical understanding of Big O notation
- **Data Visualization**: Creating educational, interactive visualizations
- **Web Development**: Building responsive applications with Streamlit
- **Performance Analysis**: Measuring and comparing algorithm efficiency
- **Software Testing**: Writing comprehensive test suites
- **Type Safety**: Professional Python development with MyPy
- **Project Organization**: Clean architecture and code structure

## 🚀 Next Steps

**Day 4 Preview**: Performance Benchmarking Suite
- Advanced performance measurement tools
- Statistical analysis of algorithm behavior
- Memory usage profiling
- Scalability testing with larger datasets
- Detailed complexity analysis

## 📊 Success Metrics

- ✅ **Functionality**: 4/5 algorithms working with visualization
- ✅ **Code Quality**: Type-safe, tested, and linted
- ✅ **User Experience**: Intuitive interface with clear feedback
- ✅ **Performance**: Real-time visualization without lag
- ✅ **Documentation**: Comprehensive usage instructions
- ✅ **Testing**: 80%+ test coverage for core algorithms

## 🤝 Contributing

This project is part of a personal learning journey, but feedback and suggestions are welcome:

1. Issues with algorithm implementations
2. UI/UX improvement suggestions
3. Performance optimization ideas
4. Additional algorithm requests

## 📝 License

This project is part of the SWE Mastery Journey and is intended for educational purposes.

---

**Project completed as part of Week 1, Day 3 of the 24-Week Software Engineering Mastery Program**

*Building professional-grade software, one algorithm at a time* 🚀
