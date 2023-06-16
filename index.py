import Jetson.GPIO as GPIO
import Pins as pins
import time

def main(): 
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pins.PIN_MOTOR_A_BACKWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_A_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_A_PWM, GPIO.OUT, initial=GPIO.HIGH)
  GPIO.setup(pins.PIN_MOTOR_B_BACKWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_B_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_B_PWM, GPIO.OUT, initial=GPIO.HIGH)
  pwmA = GPIO.PWM(pins.PIN_MOTOR_A_PWM, 100)
  pwmA.start(0)
  pwmB = GPIO.PWM(pins.PIN_MOTOR_B_PWM, 100)
  pwmB.start(0)
  GPIO.output(pins.PIN_MOTOR_A_FORWARD, GPIO.HIGH)

  ctr = 0
  try:
    while True:
      print("speed 1")
      pwmA.ChangeDutyCycle(1)
      time.sleep(2)
      print("speed 100")
      pwmA.ChangeDutyCycle(100)
      time.sleep(2)
      ctr += 1
      print("beep ", ctr)
  finally:
    GPIO.output(pins.PIN_MOTOR_A_FORWARD, GPIO.LOW)
    GPIO.cleanup()
    pwmA.stop()
    pwmB.stop()


if __name__ == "__main__":
  main()

