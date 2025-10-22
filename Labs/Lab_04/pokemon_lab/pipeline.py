#!/usr/bin/env python3
import sys
import update_portfolio as up
import generate_summary as gs


# Function 1: run_production_pipeline()
def run_production_pipeline() -> None:
    print("[PIPELINE] Starting production run…", file=sys.stderr)

    print("[PIPELINE] ETL: building card_portfolio.csv …", file=sys.stderr)
    up.main()  # runs ETL in production mode (./card_inventory/ + ./card_set_lookup/)

    print("[PIPELINE] REPORT: generating portfolio summary …", file=sys.stderr)
    gs.main()  # reads card_portfolio.csv and prints summary

    print("[PIPELINE] Completed successfully.", file=sys.stderr)


# Main Block
if __name__ == "__main__":
    run_production_pipeline()



