# Survey Schema (Final, Clean)

This schema documents the cleaned CSV found in `clean_survey_data.csv`.

| Column Name   | Required Data Type | Brief Description                           |
| :---          | :---               | :---                                        |
| `student_id`  | `INT`              | Unique identifier for the student.          |
| `major`       | `VARCHAR(50)`      | Student’s declared major.                   |
| `GPA`         | `FLOAT`            | Cumulative grade point average (0.0–4.0).   |
| `is_cs_major` | `BOOL`             | True if the student is a CS major.          |
| `credits_taken` | `FLOAT`          | Total credits completed or in progress.     |


