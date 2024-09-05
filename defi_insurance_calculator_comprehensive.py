
#!/usr/bin/env python3

import os
import random

# DeFi Insurance Calculator - Comprehensive Version

def get_asset_type():
    """Let the user choose the type of asset they're insuring."""
    print("Choose your asset type:")
    print("1. Stablecoins (e.g., USDT, USDC)")
    print("2. Altcoins (e.g., ETH, ADA, SOL)")
    print("3. NFTs")
    try:
        asset_type = int(input("Enter the corresponding number: "))
        if asset_type not in [1, 2, 3]:
            raise ValueError
        return asset_type
    except ValueError:
        print("Invalid choice. Please choose a valid number (1-3).")
        return get_asset_type()

def get_live_price(asset_type):
    """Simulate fetching live prices for the selected asset type."""
    if asset_type == 1:
        return random.uniform(0.99, 1.01)  # Stablecoin prices
    elif asset_type == 2:
        return random.uniform(1000, 4000)  # Altcoins like ETH
    elif asset_type == 3:
        return random.uniform(500, 10000)  # NFTs have varying values

def risk_scoring(volatility, liquidity, protocol_risk, contract_vulnerabilities, external_factors, asset_type):
    """Calculate the risk score based on multiple risk factors and asset type."""
    asset_risk_weight = {1: 0.7, 2: 1.0, 3: 1.2}  # Risk weight for Stablecoin, Altcoins, NFTs respectively
    total_risk = (
        (volatility * 0.25) +
        (liquidity * 0.2) +
        (protocol_risk * 0.25) +
        (contract_vulnerabilities * 0.2) +
        (external_factors * 0.1)
    ) * asset_risk_weight[asset_type]
    return total_risk

def calculate_insurance_premium(asset_value, coverage_duration, risk_score, plan_tier):
    """Calculate the insurance premium based on asset value, duration, risk score, and plan tier."""
    base_rate = 0.01  # 1% base rate
    risk_factor = risk_score / 10  # scaling risk factor
    plan_rate = {"basic": 1.0, "standard": 1.25, "premium": 1.5}
    
    premium = asset_value * (base_rate + risk_factor) * (coverage_duration / 12) * plan_rate[plan_tier]
    return round(premium, 2)

def get_risk_input():
    """Get user input for various risk factors."""
    try:
        volatility = float(input("Enter the market volatility (1-10): "))
        liquidity = float(input("Enter the liquidity risk (1-10): "))
        protocol_risk = float(input("Enter the protocol risk (1-10): "))
        contract_vulnerabilities = float(input("Enter the smart contract vulnerability risk (1-10): "))
        external_factors = float(input("Enter external risks (regulatory, hacks, etc.) (1-10): "))
        return volatility, liquidity, protocol_risk, contract_vulnerabilities, external_factors
    except ValueError:
        print("Please enter valid numbers between 1 and 10.")
        return get_risk_input()

def choose_plan_tier():
    """Allow the user to choose the insurance plan tier."""
    print("Choose your insurance plan tier:")
    print("1. Basic")
    print("2. Standard")
    print("3. Premium")
    try:
        plan_choice = int(input("Enter the corresponding number: "))
        if plan_choice == 1:
            return "basic"
        elif plan_choice == 2:
            return "standard"
        elif plan_choice == 3:
            return "premium"
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return choose_plan_tier()

def generate_report(asset_value, asset_type, coverage_duration, risk_score, premium, plan_tier):
    """Generate a summary report for the user."""
    asset_types = {1: "Stablecoin", 2: "Altcoin", 3: "NFT"}
    print("\n--- Insurance Report ---")
    print(f"Asset Type: {asset_types[asset_type]}")
    print(f"Asset Value: ${asset_value}")
    print(f"Coverage Duration: {coverage_duration} months")
    print(f"Chosen Plan: {plan_tier.capitalize()}")
    print(f"Risk Score: {round(risk_score, 2)}/10")
    print(f"Estimated Premium: ${premium}")
    print("------------------------")

def main():
    print("Welcome to the Comprehensive DeFi Insurance Calculator\n")

    # Step 1: Get the asset type and value
    asset_type = get_asset_type()
    live_price = get_live_price(asset_type)
    
    try:
        asset_quantity = float(input(f"Enter the quantity of your {['Stablecoin', 'Altcoin', 'NFT'][asset_type - 1]}: "))
        asset_value = live_price * asset_quantity
        coverage_duration = int(input("Enter the coverage duration in months: "))
        
        # Step 2: Get risk input from user
        volatility, liquidity, protocol_risk, contract_vulnerabilities, external_factors = get_risk_input()
        
        # Step 3: Get plan tier from user
        plan_tier = choose_plan_tier()
        
        # Step 4: Calculate risk score
        risk_score = risk_scoring(volatility, liquidity, protocol_risk, contract_vulnerabilities, external_factors, asset_type)
        
        # Step 5: Calculate insurance premium
        premium = calculate_insurance_premium(asset_value, coverage_duration, risk_score, plan_tier)
        
        # Step 6: Generate a summary report
        generate_report(asset_value, asset_type, coverage_duration, risk_score, premium, plan_tier)
    
    except ValueError:
        print("Please enter a valid number for asset quantity and coverage duration.")
        main()

if __name__ == "__main__":
    # Ensure the script is running in an interactive terminal session
    if os.isatty(0):
        main()
    else:
        print("This script is intended to be run in a terminal session.")
