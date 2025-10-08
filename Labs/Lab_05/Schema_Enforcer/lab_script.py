# ---- Part 1: Acquisition and Flexible Formatting ----

import csv
import json

# ---------- Task 1: Tabular CSV with type inconsistencies ----------
# columns: student_id(INT), major(STR), GPA(FLOAT but some ints),
#          is_cs_major(BOOL but saved as 'Yes'/'No'), credits_taken(FLOAT but saved as STR)

survey_rows = [
    # student_id, major,     GPA, is_cs_major, credits_taken
    [101,         "CS",      3,   "Yes",       "15.0"],    
    [102,         "Econ",    3.5, "No",        "12.5"],
    [103,         "WGS",     2,   "No",       "9.0"],     
    [104,         "PLAP",    3.2, "Yes",       "10.5"],
    [105,         "DS",      4,   "Yes",       "18.0"],    
]

with open("raw_survey_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["student_id", "major", "GPA", "is_cs_major", "credits_taken"])
    writer.writerows(survey_rows)

print("Wrote raw_survey_data.csv")

# ---------- Task 2: Hierarchical JSON (nested) ----------
course_catalog = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "PLAP3140",
        "section": "100",
        "title": "Mass Media & American Politics",
        "level": 300,
        "instructors": [
            {"name": "Paul Freedman", "role": "Primary"}
        ]
    },
    {
        "course_id": "WGS2600",
        "section": "001",
        "title": "Human Sexualities",
        "level": 200,
        "instructors": [
            {"name": "Lisa Speidel", "role": "Primary"}
        ]
    },
    {
        "course_id": "WGS2650",
        "section": "001",
        "title": "Streaming Sexualities",
        "level": 200,
        "instructors": [
            {"name": "Lisa Speidel", "role": "Primary"},
            {"name": "Andre Cavalcante", "role": "Primary"}
        ]
    },
    {
        "course_id": "DS3001",
        "section": "003",
        "title": "Foundations of ML",
        "level": 300,
        "instructors": [
            {"name": "Michael Freenor", "role": "Primary"}
        ]
    },
    {
        "course_id": "PLPT4200",
        "section": "001",
        "title": "Feminist Political Theory",
        "level": 400,
        "instructors": [
            {"name": "Lawrie Balfour", "role": "Primary"}
        ]
    }
]

with open("raw_course_catalog.json", "w") as f:
    json.dump(course_catalog, f, indent=2)

print("Wrote raw_course_catalog.json")


# ---- Part 2: Data Validation and Type Casting ----

import pandas as pd
import json

# ---------- Task 3: Clean and validate the CSV data ----------

# 1) Load the raw CSV
df = pd.read_csv("raw_survey_data.csv")

# 2) Enforce Boolean type for is_cs_major ('Yes'/'No' -> True/False)
df["is_cs_major"] = df["is_cs_major"].replace({"Yes": True, "No": False})

# 3) Enforce numeric (float) types for GPA and credits_taken
df = df.astype({
    "GPA": "float64",
    "credits_taken": "float64"
})


# 4) Save cleaned CSV
df.to_csv("clean_survey_data.csv", index=False)
print("Wrote clean_survey_data.csv")

# ---------- Task 4: Normalize the JSON data ----------

# 1) Load the raw JSON
with open("raw_course_catalog.json", "r") as f:
    data = json.load(f)

# 2) Flatten instructors list with course metadata as columns
norm = pd.json_normalize(
    data,
    record_path=["instructors"],        
    meta=["course_id", "title", "level", "section"] 
)


# 3) Save normalized CSV
norm.to_csv("clean_course_catalog.csv", index=False)
print("Wrote clean_course_catalog.csv")
