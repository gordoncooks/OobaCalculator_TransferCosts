from packages.ooba_calculator import OobaCalculator

# Instantiate the calculator
calculator = OobaCalculator(headless=True)

# Run the calculation with inputs
total_cost = calculator.calculate_transfer_costs(
    purchase_price="5000000",
    loan_amount="4000000",
    property_type="Sectional",
    vat_registered="Yes",
    purchaser_status="Natural Person"
)

# Output the result
if total_cost:
    print("Total Cost:", total_cost)
else:
    print("Calculation failed.")
