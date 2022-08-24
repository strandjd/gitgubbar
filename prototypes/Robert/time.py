import time
start = time.process_time()


for i in range(1,500):
    print(i)

print(time.process_time() - start)


# Importing the library
import psutil

# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))
