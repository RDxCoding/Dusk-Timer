import time

my_time = int(input("enter the time in second="))

for t in range(my_time,0,-1):

    sec = int(t%60)

    min = int((t/60)%60)

    hour = int(t/3600)

    print(f"{hour:02}:{min:02}:{sec:02}")


    time.sleep(1)


print("Times up!")






    
