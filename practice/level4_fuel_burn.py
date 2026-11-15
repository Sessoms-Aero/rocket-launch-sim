# Level 4: fuel burn

# --- Rules of the world ---
GRAVITY = 9.81      # gravity (m/s^2)
TIME_STEP = 0.01    # time step (s)
MAX_SIM_TIME = 600  # max sim time (s), the safety cap

# --- Rocket's specs ---
DRY_MASS = 60 / 1000                # mass of the rocket itself (kg)
FUEL_MASS = 12 / 1000               # mass of the fuel (kg)
THRUST = 6                          # motor thrust (N)
BURN_TIME = 1.6                     # how long the fuel will burn (s)
BURN_RATE = FUEL_MASS / BURN_TIME   # the rate at which the fuel is being used (kg/s)

# --- Page 0 ---
time = 0                            # time starts at 0 s
altitude = 0                        # altitude starts at 0 m
velocity = 0                        # velocity starts at 0 m/s
current_mass = DRY_MASS + FUEL_MASS # the combined mass of the rocket itself and the fuel it is carrying

# --- Draw the next page, while the rocket can move up ---
while velocity >= 0 and time < MAX_SIM_TIME:                                # keep drawing while the rocket is still climbing (and under the time cap)
    if time < BURN_TIME:                                                    # 1. motor on while time is under burn time, off after
        current_thrust = THRUST
        current_mass = max(DRY_MASS, current_mass - BURN_RATE * TIME_STEP)  # 2. making the fuel burn over time
    else:
        current_thrust = 0
    weight = current_mass * GRAVITY                                         # 3. weight = gravity's pull on the rocket (N)
    net_force = current_thrust - weight                                     # 4. net force = thrust up minus weight down (goes negative once the motor is off)
    acceleration = net_force / current_mass                                 # 5. Newton's 2nd law: a = F / m
    velocity = velocity + acceleration * TIME_STEP                          # 6. new velocity = old velocity + acceleration x time step
    altitude = altitude + velocity * TIME_STEP                              # 7. new altitude = old altitude + new velocity x time step
    time = time + TIME_STEP                                                 # 8. turns to the next page

# --- Last page ---
print(f"Max height is {altitude:.2f} m")
print(f"Time is {time:.2f} s")
print(f"The final mass is {current_mass:.2f} kg")