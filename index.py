import Jetson.GPIO as GPIO
import Pins as pins
import time

def main(): 
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pins.PIN_MOTOR_A_BACKWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_A_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_B_BACKWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(pins.PIN_MOTOR_B_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  pwmA = GPIO.PWM(pins.PIN_MOTOR_A_PWM, 500)
  pwmA.start(100)
  pwmB = GPIO.PWM(pins.PIN_MOTOR_B_PWM, 500)
  pwmB.start(100)
  GPIO.output(pins.PIN_MOTOR_A_FORWARD, GPIO.HIGH)
  GPIO.output(pins.PIN_MOTOR_B_FORWARD, GPIO.HIGH)

  ctr = 0
  try:
    while True:
      print("speed 1")
      pwmA.ChangeDutyCycle(1)
      pwmB.ChangeDutyCycle(100)
      time.sleep(2)
      print("speed 100")
      pwmA.ChangeDutyCycle(100)
      pwmB.ChangeDutyCycle(1)
      time.sleep(2)
      ctr += 1
      print("beep ", ctr)
  finally:
    GPIO.output(pins.PIN_MOTOR_A_FORWARD, GPIO.LOW)
    GPIO.output(pins.PIN_MOTOR_B_FORWARD, GPIO.LOW)
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()


if __name__ == "__main__":
  main()

