import Jetson.GPIO as GPIO
import Pins as pins

def main(): 
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pins.PIN_MOTOR_A_BACKWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_A_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_A_PWM, GPIO.OUT, initial=GPIO.HIGH)
  GPIO.setup(pins.PIN_MOTOR_B_BACKWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_B_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_B_PWM, GPIO.OUT, initial=GPIO.HIGH)
  pwmA = GPIO.PWM(pins.PIN_MOTOR_A_PWM, 50)

if __name__ == "__main__":
  main()