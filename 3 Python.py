# Import statistics Library
import statistics

# Calculate middle values
print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))






n_num = [12,14,14,15,16,17,18]
n = len(n_num)
n_num.sort()

if n%2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 -1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("median is: " + str(median))    