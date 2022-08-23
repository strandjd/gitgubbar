# https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/

import time
start = time.process_time()


for i in range(1,500):
    print(i)

print(time.process_time() - start)
#import psutil
  
# Calling psutil.cpu_precent() for 4 seconds
# print('The CPU usage is: ', psutil.cpu_percent(4))


# import os
# import psutil
  
# # Getting loadover15 minutes
# load1, load5, load15 = psutil.getloadavg()
  
# cpu_usage = (load15/os.cpu_count()) * 100
  
# print("The CPU usage is : ", cpu_usage)


# Importing the library
# import psutil

# # Getting % usage of virtual_memory ( 3rd field)
# print('RAM memory % used:', psutil.virtual_memory()[2])


# import os

# # Getting all memory using os.popen()
# total_memory, used_memory, free_memory = map(
#     int, os.popen('free -t -m').readlines()[-1].split()[1:])
  
# # Memory usage
# print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))


# Importing the library
# import psutil

# # Getting % usage of virtual_memory ( 3rd field)
# print('RAM memory % used:', psutil.virtual_memory()[2])



# https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python

# from __future__ import print_function
# import psutil
# print(psutil.cpu_percent())
# print(psutil.virtual_memory())  # physical memory usage
# print('memory % used:', psutil.virtual_memory()[2])


# import os
# import psutil
# pid = os.getpid()
# python_process = psutil.Process(pid)
# memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB...I think
# print('memory use:', memoryUse)


# from tqdm import tqdm
# from time import sleep
# import psutil

# with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
#     while True:
#         rambar.n=psutil.virtual_memory().percent
#         cpubar.n=psutil.cpu_percent()
#         rambar.refresh()
#         cpubar.refresh()
#         sleep(0.5)


import os
mem=str(os.popen('free -t -m').readlines())
"""
Get a whole line of memory output, it will be something like below
['             total       used       free     shared    buffers     cached\n', 
'Mem:           925        591        334         14         30        355\n', 
'-/+ buffers/cache:        205        719\n', 
'Swap:           99          0         99\n', 
'Total:        1025        591        434\n']
 So, we need total memory, usage and free memory.
 We should find the index of capital T which is unique at this string
"""
T_ind=mem.index('T')
"""
Than, we can recreate the string with this information. After T we have,
"Total:        " which has 14 characters, so we can start from index of T +14
and last 4 characters are also not necessary.
We can create a new sub-string using this information
"""
mem_G=mem[T_ind+14:-4]
"""
The result will be like
1025        603        422
we need to find first index of the first space, and we can start our substring
from from 0 to this index number, this will give us the string of total memory
"""
S1_ind=mem_G.index(' ')
mem_T=mem_G[0:S1_ind]
"""
Similarly we will create a new sub-string, which will start at the second value. 
The resulting string will be like
603        422
Again, we should find the index of first space and than the 
take the Used Memory and Free memory.
"""
mem_G1=mem_G[S1_ind+8:]
S2_ind=mem_G1.index(' ')
mem_U=mem_G1[0:S2_ind]

mem_F=mem_G1[S2_ind+8:]
print('Summary = ' + mem_G)
print('Total Memory = ' + mem_T +' MB')
print('Used Memory = ' + mem_U +' MB')
print('Free Memory = ' + mem_F +' MB')