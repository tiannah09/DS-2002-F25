#!/bin/bash
# refresh_card_sets.sh — batch updater for all existing Pokémon card set JSONs

echo "Refreshing all card sets in card_set_lookup/ ..."

for FILE in card_set_lookup/*.json; do
    [ -e "$FILE" ] || { echo "No JSON files found to refresh."; exit 0; }

    SET_ID=$(basename "$FILE" .json)

    echo "Updating set: $SET_ID ..."
    curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "$FILE"
    echo "Data for set '$SET_ID' has been refreshed and saved to $FILE"
done

echo "All card sets have been refreshed successfully!"

