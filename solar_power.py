class SolarPanel:
    def __init__(self, region, panel_size_m2):
        self.region = region
        self.panel_size_m2 = panel_size_m2

    def calculate_output(self, irradiance, cloud_cover):
        """
        Calculate solar output using:
        Solar Output = Irradiance * (1 - Cloud Cover) * Panel Size * Efficiency (assumed 20%)
        """
        efficiency = 0.20
        return irradiance * (1 - cloud_cover) * self.panel_size_m2 * efficiency


def get_panel_size(size_input):
    size_specifications = {
        "small": 1.5,
        "medium": 2.0,
        "large": 3.0
    }
    
    if size_input.lower() in size_specifications:
        return size_specifications[size_input.lower()]
    
    try:
        size = float(size_input)
        if size < 0.1:
            print(" Panel size must be at least 0.1 m².")
            return None
        return size
    except ValueError:
        print(" Invalid input. Enter a valid number or choose from small, medium, large.")
        return None


def calculate_power_demand():
    appliances = {
        "television": 0.25,
        "sound system": 0.30,
        "iron box": 1.50,
        "lighting": 0.50  # Default lighting
    }
    
    print("\nAvailable appliances:")
    for appliance, power in appliances.items():
        print(f" - {appliance.title()} ({power} kWh/day)")
    
    selected_appliances = input("Enter the appliances you use (comma-separated): ").strip().lower().split(",")
    total_power_demand = appliances["lighting"]  # Default lighting
    
    for appliance in selected_appliances:
        appliance = appliance.strip()
        if appliance in appliances:
            total_power_demand += appliances[appliance]
        else:
            print(f" Warning: {appliance.title()} is not in the standard list and was ignored.")
    
    print(f"\nYour total daily power requirement: {total_power_demand:.2f} kWh\n")
    return total_power_demand


def main():
    region_data = {
        "kisumu": {"irradiance": 6.06, "cloud_cover": 0.6146},
        "bomet": {"irradiance": 5.85, "cloud_cover": 0.6731},
        "mandera": {"irradiance": 5.98, "cloud_cover": 0.5024},
        "mombasa": {"irradiance": 5.63, "cloud_cover": 0.508},
        "nyandarua": {"irradiance": 5.72, "cloud_cover": 0.6395}
    }

    try:
        region = input("Enter your region (Kisumu, Bomet, Mandera, Mombasa, Nyandarua): ").strip().lower()
        if region not in region_data:
            print(f" No data for the region: {region.title()}")
            return

        size_input = input("Enter your solar panel size in m² or type small, medium, large: ").strip()
        panel_size = get_panel_size(size_input)
        if panel_size is None:
            return

        desired_output = calculate_power_demand()
        panel = SolarPanel(region, panel_size)
        data = region_data[region]
        output = panel.calculate_output(data["irradiance"], data["cloud_cover"])

        print(f"\nProjected daily solar output for {region.title()}: {output:.2f} kWh")
        
        if output < desired_output:
            print(f" Recommendation: Consider using a larger panel. Your current output is {output:.2f} kWh, which is less than your desired {desired_output:.2f} kWh.")
        else:
            print(" Your solar output meets your desired output.")
    
    except Exception as e:
        print(f" An error occurred: {e}")


if __name__ == "__main__":
    main()

