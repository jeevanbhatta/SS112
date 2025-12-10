import matplotlib.pyplot as plt
import numpy as np

# Data: CPI Scores for Nepal (2012-2024)
# Source: Transparency International (https://www.transparency.org/en/countries/nepal)
years = np.arange(2012, 2025)
scores = [27, 31, 29, 27, 29, 31, 31, 34, 33, 33, 34, 35, 34]

# Events for Overlapping Graph
events = [
    {"year": 2013, "title": "2nd CA Election", "type": "Regime"},
    {"year": 2015, "title": "New Constitution", "type": "Regime"},
    {"year": 2015.8, "title": "Madhes Blockade", "type": "Protest"},
    {"year": 2017, "title": "1st Federal Elections", "type": "Regime"},
    {"year": 2020.9, "title": "Parliament Dissolution", "type": "Instability"},
    {"year": 2022.9, "title": "Rise of RSP / Elections", "type": "Regime"},
    {"year": 2023.4, "title": "Refugee Scandal", "type": "Protest"},
    {"year": 2024.2, "title": "Coop Fraud Protests", "type": "Protest"}
]

# --- Plot 1: Standalone CPI Graph ---
plt.figure(figsize=(12, 6))
plt.plot(years, scores, marker='o', linestyle='-', color='#006699', linewidth=2, markersize=8)

# Annotate scores
for x, y in zip(years, scores):
    plt.annotate(str(y), xy=(x, y), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=10, fontweight='bold')

plt.title("Nepal: Corruption Perceptions Index (CPI) Score (2012-2024)", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("CPI Score (0=Highly Corrupt, 100=Very Clean)", fontsize=12)
plt.ylim(20, 45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(years)
plt.tight_layout()
plt.savefig("nepal_cpi_standalone.png")
print("Saved nepal_cpi_standalone.png")

# --- Plot 2: Overlapping with Regime/Protests ---
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot CPI on primary axis
ax1.plot(years, scores, marker='o', linestyle='-', color='#006699', linewidth=2, markersize=8, label='CPI Score')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("CPI Score", fontsize=12, color='#006699')
ax1.tick_params(axis='y', labelcolor='#006699')
ax1.set_ylim(20, 45)
ax1.grid(axis='y', linestyle='--', alpha=0.3)
ax1.set_xticks(years)

# Add vertical lines for events
for event in events:
    color = 'red' if event['type'] == 'Protest' else ('green' if event['type'] == 'Regime' else 'orange')
    linestyle = '--' if event['type'] == 'Protest' else '-'
    
    plt.axvline(x=event['year'], color=color, linestyle=linestyle, alpha=0.6)
    
    # Add label
    y_pos = 42 if event['type'] == 'Regime' else (40 if event['type'] == 'Instability' else 38)
    # Stagger labels slightly to avoid overlap
    if event['year'] == 2015: y_pos = 43
    if event['year'] == 2015.8: y_pos = 37
    
    plt.text(event['year'], y_pos, event['title'], rotation=90, verticalalignment='center', 
             horizontalalignment='right', fontsize=9, color=color, fontweight='bold',
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

plt.title("Nepal: CPI Scores vs. Political Events (2012-2024)", fontsize=16, pad=20)

# Custom Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='#006699', lw=2, label='CPI Score'),
    Line2D([0], [0], color='green', lw=1, label='Regime Change/Election'),
    Line2D([0], [0], color='red', lw=1, linestyle='--', label='Protest/Scandal'),
    Line2D([0], [0], color='orange', lw=1, label='Political Instability')
]
plt.legend(handles=legend_elements, loc='upper left')

plt.figtext(0.5, 0.01, "Source: Transparency International (CPI Data) & ACLED/News Reports (Events)", ha="center", fontsize=9, style='italic')

plt.tight_layout()
plt.savefig("nepal_cpi_regime_overlap.png")
print("Saved nepal_cpi_regime_overlap.png")
