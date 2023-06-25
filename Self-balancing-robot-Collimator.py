import matplotlib.pyplot as plt
import pycollimator as collimator
import math

# Load token for Collimator from file
token_file = open("token.txt", 'r')
token = token_file.read()

# Load model from Collimator
project_uuid = "221181d1-4494-4cf8-a58a-61345a7aa14c"
collimator.set_auth_token(token, project_uuid)
model = collimator.load_model("Self-Balancing Robot - PD")

# Simulate model
sim = collimator.run_simulation(model)
res = sim.results.to_pandas()

# Create figure
plt.figure()
plt.title("Self-Balancing Robot Control")

# Plot tilt angle response
plt.subplot(3, 1, 1)

plt.plot(res.index, res["Self_Balancing_Robot.theta"]*180/math.pi, label=f"Response")

plt.plot(res.index, res["Step.out_0"]*180/math.pi, "--", label="Setpoint")
plt.xlabel("Time [s]")
plt.ylabel("Theta - Tilt Angle [deg]")
plt.legend()
plt.grid()

# Plot controller output
plt.subplot(3, 1, 2)

plt.plot(res.index, res["Adder_1.out_0"])
plt.xlabel("Time [s]")
plt.ylabel("Wheel Torque [Nm]")
plt.grid()

# Plot robot position
plt.subplot(3, 1, 3)

plt.plot(res.index, res["Self_Balancing_Robot.x"])
plt.xlabel("Time [s]")
plt.ylabel("Robot Position [m]")
plt.grid()

# Show plots
plt.show()