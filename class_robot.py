__author__ = "Chloé Bernardet"
__filename__ = "class_robot"

import RPi.GPIO as GPIO
import time


class Robot:
    """ classe permettant de controler le robot """

    def __init__(self, gpio1_roue_droite, gpio2_roue_droite, gpio_pwm_roue_droite, gpio1_roue_gauche, gpio2_roue_gauche,
                 gpio_pwm_roue_gauche):
        # Broches roue droite du robot
        self.gpio1_roue_droite = gpio1_roue_droite  # IN
        self.gpio2_roue_droite = gpio2_roue_droite  # IN
        self.gpio_pwm_roue_droite = gpio_pwm_roue_droite

        # Broches roue gauche du robot
        self.gpio1_roue_gauche = gpio1_roue_gauche  # IN
        self.gpio2_roue_gauche = gpio2_roue_gauche  # IN
        self.gpio_pwm_roue_gauche = gpio_pwm_roue_gauche

        # Initialisation
        GPIO.setup(self.gpio1_roue_gauche, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.gpio2_roue_gauche, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.gpio1_roue_droite, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.gpio2_roue_droite, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(gpio_pwm_roue_droite, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(gpio_pwm_roue_gauche, GPIO.OUT, initial=GPIO.LOW)
        self.pwm_roue_droite = GPIO.PWM(gpio_pwm_roue_droite, 0)  # 0 = frequence
        self.pwm_roue_gauche = GPIO.PWM(gpio_pwm_roue_gauche, 0)
        self.pwm_roue_droite.start(0)  # 0 = rapport cyclique
        self.pwm_roue_gauche.start(0)

    def changement_frequence_pwn_roue_gauche(self, nouv_frequence_pwm_roue_gauche):
        if not 0 <= nouv_frequence_pwm_roue_gauche <= 100:
            raise ValueError("La fréquence doit être comprise entre 0 et 100")
        self.pwm_roue_gauche.ChangeDutyCycle(nouv_frequence_pwm_roue_gauche)

    def changement_frequence_pwm_roue_droite(self, nouv_frequence_pwm_roue_droite):
        if not 0 <= nouv_frequence_pwm_roue_droite <= 100:
            raise ValueError("La fréquence doit être comprise entre 0 et 100")
        self.pwm_roue_droite.ChangeDutyCycle(nouv_frequence_pwm_roue_droite)

    def avancer(self, temps):
        """ le robot avance tout droit pendant temps secondes
        temps = entier = temps en secondes """
        GPIO.output(self.gpio1_roue_droite, GPIO.HIGH)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.HIGH)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)

        time.sleep(temps)

        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)

    def reculer(self, temps):
        """ le robot recule tout droit pendant temps secondes
        temps = entier = temps en secondes """
        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.HIGH)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.HIGH)

        time.sleep(temps)

        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)

    def droite(self, temps):
        """le robot tourne à droite pendant temps secondes"""

        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.HIGH)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)

        time.sleep(temps)

        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)

    def gauche(self, temps):
        """le robot tourne à gauche pendant temps secondes"""

        GPIO.output(self.gpio1_roue_droite, GPIO.HIGH)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)

        time.sleep(temps)

        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)
