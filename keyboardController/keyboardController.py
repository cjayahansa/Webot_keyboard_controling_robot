
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

motor1 = robot.getDevice('motor1')
motor2 = robot.getDevice('motor2')
motor3 = robot.getDevice('motor3')
motor4 = robot.getDevice('motor4')
#left_motor = robot.getDevice('left wheel motor')

# right_motor.setPosition(float('inf'))
# left_motor.setVelocity(0.0)
motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
# motor3.setPosition(float('inf'))
motor4.setPosition(float('inf'))
motor3.setPosition(float('inf'))

motor1.setVelocity(0.0)
motor2.setVelocity(0.0)
# motor3.setVelocity(0.0)
motor4.setVelocity(0.0)
motor3.setVelocity(0.0)

# keyboard
keyboard = robot.getKeyboard()
keyboard.enable(timestep)

# speeds (tweak these numbers)

FORWARD_SPEED = 3.0
TURN_SPEED = 2.0
STOP_SPEED = 0.0

def FORWARD(FORWARD_SPEED):
     motor1.setVelocity(-1*FORWARD_SPEED)
     motor2.setVelocity(-1*FORWARD_SPEED)
     motor4.setVelocity(-1*FORWARD_SPEED)
     motor3.setVelocity(-1*FORWARD_SPEED)
    
    
def REVERSE(FORWARD_SPEED):
     motor1.setVelocity(FORWARD_SPEED)
     motor2.setVelocity(FORWARD_SPEED)
     motor4.setVelocity(FORWARD_SPEED)
     motor3.setVelocity(FORWARD_SPEED)
     
     
     
def TURN_LEFT(TURN_SPEED):
     motor1.setVelocity(-1*TURN_SPEED)
     motor2.setVelocity(-1*TURN_SPEED)
     motor4.setVelocity(TURN_SPEED)
     motor3.setVelocity(TURN_SPEED)
  
  
def TURN_RIGHT(TURN_SPEED):
     motor1.setVelocity(TURN_SPEED)
     motor2.setVelocity(TURN_SPEED)
     motor4.setVelocity(-1*TURN_SPEED)
     motor3.setVelocity(-1*TURN_SPEED)
  
  
  
while robot.step(timestep) != -1:

    FORWARD_SPEED = 3.0
    TURN_SPEED = 2.0
    STOP_SPEED = 0.0
    
    key = keyboard.getKey()
    print(key)
    
    
    motor1.setVelocity(0.0)
    motor2.setVelocity(0.0)
    # motor3.setVelocity(0.0)
    motor4.setVelocity(0.0)
    motor3.setVelocity(0.0)
    
    if key == 315:
       FORWARD(FORWARD_SPEED)
    elif key == 317:
        REVERSE(FORWARD_SPEED)
    elif key == 316:
        TURN_LEFT(TURN_SPEED)
    elif key == 314:
        TURN_RIGHT(TURN_SPEED)

        