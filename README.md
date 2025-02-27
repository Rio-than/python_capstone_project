# python_capstone_project
# **Python Capstone Project Proposal**  

## **Project Overview**  

### **Project Title**  
**Solar Power Output and Energy Demand Calculator**  

### **Project Summary**  
This project is a Python-based solar energy calculator using Tkinter. It allows users to select a region in Kenya from a specified number of regions;kisumu,bomet,nyandarua,mandera,mombasa, specify a solar panel size, and choose household appliances from a list of common appliances;television,sound system,iron box,lighting set as default, to estimate solar power generation and daily energy consumption. Based on the calculations, the program provides recommendations on whether the panel size is sufficient or if an upgrade is necessary.  

---

## **Problem Statement**  

### **What problem will your Python project solve?**  
- Many people in Kenya struggle to estimate the correct solar panel size for their energy needs.  
- This tool helps users determine if their selected panel can generate enough power for daily use based on weather data for different regions.  

### **Why is this solution needed?**  
- Provides data-driven insights into solar panel efficiency across various regions.  
- Helps users make informed decisions before purchasing solar panels.
- Helps users who want to add more appliances from the listed appliances.
- Helps solar panel distributors to advice their clients on most suitable panel size.  
- Encourages the adoption of renewable energy by simplifying the estimation process.  

### **Who will use this program?**  
- Homeowners and institutions considering solar panel installations.  
- Solar energy consultants and technicians. 
- Small businesses looking to optimize solar energy usage.  

---

## **Technical Details**  

### **Python Components**  

1. **Python Version**  
   - Python **3.13**  

2. **Core Python Concepts to be Used**  
   - Functions  
   - Classes and Objects  
   - Error Handling  
   - Conditional Statements and Loops  
   - Tkinter for GUI  

3. **Basic Python Libraries**  
   - `tkinter` for graphical user interface  
   - `ttk` for improved widgets  
   - `messagebox` for displaying alerts  

4. **Development Tools**  
   - **Editor**: VS Code  
   - **Version Control**: Git/GitHub  

---

## **Program Structure**  

### **Core Features**  

1. **Region-Based Solar Output Calculation**  
   - Users select a region in Kenya to retrieve solar irradiance and cloud cover data.  
   - The program uses this data to estimate the daily solar energy output for the selected region.  

2. **Solar Panel Size Input and Validation**  
   - Users can manually enter a panel size or select from predefined sizes (small, medium, or large).  
   - The program ensures the input is valid and provides feedback if corrections are needed.  

3. **Energy Demand Calculation Based on Appliances**  
   - Users select common household appliances they intend to power using solar energy.  
   - The program calculates the total daily energy consumption based on selected appliances.  

4. **Solar Output vs. Power Demand Comparison**  
   - The program compares the estimated solar energy output with the total power demand.  
   - If the panel is insufficient, a recommendation is given to consider a larger panel and details of panel supplier given 

---

### **User Interface**  

This project features a **Graphical User Interface (GUI) using Tkinter** with the following elements:  

- **Region Selection:** A dropdown menu to choose a region in Kenya.  
- **Panel Size Input:** A text box for entering a specific panel size or selecting predefined options.  
- **Appliance Selection:** Checkboxes for choosing appliances that require solar power.  
- **Calculation Button:** A button that triggers the energy calculation process.  
- **Results Display:** A pop-up message displaying the estimated solar power output, energy demand, and recommendations.  

---

## **Project Timeline**  

| Day | Programming Tasks | Status |
|------|------------------|---------|
| 1 | Set up project structure |  Done |
| 2 | Implement core functions | Done |
| 3 | Create user interface |  Done |
| 4 | Testing and debugging |  In Progress |
| 5 | Project documentation | Not Started |

---

## **Program Design**  

### **Functions and Classes Overview**  
- The program is structured using **classes** to manage solar panel attributes and energy calculations.  
- **Functions** handle user input validation, energy demand calculations, and power output comparisons.  
- The **GUI components** interact with these functions to provide a smooth user experience.  

---

### **Data Storage**  
- The program does not require a database.  
- It uses a **hardcoded dictionary** to store solar irradiance and cloud cover values for different regions.  

---

### **Error Handling**  
- Ensures valid user input for panel size and region selection.  
- Displays appropriate error messages for invalid or missing data.  
- Prevents crashes due to incorrect input formats.  

---

## **Testing Strategy**  

- **Unit Testing:**  
  - Verify that solar panel output calculations return correct values.  
  - Test if invalid inputs trigger appropriate error messages.  
  - Ensure the program functions correctly with different appliance selections.  

- **User Testing:**  
  - Conduct tests with sample users to gather feedback on usability.  
  - Identify and fix any issues with the user interface.  

---

## **Project Delivery**  

### **Running the Program**  
1. Install **Python 3.13**  
2. Run the program using the command:  
   ```
   python solar_panel.py
   ```

---

### **Sample Usage**  
**Example Scenario:**  
- **Region Selected:** Kisumu  
- **Panel Size:** 1.0 m²  
- **Appliances:** Television, Iron Box  

**Expected Output:**  
- **Projected Daily Solar Output:** 2.42 kWh  
- **Total Daily Power Requirement:** 1.65 kWh  
- **Conclusion:** The solar panel can meet the daily power demand.  

---

## **Potential Challenges**  

| Challenge | Solution |
|-----------|----------|
| User enters invalid data | Implement robust input validation |
| No current data on Kenya solar irradiance on NASA api|Try other weather api's|
| Tkinter navigation challenges | Consider other deployment interfaces and more exposure to tkinter |
| Limited appliance options | Add more posssible user appliances |

---

## **Future Improvements**  

- **Recommendation**:Add a live url link when recommending a store to the user.  
- **Data Visualization**: Add graphs to display energy usage vs. solar output.  
- **Expanded Appliance List**: Enable users to add custom appliances with power ratings.
- **Expanded region scope**:Add more regions accross the country that can access this service.
- **Appliance variables**:Enable the user to include the number of instances of an individual appliance.
- **Panel Efficiency**:Enhance the program to include the varied factors that can affect panel efficiency. 
- **Mobile Compatibility**: Convert the program into a mobile-friendly web application.
- **Real-Time weather Data**: Integrate an API to fetch live solar irradiance data.  

---

