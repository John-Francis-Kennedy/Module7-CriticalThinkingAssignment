# Module7-CriticalThinkingAssignment
Module7-CriticalThinkingAssignment-CourseInfoLookup Program


A Python program that stores **course room numbers**, **instructors**, and **meeting times** in dictionaries and lets a user look up details by course number.

## What’s New in This Version
- **User-Defined Functions (UDFs):**
  - `normalize_course_code(raw)` — cleans user input.
  - `lookup_course(course_code)` — fetches details or raises an exception.
  - `render_info(info)` — formats output.
  - `main()` — orchestrates I/O loop.
- **Exceptions:**
  - Custom **`CourseNotFoundError`** raised on invalid course codes.
  - `try/except` blocks in `main()` to handle errors gracefully.
  - Graceful `KeyboardInterrupt` handling (Ctrl+C).

## Run
```bash
python course_info_Lookup_Program.py
```

## Example
```
Course Information Lookup (press ENTER to quit)

Enter a course number (e.g., CSC101, NET110): CSC102

Course:      CSC102
Room:        4501
Instructor:  Alvarado
Meeting:     9:00 a.m.

Enter a course number (e.g., CSC101, NET110): csc999
Unknown course: 'csc999'. Please try one of: COM241, CSC101, CSC102, CSC103, NET110

Enter a course number (e.g., CSC101, NET110):
Goodbye!
```

## Files
- `course_info_Lookup_Program.py` – program using UDFs & exceptions
- `Module 7 - Critical Thinking Assignment - Course Info Lookup Program.docx
