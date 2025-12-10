import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data: Events with dates, types, and descriptions
# Source: PolSci Institute (https://polsci.institute/south-asia/nepal-history-monarchy-to-democratic-republic/)
events = [
    {"year": 1769, "type": "Regime Change", "title": "Unification of Nepal", "desc": "Shah Dynasty Established"},
    {"year": 1846, "type": "Regime Change", "title": "Rise of Rana Dynasty", "desc": "Autocratic Rule Begins"},
    {"year": 1951, "type": "Protest/Movement", "title": "1951 Revolution", "desc": "Anti-Rana Movement"},
    {"year": 1951.5, "type": "Regime Change", "title": "End of Rana Rule", "desc": "Monarchy Restored"},
    {"year": 1996, "type": "Protest/Movement", "title": "Maoist Insurgency", "desc": "People's War Begins"},
    {"year": 2006, "type": "Protest/Movement", "title": "People's Movement II", "desc": "Jana Andolan / Peace Deal"},
    {"year": 2008, "type": "Regime Change", "title": "Republic Declared", "desc": "Monarchy Abolished"},
    {"year": 2015, "type": "Regime Change", "title": "New Constitution", "desc": "Federal Republic Solidified"},
    {"year": 2023, "type": "Protest/Movement", "title": "Gen Z Protests", "desc": "Anti-Corruption / 'No Not Again'"}
]

# Separate data for plotting
years = [e["year"] for e in events]
titles = [e["title"] for e in events]
types = [e["type"] for e in events]

# Create figure and plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define levels to avoid text overlap
levels = [1, -1, 2, -2, 3, -3, 1, -1, 2] 

# Create the baseline
ax.plot(years, [0] * len(years), "-.", color="black", marker="o")

# Plot each event
for i, (year, title, event_type, level) in enumerate(zip(years, titles, types, levels)):
    color = "red" if event_type == "Protest/Movement" else "blue"
    
    # Vertical line to the event
    ax.vlines(year, 0, level, color=color, linestyle="--", alpha=0.7)
    
    # Event Point
    ax.plot(year, level, "o", color=color, markersize=10)
    
    # Text Label
    ax.annotate(f"{year}: {title}\n({events[i]['desc']})", 
                xy=(year, level), 
                xytext=(0, 5 if level > 0 else -25), 
                textcoords="offset points", 
                ha="center", va="bottom" if level > 0 else "top",
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, alpha=0.9))

# Customizing the plot
ax.set_title("Timeline of Political Change in Nepal: Protests vs. Regime Shifts", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.get_yaxis().set_visible(False) # Hide Y axis
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xlim(1750, 2030)

# Add a legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Regime Change', markerfacecolor='blue', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Protest/Movement', markerfacecolor='red', markersize=10)
]
ax.legend(handles=legend_elements, loc='upper left')

# Add Source Citation
plt.figtext(0.5, 0.02, "Source: PolSci Institute (nepal-history-monarchy-to-democratic-republic) & ACLED", ha="center", fontsize=8, style='italic')

# Save the plot
plt.tight_layout()
plt.savefig("nepal_political_timeline.png")
print("Timeline saved as nepal_political_timeline.png")
