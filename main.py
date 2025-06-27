from calculator import calculate_resistance, calculate_short_circuit_current

def main():
    print("Short-Circuit Current Calculator")

    voltage = float(input("Enter system voltage (V): "))
    length = float(input("Enter cable length (m): "))
    cross_section = float(input("Enter conductor cross-section (mm^2): "))
    material = input("Enter conductor material (copper/aluminum): ").strip().lower()

    try:
        resistance = calculate_resistance(length, cross_section, material)
        ik = calculate_short_circuit_current(voltage, resistance)

        print(f"\n--- Results ---")
        print(f"Loop Resistance: {resistance:.4f} Ω")
        print(f"Short-Circuit Current (Ik): {ik:.2f} A")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
