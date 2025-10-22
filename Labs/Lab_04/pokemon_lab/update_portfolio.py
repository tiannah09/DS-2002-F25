#!/usr/bin/env python3
import sys
import json
from pathlib import Path
import pandas as pd


# Function 1: Load Lookup Data

def _load_lookup_data(lookup_dir: str) -> pd.DataFrame:
    all_data = []

    for file in Path(lookup_dir).glob("*.json"):  # no space; matches files correctly
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        df = pd.json_normalize(data["data"])

        
        holo = pd.to_numeric(df.get("tcgplayer.prices.holofoil.market"), errors="coerce")
        norm = pd.to_numeric(df.get("tcgplayer.prices.normal.market"),  errors="coerce")
        df["card_market_value"] = holo.fillna(norm).fillna(0.0)

        
        df = df.rename(columns={
            "id": "card_id",
            "name": "card_name",
            "number": "card_number",
            "set.id": "set_id",
            "set.name": "set_name",
        })

        cols = ["card_id", "card_name", "card_number", "set_id", "set_name", "card_market_value"]
        all_data.append(df[cols])

    if not all_data:
        return pd.DataFrame(columns=["card_id","card_name","card_number","set_id","set_name","card_market_value"])

    lookup_df = pd.concat(all_data, ignore_index=True)
    lookup_df = lookup_df.drop_duplicates(subset=["card_id"], keep="first")
    return lookup_df



# Function 2: Load Inventory Data

def _load_inventory_data(inventory_dir: str) -> pd.DataFrame:
    frames = []
    for file in Path(inventory_dir).glob("*.csv"):
        df = pd.read_csv(file)
        df["card_id"] = df["set_id"].astype(str) + "-" + df["card_number"].astype(str)
        frames.append(df)

    if not frames:
        return pd.DataFrame(columns=[
            "card_name","set_id","card_number","binder_name","page_number","slot_number","card_id"
        ])

    return pd.concat(frames, ignore_index=True)


# Function 3: Update Portfolio 

def update_portfolio(inventory_dir: str, lookup_dir: str, output_file: str) -> None:
    lookup_df    = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)

    final_cols = [
        "index","card_id","card_name","set_id","set_name",
        "card_number","card_market_value","binder_name","page_number","slot_number"
    ]

    
    if inventory_df.empty:
        print("Error: Inventory is empty.", file=sys.stderr)
        pd.DataFrame(columns=final_cols).to_csv(output_file, index=False)
        return

    
    lookup_cols = ["card_id","card_name","set_id","set_name","card_number","card_market_value"]
    lkp = lookup_df[lookup_cols].add_suffix("_lkp")
    lkp = lkp.rename(columns={"card_id_lkp": "card_id"})  # keep the join key unsuffixed
    merged = inventory_df.merge(lkp, on="card_id", how="left")

    
    default = pd.Series([pd.NA] * len(merged), index=merged.index)

    
    merged["card_name"]   = merged.get("card_name_lkp", default).fillna(merged.get("card_name", default))
    merged["set_id"]      = merged.get("set_id_lkp", default).fillna(merged.get("set_id", default))
    merged["set_name"]    = merged.get("set_name_lkp", default).fillna(merged.get("set_name", default))
    merged["card_number"] = merged.get("card_number_lkp", default).fillna(merged.get("card_number", default))

    
    price_series = merged.get("card_market_value_lkp", default)
    merged["card_market_value"] = pd.to_numeric(price_series, errors="coerce").fillna(0.0)

    
    for col in ("binder_name","page_number","slot_number"):
        if col not in merged:
            merged[col] = pd.NA

    
    merged["index"] = (
        merged["binder_name"].astype(str) + "-" +
        merged["page_number"].astype(str) + "-" +
        merged["slot_number"].astype(str)
    )

    
    for col in final_cols:
        if col not in merged:
            merged[col] = pd.NA

    merged[final_cols].to_csv(output_file, index=False)
    print(f"Portfolio written to {output_file}")

def main():
    """Production mode: builds real portfolio."""
    update_portfolio(
        inventory_dir="./card_inventory/",
        lookup_dir="./card_set_lookup/",
        output_file="card_portfolio.csv",
    )

def test():
    """Test mode: uses test data."""
    update_portfolio(
        inventory_dir="./card_inventory_test/",
        lookup_dir="./card_set_lookup_test/",
        output_file="test_card_portfolio.csv",
    )



# Main Block

if __name__ == "__main__":
    # Default to Test Mode for this lab
    print("Running in Test Mode...", file=sys.stderr)
    update_portfolio(
        "./card_inventory_test/",
        "./card_set_lookup_test/",
        "test_card_portfolio.csv"
    )

if __name__ == "__main__":
    print("[INFO] Starting update_portfolio in Test Mode...", file=sys.stderr)
    test()


