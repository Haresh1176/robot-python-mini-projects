def robot_assistant():
    name = input("Enter robot name: ")
    battery = int (input("Enter battery level: "))
    mode = input("Enter robot mode (Idle/Active/Shutdown): ").lower()

    if battery < 20:
        battery_status = "low battery"

    elif battery <= 70:
        battery_status = "battery okay"

    else:
        battery_status = "fully charged"

    if mode == "idle":
        mode_status  = "Waiting"

    elif mode == "active":
        mode_status = "working"

    elif mode == "shutdown":
        mode_status = "Shutting down"

    else:
        mode_status = "invalid mode"

    return f"\nrobot: {name}\nbattery: {battery}%({battery_status})\nmode: {mode_status}"

print(robot_assistant())