# Rocket launch simulation for you to input values to create a calculated apogee.
# Ethan Sessoms
# v1.0

import math
import sys

# --- Rules of the world ---

GRAVITY = 9.81      # Gravity (m/s^2)
AIR_DENSITY = 1.225 # Air Density at Sea Level (kg/m^3)
TIME_STEP = 0.01    # Time Step (s)
MAX_SIM_TIME = 600  # Maximum Simulation Time (s)

# --- Rocket's specs ---

dry_mass = float(input("Dry mass (g): "))               # Mass of rocket's structure
fuel_mass = float(input("Fuel mass (g): "))             # Mass of the propellant
thrust = float(input("Thrust (N): "))                   # Amount of rocket's force
burn_time = float(input("Burn Time (s): "))             # How long the fuel will burn
diameter = float(input("Diameter (cm): "))              # Width of the rocket
drag_coefficient = float(input("Drag coefficient: "))   # How streamlined the shape is

dry_mass = dry_mass / 1000                              # Grams to kilograms
fuel_mass = fuel_mass / 1000                            # Grams to kilograms
diameter = diameter / 100                               # Centimeters to meters

total_mass = dry_mass + fuel_mass                       # Mass of rocket in its entirety
burn_rate = fuel_mass / burn_time                       # How much fuel is being used per second
cross_section_area = math.pi * ((diameter / 2)**2)      # Calculating the area of the rocket's nose for drag
liftoff_weight = total_mass * GRAVITY                   # Weight of the rocket

# --- Go or no go check ---

if thrust <= liftoff_weight:    # Checks if there is enough thrust for liftoff
    print("Your thrust is not big enough to lift the rocket up!")
    sys.exit()
else:
    ratio = thrust / liftoff_weight
    print(f"Thrust-to-weight ratio: {ratio:.1f}")

# --- Page 0 of flipbook ---

time = 0 
altitude = 0
velocity = 0
current_mass = total_mass

# --- Noteworhty reports ---

peak_velocity = 0
burnout_alt = 0
burnout_vel = 0
burnout = False

# --- "Draw the next page" ---

while velocity >= 0 and time >= 0 and MAX_SIM_TIME >= 0:
    if time < burn_time:
        current_thrust = thrust
    weight = current_mass
    # drag
    # net force
    # update the motion
    # burn fuel
    # record burnout
    # track top speed