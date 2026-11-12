# Level 2: thrown ball (gravity only)

# --- Rules of the world ---
GRAVITY = 9.81      # gravity (m/s^2)
TIME_STEP = 0.01    # time step (s)
MAX_SIM_TIME = 600  # max sim time (s), the safety cap

# --- Page 0 ---
time = 0        # time starts at 0 s
altitude = 0    # altitude starts at 0 m
velocity = 30   # velocity starts at 30 m/s

# --- Draw the next page, while the ball is moving up ---
while velocity >= 0 and time < MAX_SIM_TIME:
    acceleration = -1 * GRAVITY                     # 1. acceleration
    velocity = velocity + acceleration * TIME_STEP  # 2. new velocity = old velocity + acceleration x time step
    altitude = altitude + velocity * TIME_STEP      # 3. new altitude = old altitude + new velocity x time step
    time = time + TIME_STEP                         # 4. new time = old time + time step

# --- Last page ---
print(f"Time is {time:.2f} s")
print(f"Height is {altitude:.2f} m")