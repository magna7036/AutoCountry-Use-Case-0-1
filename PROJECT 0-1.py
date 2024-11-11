class CarFinder:
   def __init__(self):
       self.allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
   def print_allowed_vehicles(self):
       print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
       for vehicle in self.allowed_vehicles:
           print(vehicle)
   def display_menu(self):
       print("\n------ AutoCountry Vehicle Finder v0.1 ------")
       print("1. Print all Allowed Vehicles")
       print("2. Exit")
   def run(self):
       while True:
           self.display_menu()
           choice = input("Enter your choice: ")
           if choice == '1':
               self.print_allowed_vehicles()
           elif choice == '2':
               print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
               break
           else:
               print("Invalid choice. Please choose again.")

if __name__ == "__main__":
   car_finder = CarFinder()
   car_finder.run()