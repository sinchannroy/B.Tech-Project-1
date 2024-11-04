import numpy as np
import pandas as pd

# Number of entries to generate
num_samples = 3000

# Define feature ranges based on 22nm CMOS technology parameters
voltage_range = (0.8, 1.2)  # V (Operating voltage range)
frequency_range = (100, 1000)  # MHz (Frequency range)
temperature_range = (20, 100)  # °C (Temperature range)
capacitance_range = (0.5e-12, 1.5e-12)  # F (Capacitance)
leakage_current_range = (0.1e-6, 5e-6)  # A (Leakage current)
switching_activity_range = (0.1, 0.9)  # Switching activity factor (0-1)
circuit_area_range = (0.5, 15)  # mm² (Circuit area)

# Initialize arrays for feature generation
voltages = np.random.uniform(*voltage_range, num_samples)
frequencies = np.random.uniform(*frequency_range, num_samples)
temperatures = np.random.uniform(*temperature_range, num_samples)
capacitances = np.random.uniform(*capacitance_range, num_samples)
leakage_currents = np.random.uniform(*leakage_current_range, num_samples)
switching_activities = np.random.uniform(*switching_activity_range, num_samples)
circuit_areas = np.random.uniform(*circuit_area_range, num_samples)

# Set parameters for iterative noise refinement (diffusion-like process)
num_iterations = 100  # Number of diffusion steps
noise_level = 0.01  # Initial noise level (can be decreased over iterations)

for i in range(num_iterations):
    # Refine each feature with Gaussian noise, simulating process variations
    voltages += np.random.normal(0, noise_level * (voltage_range[1] - voltage_range[0]), num_samples)
    frequencies += np.random.normal(0, noise_level * (frequency_range[1] - frequency_range[0]), num_samples)
    temperatures += np.random.normal(0, noise_level * (temperature_range[1] - temperature_range[0]), num_samples)
    capacitances += np.random.normal(0, noise_level * (capacitance_range[1] - capacitance_range[0]), num_samples)
    leakage_currents += np.random.normal(0, noise_level * (leakage_current_range[1] - leakage_current_range[0]), num_samples)
    switching_activities += np.random.normal(0, noise_level * (switching_activity_range[1] - switching_activity_range[0]), num_samples)
    circuit_areas += np.random.normal(0, noise_level * (circuit_area_range[1] - circuit_area_range[0]), num_samples)

    # Ensure values remain within bounds
    voltages = np.clip(voltages, *voltage_range)
    frequencies = np.clip(frequencies, *frequency_range)
    temperatures = np.clip(temperatures, *temperature_range)
    capacitances = np.clip(capacitances, *capacitance_range)
    leakage_currents = np.clip(leakage_currents, *leakage_current_range)
    switching_activities = np.clip(switching_activities, *switching_activity_range)
    circuit_areas = np.clip(circuit_areas, *circuit_area_range)

    # Decrease noise level over iterations to refine data (diffusion-like)
    noise_level *= 0.98

# Calculate power consumption using a simplified model
# Dynamic Power: P_dynamic = C * V^2 * f * alpha
# Leakage Power: P_leakage = I_leakage * V
# Total Power: Sum of dynamic and leakage power
dynamic_power = capacitances * (voltages**2) * frequencies * switching_activities
leakage_power = leakage_currents * voltages
total_power = dynamic_power + leakage_power

# Convert power to milliwatts
total_power_mw = total_power * 1000

# Create DataFrame with generated features and target power
data = pd.DataFrame({
    'Voltage (V)': voltages,
    'Frequency (MHz)': frequencies,
    'Temperature (°C)': temperatures,
    'Capacitance (F)': capacitances,
    'Leakage Current (A)': leakage_currents,
    'Switching Activity': switching_activities,
    'Circuit Area (mm²)': circuit_areas,
    'Power Consumption (mW)': total_power_mw
})

# Save to CSV file
output_file = 'synthetic_dataset.csv'
data.to_csv(output_file, index=False)

print(f"Dataset generated and saved as '{output_file}'")
