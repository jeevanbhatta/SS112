import matplotlib.pyplot as plt
import numpy as np

# Define the grid
x = np.linspace(0, 10, 100) # State Repression
y = np.linspace(0, 10, 100) # Public Mobilization
X, Y = np.meshgrid(x, y)

# Define a potential function with two wells (basins of attraction)
# Basin 1: Status Quo (Moderate Repression, Low Mobilization) -> (3, 2)
# Basin 2: Regime Change (Low Repression, High Mobilization/Reform) -> (7, 8) - conceptually, high mobilization forces change
# Saddle point (Critical Point) roughly between them
Z = 0.5 * ((X - 3)**2 + (Y - 2)**2) - 0.3 * np.exp(-((X - 5)**2 + (Y - 5)**2)) 
# Let's make a simpler synthetic potential for visual clarity
# Two attractors
Z = -1 * (np.exp(-0.2*((X-2)**2 + (Y-2)**2)) + np.exp(-0.2*((X-8)**2 + (Y-8)**2)))
# Add a barrier (saddle)
Z += 0.5 * np.exp(-0.1*((X-5)**2 + (Y-5)**2))

fig, ax = plt.subplots(figsize=(12, 9))

# Plot the basins (contour)
# cmap='coolwarm_r': Red = Low Z (Stable), Blue = High Z (Unstable)
cp = ax.contourf(X, Y, Z, levels=20, cmap='coolwarm_r', alpha=0.6)

# Add Colorbar Legend
cbar = fig.colorbar(cp, ax=ax, shrink=0.8)
cbar.set_label('System Potential (Stability)', fontsize=12)
cbar.set_ticks([Z.min(), Z.max()])
cbar.set_ticklabels(['Stable (Attractor)', 'Unstable (Barrier)'])

# Define the trajectory
# 1. Start at Status Quo (2, 2)
# 2. Social Media Ban (Increase Repression) -> (4.5, 2.2)
# 3. Protests Erupt (Increase Mobilization) -> (4.8, 4.0) - Climbing the hill
# 4. Police Brutality (Critical Point/Tipping Point) -> (5.0, 5.0) - Exact peak of the barrier/saddle point
# 5. Regime Shift (Flow to new attractor) -> (8, 8)

path_x = [2, 4.5, 4.8, 5.0, 8]
path_y = [2, 2.2, 4.0, 5.0, 8]

# Plot trajectory
ax.plot(path_x, path_y, color='black', linewidth=2, linestyle='--', marker='o', label='System Trajectory')

# Annotate points
annotations = [
    (2, 2, "Status Quo\n(Attractor A)"),
    (4.5, 2.2, "Social Media Ban\n(Trigger)"),
    (4.8, 4.0, "Protests Erupt"),
    (5.0, 5.0, "Police Brutality\n(Critical Point)"),
    (8, 8, "Regime Change\n(Attractor B)")
]

for tx, ty, text in annotations:
    ax.annotate(text, (tx, ty), xytext=(tx+0.5, ty-0.5), 
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8))

# Add Separator Line (approximate)
x_sep = np.linspace(0, 10, 100)
y_sep = 10 - x_sep
ax.plot(x_sep, y_sep, 'k:', alpha=0.5, label='Basin Boundary')

# Labels and Title
ax.set_xlabel("State Repression (Inverse Civil Liberties)", fontsize=12)
ax.set_ylabel("Public Mobilization (Protest Intensity)", fontsize=12)
ax.set_title("Phase Space of Political Unrest: From Ban to Regime Change", fontsize=14)

# Custom Ticks for Axes to give meaning
ax.set_xticks([0, 2.5, 5, 7.5, 10])
ax.set_xticklabels(["Open Society", "Targeted\nRestrictions", "Censorship/\nBans", "Mass Arrests", "Authoritarian"])

ax.set_yticks([0, 2.5, 5, 7.5, 10])
ax.set_yticklabels(["Apathy", "Digital\nDissent", "Regional\nProtests", "Mass\nUprising", "Revolution"])

ax.legend(loc='upper left')
ax.grid(True, linestyle='--', alpha=0.3)

# Save
plt.tight_layout()
plt.savefig("nepal_phase_space.png")
print("Saved nepal_phase_space.png")
