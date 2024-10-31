# Ooba Calculator Package

This package automates the process of calculating transfer costs on the [Ooba Transfer Cost Calculator](https://www.ooba.co.za/home-loan/transfer-cost-calculator/) using Selenium. The package runs in headless mode, making it ideal for server environments.

## Features

- Headless browser mode for server compatibility
- Automated data entry and submission on the Ooba calculator website
- Retry mechanism for reliability in case of failed attempts
- Supports multiple property and purchaser types

## Installation

1. **Install Dependencies**:
   ```bash
   pip install selenium
   ```

## Usage

```python
from packages.ooba_calculator import OobaCalculator

# Initialize the calculator
calculator = OobaCalculator(headless=True)

# Perform the calculation
total_cost = calculator.calculate_transfer_costs(
    purchase_price="5000000",
    loan_amount="4000000",
    property_type="Sectional",
    vat_registered="Yes",
    purchaser_status="Natural Person"
)

# Print the result
if total_cost:
    print("Total Cost:", total_cost)
else:
    print("Calculation failed.")
```

## Parameters

- purchase_price (str): The total purchase price including VAT. Example: "5000000"
- loan_amount (str): The loan amount required. Example: "4000000"
- property_type (str): Type of property ownership. Options: "Freehold" or "Sectional".
- vat_registered (str): Seller VAT registration status. Options: "Yes" or "No".
- purchaser_status (str): Status of the purchaser. Options: "Natural Person", "Company", "Closed Corporation", "Trust".

## Requirements

This package relies on Selenium WebDriver to control the browser for automating the data entry and retrieval of results. The following are required:

Google Chrome (or Chromium) installed on the system.
ChromeDriver: This must match the installed version of Chrome and be accessible in the system's PATH.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as you see fit. See the LICENSE file for more details.
