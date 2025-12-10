import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'ACLED Data_2025-12-09.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File {file_path} not found.")
    exit(1)

# Convert event_date to datetime
df['event_date'] = pd.to_datetime(df['event_date'])

# Filter for relevant years (2019-2025 based on file name and request)
df = df[(df['year'] >= 2019)]

# Filter for relevant event types mentioned in the text
# "Protests", "Riots", "Strategic developments"
relevant_types = ['Protests', 'Riots', 'Strategic developments']
df_filtered = df[df['event_type'].isin(relevant_types)]

# Aggregate data by month and event type
df_filtered['month_year'] = df_filtered['event_date'].dt.to_period('M')
monthly_counts = df_filtered.groupby(['month_year', 'event_type']).size().reset_index(name='count')
monthly_counts['month_year'] = monthly_counts['month_year'].dt.to_timestamp()

# Set the style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# Create the plot
sns.lineplot(data=monthly_counts, x='month_year', y='count', hue='event_type', marker='o')

# Customize the plot
plt.title('ACLED Event Count in Nepal (2019–2025)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Events', fontsize=12)
plt.legend(title='Event Type')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
output_path = 'visualizations/acled_event_count.png'
plt.savefig(output_path)
print(f"Graph saved to {output_path}")
