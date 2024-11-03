import numpy as np
import pandas as pd

# Define the number of samples
num_samples = 3000

# Define realistic ranges for each feature based on 22nm CMOS technology
voltage_range = (0.8, 1.2)           # Operating voltage range in volts
frequency_range = (100, 1000)        # Frequency range in MHz
temperature_range = (20, 100)        # Temperature range in °C
capacitance_range = (0.5e-12, 1.5e-12) # Load capacitance range in Farads
leakage_current_range = (0.1e-6, 5e-6) # Leakage current range in Amperes
switching_activity_range = (0.1, 0.9)  # Switching activity factor (0-1)
circuit_area_range = (0.5, 15)         # Circuit area range in mm²

# Generate random data within the specified ranges
voltages = np.random.uniform(*voltage_range, num_samples)
frequencies = np.random.uniform(*frequency_range, num_samples)
temperatures = np.random.uniform(*temperature_range, num_samples)
capacitances = np.random.uniform(*capacitance_range, num_samples)
leakage_currents = np.random.uniform(*leakage_current_range, num_samples)
switching_activities = np.random.uniform(*switching_activity_range, num_samples)
circuit_areas = np.random.uniform(*circuit_area_range, num_samples)

# Calculate power consumption using a simple approximate formula
# For dynamic power: Power_dynamic = capacitance * voltage^2 * frequency * switching_activity
# For leakage power: Power_leakage = leakage_current * voltage
# Total power is the sum of dynamic and leakage power

dynamic_power = capacitances * (voltages**2) * frequencies * switching_activities
leakage_power = leakage_currents * voltages
total_power = dynamic_power + leakage_power

# Combine all features and power consumption into a DataFrame
data = pd.DataFrame({
    'Voltage (V)': voltages,
    'Frequency (MHz)': frequencies,
    'Temperature (°C)': temperatures,
    'Capacitance (F)': capacitances,
    'Leakage Current (A)': leakage_currents,
    'Switching Activity': switching_activities,
    'Circuit Area (mm²)': circuit_areas,
    'Power Consumption (mW)': total_power * 1000  # Convert to mW
})

# Save the dataset to a CSV file
data.to_csv('vlsi_power_dataset_22nm.csv', index=False)

print("Dataset generated and saved as 'vlsi_power_dataset_22nm.csv'")
