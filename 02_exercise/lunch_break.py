import math

series_name = input()
episode_time = int(input())
lunch_break = int(input())

lunch_time = lunch_break * 1/8
break_time = lunch_break * 1/4
time_left = lunch_break - lunch_time - break_time

if time_left >= episode_time:
    free_time = math.ceil(time_left - episode_time)
    print(f"You have enough time to watch {series_name} and left with {free_time} minutes free time.")
else:
    needed_time = math.ceil(episode_time - time_left)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")
