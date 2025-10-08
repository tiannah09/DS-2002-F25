# Course Catalog Schema (Normalized)

This schema documents the flattened CSV found in `clean_course_catalog.csv`.

| Column Name  | Required Data Type | Brief Description                                   |
| :---         | :---               | :---                                                |
| `name`       | `VARCHAR(100)`     | Instructor full name.                               |
| `role`       | `VARCHAR(20)`      | Instructor role for the course (e.g., Primary, TA).|
| `course_id`  | `VARCHAR(16)`      | Course code (e.g., DS2002, PLAP3140).               |
| `title`      | `VARCHAR(200)`     | Official course title.                              |
| `level`      | `INT`              | Course level number (e.g., 200, 300, 400).          |
| `section`    | `VARCHAR(10)`      | Section identifier (e.g., 001, 100).                |


