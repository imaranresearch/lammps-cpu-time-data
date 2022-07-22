# lammps-cpu-time-data
A python module to extract the CPU time breakdown time and total wall time from lammps log file

### Basic usage

```python 

import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import logfileCPU as cputime


process_time,wall_time = cputime.cpu_timebreakdown("path/to/logfile")
process_time.head()

```
