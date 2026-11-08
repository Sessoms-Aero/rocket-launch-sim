# Rocket launch simulation for you to input values to create a calculated apogee.
# Ethan Sessoms
# v1.0

import math
import sys

# --- Constants ---

GRAVITY = 9.81      # Gravity (m/s^2)
AIR_DENSITY = 1.225 # Air Density at Sea Level (kg/m^3)
TIME_STEP = 0.01    # Time Step (s)
MAX_SIM_TIME = 600  # Maximum Simulation Time (s)

# --- User inputs ---

dry_mass = float(input("Dry mass (g): "))               # Mass of rocket's structure
fuel_mass = float(input("Fuel mass (g): "))             # Mass of the propellant
thrust = float(input("Thrust (N): "))                   # Amount of rocket's force
burn_time = float(input("Burn Time (s): "))             # How long the fuel will burn
diameter = float(input("Diameter (cm): "))              # Width of the rocket
drag_coefficient = float(input("Drag coefficient: "))   # Air pressure opposing thrust

# --- Unit conversions (SI) ---

dry_mass = dry_mass / 1000      # Grams to kilograms
fuel_mass = fuel_mass / 1000    # Grams to kilograms
diameter = diameter / 100       # Centimeter to meters

# --- Derived values ---

total_mass = dry_mass + fuel_mass                   # Mass of rocket in its entirety
burn_rate = fuel_mass / burn_time                   # How much fuel is being used per second
cross_section_area = math.pi * ((diameter / 2)**2)  # Calculating the area of the rocket's nose for drag
liftoff_weight = total_mass * GRAVITY               # Weight of the rocket

# --- Liftoff check ---

if thrust <= liftoff_weight:    # Checks if there is enough thrust for liftoff
    print("Your thrust is not big enough to lift the rocket up.")
    sys.exit()
else:
    ratio = thrust / liftoff_weight
    print(f"Thrust-to-weight ratio: {ratio:.1f}")