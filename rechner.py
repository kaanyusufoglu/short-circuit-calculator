from constants import MATERIAL_RESISTIVITY

def calculate_resistance(length_m, cross_section_mm2, material):
    cross_section_m2 = cross_section_mm2 * 1e-6
    rho = MATERIAL_RESISTIVITY.get(material.lower())
    if rho is None:
        raise ValueError("Unsupported material. Choose 'copper' or 'aluminum'.")
    return (2 * rho * length_m) / cross_section_m2

def calculate_short_circuit_current(voltage_v, resistance_ohm):
    if resistance_ohm == 0:
        return float('inf')
    return voltage_v / resistance_ohm
