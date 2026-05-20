python
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load data from the CSV file
    data = pd.read_csv(file_path)
    return data

def visualize_data(data, region):
    # Filter data for the selected region
    region_data = data[data['Region'] == region]

    # Group data by year and calculate total farm area
    yearly_data = region_data.groupby('Year')['Area (Donums)'].sum().reset_index()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_data['Year'], yearly_data['Area (Donums)'], marker='o', color='b', label='Total Farm Area')
    plt.title(f'Total Farm Area in {region} (2012-2019)')
    plt.xlabel('Year')
    plt.ylabel('Total Area (Donums)')
    plt.grid()
    plt.legend()
    plt.show()

# Example usage
file_path = 'common_open_datasets_2_10_3.csv'
data = load_data(file_path)
visualize_data(data, 'Abu Dhabi')
