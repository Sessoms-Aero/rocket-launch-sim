# Level 3: motor

# --- Rules of the world ---
GRAVITY = 9.81      # gravity (m/s^2)
TIME_STEP = 0.01    # time step (s)
MAX_SIM_TIME = 600  # max sim time (s), the safety cap

# --- Rocket's specs ---
MASS = .072     # mass of rocket (kg)
THRUST = 6      # amount of rocket's force (N)
BURN_TIME = 1.6 # how long the fuel will burn (s)

# --- Page 0 ---
time = 0        # time starts at 0 s
altitude = 0    # altitude starts at 0 m
velocity = 0    # velocity starts at 0 m/s

# --- Draw the next page, while the rocket can move up ---
while velocity >= 0 and time < MAX_SIM_TIME:
    if time < BURN_TIME:
        current_thrust = THRUST
    else:
        current_thrust = 0
    weight = MASS * GRAVITY
    net_force = current_thrust - weight
    acceleration = net_force / MASS
    velocity = velocity + acceleration * TIME_STEP  # 2. new velocity = old velocity + acceleration x time step
    altitude = altitude + velocity * TIME_STEP      # 3. new altitude = old altitude + new velocity x time step
    time = time + TIME_STEP

# --- Last page ---
print(f"Max height is {altitude:.2f} m")
print(f"Time is {time:.2f} s")