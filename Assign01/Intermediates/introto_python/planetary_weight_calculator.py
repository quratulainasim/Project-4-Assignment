def main():
    weight_on_earth = float(input("Enter your weight on Earth (in kg): "))
    planet_gravitys={
            "Mercury": 0.38,
            "Venus": 0.91,
            "Mars": 0.38,
            "Jupiter": 2.34,    
            "Saturn": 1.06,
            "Uranus": 0.92,         
            "Neptune": 1.19,    
            }                               

    for planet in planet_gravitys:
        print(f' - {planet}')    
    planet_choice=input("Choice the planet:").title()
    if planet_choice in planet_gravitys:
            total_gravity=planet_gravitys[planet_choice]* weight_on_earth 
            print(f"Your weight on {planet_choice} is: {total_gravity}: kg")
    else:
            print("Invalid choice. Please select a valid planet.")


if __name__ == "__main__":
    main()