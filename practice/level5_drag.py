# Level 5: drag

import math

# --- Rules of the world ---
GRAVITY = 9.81      # gravity (m/s^2)
TIME_STEP = 0.01    # time step (s)
MAX_SIM_TIME = 600  # max sim time (s), the safety cap
AIR_DENSITY = 1.225 # air density at sea level (kg/m^3)

# --- Rocket's specs ---
DRY_MASS = 60 / 1000                                # mass of the rocket itself (kg)
FUEL_MASS = 12 / 1000                               # mass of the fuel (kg)
THRUST = 6                                          # motor thrust (N)
BURN_TIME = 1.6                                     # how long the fuel will burn (s)
BURN_RATE = FUEL_MASS / BURN_TIME                   # the rate at which the fuel is being used (kg/s)
DIAMETER = 2.5 / 100                                # width of the rocket (m)
DRAG_COEFFICIENT = 0.75                             # how streamlined the shape is
CROSS_SECTION_AREA = math.pi * ((DIAMETER/2)**2)    # calculating the area of the rocket's nose for drag

# --- Page 0 ---
time = 0                            # time starts at 0 s
altitude = 0                        # altitude starts at 0 m
velocity = 0                        # velocity starts at 0 m/s
current_mass = DRY_MASS + FUEL_MASS # the combined mass of the rocket itself and the fuel it is carrying

# --- Draw the next page, while the rocket can move up ---
while velocity >= 0 and time < MAX_SIM_TIME:                                            # keep drawing while the rocket is still climbing (and under the time cap)
    if time < BURN_TIME:                                                                # 1. motor on while time is under burn time, off after
        current_thrust = THRUST
        current_mass = max(DRY_MASS, current_mass - BURN_RATE * TIME_STEP)              # 2. burn this page's fuel (never below dry mass)
    else:
        current_thrust = 0
    weight = current_mass * GRAVITY                                                     # 3. weight = gravity's pull on the rocket (N)
    drag = 1/2 * AIR_DENSITY * (velocity ** 2) * DRAG_COEFFICIENT * CROSS_SECTION_AREA  # 4. drag = air resistance, pushes down while climbing (N)
    net_force = current_thrust - weight - drag                                          # 5. net force = thrust up minus weight down (goes negative once the motor is off)
    acceleration = net_force / current_mass                                             # 6. Newton's 2nd law: a = F / m
    velocity = velocity + acceleration * TIME_STEP                                      # 7. new velocity = old velocity + acceleration x time step
    altitude = altitude + velocity * TIME_STEP                                          # 8. new altitude = old altitude + new velocity x time step
    time = time + TIME_STEP                                                             # 9. turns to the next page

# --- Last page ---
print(f"Max height is {altitude:.2f} m")
print(f"Time is {time:.2f} s")
print(f"The final mass is {current_mass:.3f} kg")