world_record = float(input())
distance = float(input())
time_for_meter = float(input())

time = distance * time_for_meter
# distance_slowing = math.floor(distance / 15) * 12.5
distance_slowing = (distance // 15) * 12.5
total_time = time + distance_slowing

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_needed = total_time - world_record
    print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")
