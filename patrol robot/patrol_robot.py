class patrol_robot:
    def __init__(self,name,battery):
        self.name=name
        self.battery=battery

    def status(self):
        print(f"{self.name}| battery is {self.battery}%")

    def patrol(self,zone):
        print(f"{self.name} preparing to patrol {zone}")

        if self.battery < 30:
            print("Battery level is low please charge ")

        else:
             if zone=="A":
                 print("patrol zone is A:main entrance")
             elif    zone =="B":
                 print("patrol zone is B:storage area")
             elif zone=="C":
                 print("patrol zone is C:quality control")
             else:
                 print("invalid zone")
             self.battery -= 25
             print(f"updated battery level:{self.battery}%")

robot = patrol_robot("optimus",70)
robot.status()
robot.patrol("A")
robot.patrol("B")
robot.patrol("C")
robot.status()