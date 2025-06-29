import time
battery=0
while battery <= 100:
    print(f"🔋charging ...[{battery}%]")
    if battery == 50:
     print("🔋battery is halfway")
    elif battery == 100:
     print("🔋battery is  fully charged!!! ")
    battery += 20
    time.sleep(1)

