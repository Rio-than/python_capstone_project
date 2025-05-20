import tkinter as tk
from tkinter import messagebox, ttk

class SolarPanel:
    def __init__(self, region, panel_size_m2):
        self.region = region
        self.panel_size_m2 = panel_size_m2

    def calculate_output(self, irradiance, cloud_cover):
        efficiency = 0.20
        return irradiance * (1 - cloud_cover) * self.panel_size_m2 * efficiency


def get_panel_size(size_input):
    size_specifications = {
        "small": 0.3,   # Midpoint of 0.1 - 0.5
        "medium": 0.85, # Midpoint of 0.51 - 1.2
        "large": 1.5    # Any size > 1.2
    }

    size_input = size_input.lower().strip()

    if size_input in size_specifications:
        return size_specifications[size_input]

    try:
        size = float(size_input)
        if size < 0.1:
            messagebox.showerror("Error", "Panel size must be at least 0.1 m².")
            return None
        elif 0.1 <= size <= 0.5:
            category = "Small"
        elif 0.51 <= size <= 1.2:
            category = "Medium"
        else:
            category = "Large"

        messagebox.showinfo("Panel Size", f"Selected panel size: {size} m² ({category})")
        return size
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Enter a valid number or choose: small, medium, large.")
        return None


def calculate_power_demand(selected_appliances):
    appliances = {
        "television": 0.15,
        "sound system": 0.20,
        "iron box": 1.50,
        "lighting": 0.20  # Default lighting
    }
    
    total_power_demand = appliances["lighting"]  # Default lighting
    for appliance in selected_appliances:
        if appliance in appliances:
            total_power_demand += appliances[appliance]
    
    return total_power_demand


def calculate_solar_output():
    region = region_var.get().lower()
    size_input = panel_size_var.get().strip()
    
    if region not in region_data:
        messagebox.showerror("Error", "Invalid region selected.")
        return
    
    panel_size = get_panel_size(size_input)
    if panel_size is None:
        return
    
    selected_appliances = [appliance for appliance, var in appliance_vars.items() if var.get()]
    desired_output = calculate_power_demand(selected_appliances)
    panel = SolarPanel(region, panel_size)
    data = region_data[region]
    output = panel.calculate_output(data["irradiance"], data["cloud_cover"])
    
    result_text = f"Projected daily solar output for {region.title()}: {output:.2f} kWh\n"
    result_text += f"Your total daily power requirement: {desired_output:.2f} kWh\n\n"
    
    if output < desired_output:
        result_text += f"Recommendation: Consider using a larger panel or add more panels. Your current output is {output:.2f} kWh, which is less than your desired {desired_output:.2f} kWh.To purchase solar panels visit:{"https://solarstore.co.ke/pv-solar-panels/"}"
    else:
        result_text += "Your solar output meets your desired output."
    
    messagebox.showinfo("Solar Output Calculation", result_text)


# GUI Implementation
root = tk.Tk()
root.title("Solar Power Calculator")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

region_data = {
    "kisumu": {"irradiance": 6.06, "cloud_cover": 0.6146},
    "bomet": {"irradiance": 5.85, "cloud_cover": 0.6731},
    "mandera": {"irradiance": 5.98, "cloud_cover": 0.5024},
    "mombasa": {"irradiance": 5.63, "cloud_cover": 0.508},
    "nyandarua": {"irradiance": 5.72, "cloud_cover": 0.6395}
}

appliance_vars = {
    "television": tk.BooleanVar(),
    "sound system": tk.BooleanVar(),
    "iron box": tk.BooleanVar(),
}

# Centering the frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True)

# UI Elements (Centered)
tk.Label(frame, text="Select Region:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
region_var = tk.StringVar()
region_menu = ttk.Combobox(frame, textvariable=region_var, values=list(region_data.keys()), font=("Arial", 12))
region_menu.pack(pady=5)

# Panel Size Entry
tk.Label(frame, text="Enter Panel Size (m²) or choose small, medium, large:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
panel_size_var = tk.StringVar()
tk.Entry(frame, textvariable=panel_size_var, font=("Arial", 12)).pack(pady=5)

# Appliances Selection (Centered)
tk.Label(frame, text="Select Appliances:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
appliance_frame = tk.Frame(frame, bg="#f0f0f0")
appliance_frame.pack(pady=5)

for appliance, var in appliance_vars.items():
    tk.Checkbutton(appliance_frame, text=appliance.title(), variable=var, font=("Arial", 12), bg="#f0f0f0").pack(anchor="center")

# Default lighting (locked)
tk.Label(frame, text="Lighting (Default): ✔", font=("Arial", 12, "bold"), fg="green", bg="#f0f0f0").pack(pady=5)

# Calculate Button (Centered)
tk.Button(frame, text="Calculate Solar Output", command=calculate_solar_output, font=("Arial", 12, "bold"), bg="#007BFF", fg="white").pack(pady=15)

root.mainloop()
