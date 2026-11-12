# Level 3: motor (constant mass, no drag)

# --- Rules of the world ---
GRAVITY = 9.81      # gravity (m/s^2)
TIME_STEP = 0.01    # time step (s)
MAX_SIM_TIME = 600  # max sim time (s), the safety cap

# --- Rocket's specs ---
MASS = 0.072     # mass of rocket (kg)
THRUST = 6      # motor thrust (N)
BURN_TIME = 1.6 # how long the fuel will burn (s)

# --- Page 0 ---
time = 0        # time starts at 0 s
altitude = 0    # altitude starts at 0 m
velocity = 0    # velocity starts at 0 m/s

# --- Draw the next page, while the rocket can move up ---
while velocity >= 0 and time < MAX_SIM_TIME:        # keep drawing while the rocket is still climbing (and under the time cap)
    if time < BURN_TIME:                            # 1. motor on while time is under burn time, off after
        current_thrust = THRUST
    else:
        current_thrust = 0
    weight = MASS * GRAVITY                         # 2. weight = gravity's pull on the rocket (N)
    net_force = current_thrust - weight             # 3. net force = thrust up minus weight down (goes negative once the motor is off)
    acceleration = net_force / MASS                 # 4. Newton's 2nd law: a = F / m
    velocity = velocity + acceleration * TIME_STEP  # 5. new velocity = old velocity + acceleration x time step
    altitude = altitude + velocity * TIME_STEP      # 6. new altitude = old altitude + new velocity x time step
    time = time + TIME_STEP                         # 7. turns to the next page

# --- Last page ---
print(f"Max height is {altitude:.2f} m")
print(f"Time is {time:.2f} s")