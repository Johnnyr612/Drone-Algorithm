from djitellopy import TelloSwarm
from time import sleep

telloDancers = TelloSwarm.fromIps(["192.168.0.100", "192.168.0.102"])

telloDancers.connect()
sleep(3)

# added things for mission pads
telloDancers.enable_mission_pads()
telloDancers.set_mission_pad_detection_direction(2)

sleep(1)

# gets battery of each tello drone
for tello in telloDancers:
    print(tello.get_battery())


print("Tello count: {}".format(len(telloDancers)))
print("ready for takeoff")

telloDancers.takeoff()
print("takeoff successful")
distance = 80

def doStuff1(i, tello):
    if i == 0:
        tello.go_xyz_speed_mid(0, 0, 60, 50, 2)
        telloDancers.sync()

    if i == 1:
        tello.go_xyz_speed_mid(0, 0, 60, 50, 3)
        telloDancers.sync()
    # make all other drones wait for one to complete its flip

def doStuff2(i, tello):
    if i == 0:
        tello.go_xyz_speed_mid(0, 0, 60, 50, 4)
        telloDancers.sync()

    if i == 1:
        tello.go_xyz_speed_mid(0, 0, 60, 50, 1)
        telloDancers.sync()
    # make all other drones wait for one to complete its flip


telloDancers.parallel(lambda i, tello: tello.move_forward(distance))
telloDancers.parallel(doStuff1)
print("pad 1 successful")
telloDancers.parallel(lambda i, tello: tello.rotate_counter_clockwise(90))
print("first rotation successful")
telloDancers.parallel(lambda i, tello: tello.move_forward(distance))
telloDancers.parallel(lambda i, tello: tello.rotate_counter_clockwise(90))
print("second rotation successful")
telloDancers.parallel(doStuff2)
print("pad 2 successful")
telloDancers.land()
telloDancers.end()


# Uncomment to use algorithm
"""""
telloDancers.takeoff()
sleep(1)
telloDancers.rotate_counter_clockwise(180)
print("turn successful")
sleep(2)
telloDancers.parallel(lambda i, tello: tello.move_up(50 + i * 10))
print("move up successful")
sleep(2)
telloDancers.sequential(lambda i, tello: tello.move_forward(i * 20 + 45))
print("move forward successful")
sleep(2)
telloDancers.rotate_counter_clockwise(90)
print("turn successful")
sleep(2)
telloDancers.parallel(lambda i, tello: tello.flip("f"))
print("flip successful")
sleep(2)
telloDancers.rotate_counter_clockwise(90)
print("rotation successful")
sleep(1)
telloDancers.parallel(lambda i, tello: tello.flip("l"))
print("flip left successful")
sleep(2)
telloDancers.land()
print("landing successful")
telloDancers.end()
"""""

"""""
telloDancers.sequential(lambda i, tello: tello.move_forward(i * 20 + 45))
print("turn seccessful")
sleep(2)
telloDancers.land()
print("landing successful")
sleep(1)
telloDancers.end()
"""""
