# Pandas
### Data analysis using Pandas
-  **Pandas** is the most popular python library that is used for data analysis. It provides highly optimized performance with back-end source code is purely written in C or Python.

```sh
We can analyze data in pandas with:

1. Series
2. DataFrames
```
#### Series:
- Series is one dimensional(1-D) array defined in pandas that can be used to store any data type.
- **Code #1: Creating Series**

```sh
Program to create series
import pandas as pd  # Import Panda Library

Data = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Index = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Create series with Data, and Index
a = pd.Series(Data, Index)
print(a)
```