# Rocket launch simulation for you to input values to create a calculated apogee.
# Ethan Sessoms
# v1.0

import math
import sys

GRAVITY = 9.81      # Gravity (m/s^2)
AIR_DENSITY = 1.225 # Air Density at Sea Level (kg/m^3)
TIME_STEP = 0.01    # Time Step (s)
MAX_SIM_TIME = 600  # Maximum Simulation Time (s)

dry_mass = float(input("Dry mass (g): "))
fuel_mass = float(input("Fuel mass (g): "))
thrust = float(input("Thrust (N): "))
burn_time = float(input("Burn Time (s): "))
diameter = float(input("Diameter (cm): "))
drag_coefficient = float(input("Drag coefficient: "))

dry_mass = dry_mass / 1000
fuel_mass = fuel_mass / 1000
diameter = diameter / 100