.PHONY: all fetch analyze clean

analyze: fetch
	@echo "Starting analysis: reading JSON from raw_metars/ and writing weather_report.csv..."
	@./analyze_data.sh
	@echo "Finished analysis: results saved to weather_report.csv"
	@echo "Pipeline completed successfully."

all: analyze

fetch:
	@echo "Starting fetch: retrieving METAR JSON and saving to raw_metars/..."
	@./fetch_metars.sh
	@echo "Finished fetch: raw JSON saved in raw_metars/"

clean:
	@echo "Cleaning generated files (weather_report.csv and raw_metars/)..."
	@rm -rf weather_report.csv raw_metars
	@echo "Clean complete."

