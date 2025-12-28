##  Energy Complexity Model
We propose that energy is an asymptotic measure defined by:

$$E(n) = P_{avg} \times T(n)$$

* **$E(n)$**: Total Energy (Joules)
* **$P_{avg}$**: Hardware Stress/Power Draw (Watts)
* **$T(n)$**: Execution Time (Seconds)

##  Algorithms Under Test

| Algorithm | Complexity | Resource Characteristic |
| :--- | :--- | :--- |
| **MergeSort** | $O(n \log n)$ | High memory overhead (Stable) |
| **QuickSort** | $O(n \log n)$ | CPU intensive, Cache friendly (In-place) |
| **Strassen** | $O(n^{2.81})$ | Massive recursion & CPU load |

---

##  Quick Start Guide

1️ Prerequisites
```bash
# Install visualization tools
python -m pip install pandas matplotlib openpyxl
````

2 Generate Data
``` bash
# Create randomized arrays & matrices
python generate_inputs.py
````

3 Compile Engine
``` bash
# Build C++ with O3 optimization
g++ -O3 src/main.cpp src/mergesort.cpp src/quicksort.cpp src/strassen.cpp -o build/program.exe
````

4 Run Benchmark
``` bash
# Collect Time & Energy metrics
python measure/measure.py
````

5 Visualize Results
``` bash
# Generate plots & Excel report
python measure/plot_results.py
python measure/export_excel_final.py
````

##  Key Findings

###  Asymptotic Dominance
* **Strassen ($O(n^{2.81})$)** exhibits exponential-like energy surges, dominating sorting algorithms even at small $n$.
* **Logarithmic plots** (generated in `results/`) confirm the theoretical divergence.

###  Energy Efficiency
| Algorithm | Efficiency | Why? |
| :--- | :--- | :--- |
| **QuickSort** | 🟢 **Best** | **In-place** nature reduces memory I/O & cache misses. |
| **MergeSort** | 🟡 **Medium** | **$O(n)$** auxiliary space increases RAM power draw. |
| **Strassen** | 🔴 **Worst** | Recursive depth causes extreme CPU & Memory stress. |


