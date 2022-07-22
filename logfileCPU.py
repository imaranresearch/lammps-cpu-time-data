#import numpy as np
#import pandas as pd
#import matplotlib.pylab as plt
'''



'''
import numpy as np
import pandas as pd

def cpu_timebreakdown(str):
    data_frame = open(str,"r+")
    contents = data_frame.readlines()
    cpu_time_strings = ("Comm","Pair",'Neigh   ',"Output","Modify","Output")
    cpu_use_string = "Loop"
    wall_time =0

    algorithm = []
    relative_time_percentage = []

    for line in contents:
        if (line.startswith(cpu_time_strings)==True):
            data1 = (line.split('|'))
            # print(data1[0],data1[len(data1)-1])
            algorithm.append(data1[0].strip())
            relative_time_percentage.append(float(data1[len(data1)-1]))
        if (line.startswith(cpu_use_string)):
            wall_time=wall_time+(float(line.split()[3]))
    cpu_use_percentage = pd.DataFrame([np.array(relative_time_percentage)],columns=np.array(algorithm))
    #wall_time = wall_time_local
    return cpu_use_percentage,wall_time

#if __name__ == "__main__":
#    logfileCPU()
