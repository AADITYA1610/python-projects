import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#creating class:
class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
    
    def analyze_data(self):
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
        
        # Plotting age vs frequency (Age Distribution)
        self.plot_age_frequency()
        
        # Plotting age vs experience
        self.plot_age_experience()
        
        # Plotting experience vs salary
        self.plot_experience_salary()
        
        # Display descriptive statistics
        self.display_descriptive_statistics()
    def plot_age_frequency(self):
        self.data['Age'].hist(bins=20, color='skyblue', edgecolor='black')
        plt.title('Age vs Frequency')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
        
    def plot_age_experience(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['Age'], self.data['Experience'], color='orange', alpha=0.7)
        plt.title('Age vs Experience')
        plt.xlabel('Age')
        plt.ylabel('Experience (years)')
        plt.grid(True)
        plt.show()
    
    def plot_experience_salary(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['Experience'], self.data['Salary'], color='green', alpha=0.7)
        plt.title('Experience vs Salary')
        plt.xlabel('Experience (years)')
        plt.ylabel('Salary')
        plt.grid(True)
        plt.show()
    
    def save_data(self):
        self.data.to_csv(self.file_path, index=False)
        print(f"Data saved to '{self.file_path}'.")

    
    def filter_data(self, min_salary, min_experience):
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
        
        filtered_data = self.data[(self.data['Salary'] >= min_salary) & (self.data['Experience'] >= min_experience)]
        
        if len(filtered_data) == 0:
            print("No data matches the filter criteria.")
        else:
            print("\nFiltered Data:")
            print(filtered_data)
        
        return filtered_data
    
    def add_entry(self, name, age, salary, experience):
        new_entry = pd.DataFrame({'Name': [name], 'Age': [age], 'Salary': [salary], 'Experience': [experience]})
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
        print(f"New entry added successfully:\n{name}, {age}, {salary}, {experience}")
    
    def display_descriptive_statistics(self):
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
        
        # Calculate descriptive statistics using NumPy
        mean_age = np.mean(self.data['Age'])
        median_salary = np.median(self.data['Salary'])
        max_experience = np.max(self.data['Experience'])
        
        print(f"\nDescriptive Statistics:")
        print(f"Mean Age: {mean_age:.2f}")
        print(f"Median Salary: {median_salary:.2f}")
        print(f"Maximum Experience: {max_experience} years")
    
    def save_data(self):
        if self.data is None:
            print("No data to save. Please load or add data.")
            return
        
        self.data.to_csv(self.file_path, index=False)
        print(f"Data saved to '{self.file_path}'.")

def main():
    print("Enhanced Data Analysis Tool ")
    file_path = 'employee_data.csv'
    analyzer = DataAnalyzer(file_path)# Create DataAnalyzer instance
    analyzer.load_data()# Load data
    while True:
        print("\nOptions:")
        print("1. Analyze data (Custom Plots and Descriptive Statistics)")
        print("2. Filter data (Show Filtered Data)")
        print("3. Add new entry")
        print("4. Display descriptive statistics")
        print("5. Save data")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        if choice == '1':
            analyzer.analyze_data()
        elif choice == '2':
            min_salary = float(input("Enter minimum salary threshold: "))
            min_experience = int(input("Enter minimum experience threshold (in years): "))
            analyzer.filter_data(min_salary, min_experience)
        elif choice == '3':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            experience = int(input("Enter experience (in years): "))
            analyzer.add_entry(name, age, salary, experience)
        elif choice == '4':
            analyzer.display_descriptive_statistics()
        elif choice == '5':
            analyzer.save_data()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()




