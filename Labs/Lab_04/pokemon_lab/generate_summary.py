#!/usr/bin/env python3
import os
import sys
import pandas as pd


# Function 1: Generate the summary

def generate_summary(portfolio_file: str) -> None:
    
    if not os.path.exists(portfolio_file):
        print(f"Error: '{portfolio_file}' not found.", file=sys.stderr)
        sys.exit(1)

    
    df = pd.read_csv(portfolio_file)

    
    if df.empty:
        print("The portfolio file is empty. Nothing to summarize.")
        return

    
    total_portfolio_value = pd.to_numeric(df["card_market_value"], errors="coerce").fillna(0.0).sum()

    
    max_idx = df["card_market_value"].idxmax()
    most_valuable_row = df.loc[max_idx]

    print("==== Portfolio Summary ====")
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print("Most Valuable Card:")
    print(f"  Name : {most_valuable_row.get('card_name', 'UNKNOWN')}")
    print(f"  ID   : {most_valuable_row.get('card_id', 'UNKNOWN')}")
    print(f"  Value: ${most_valuable_row.get('card_market_value', 0.0):,.2f}")



# Function 2: Main run
def main() -> None:
    generate_summary("card_portfolio.csv")


# Function 3: Test run
def test() -> None:
    generate_summary("test_card_portfolio.csv")


# Main Block
if __name__ == "__main__":
    test()


