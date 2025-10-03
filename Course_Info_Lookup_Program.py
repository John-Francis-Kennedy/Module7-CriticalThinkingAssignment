#!/usr/bin/env python3
"""Course Information Lookup (with UDFs & Exceptions)

- Stores course details in dictionaries.
- Uses user-defined functions for normalization, lookup, rendering, and the main loop.
- Uses a custom exception (CourseNotFoundError) and structured try/except blocks.
- Press ENTER on an empty prompt to quit.
"""

from typing import Dict


class CourseNotFoundError(Exception):
    """Raised when a course code does not exist in the data store."""


COURSE_ROOMS: Dict[str, str] = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

COURSE_INSTRUCTORS: Dict[str, str] = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

COURSE_TIMES: Dict[str, str] = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def normalize_course_code(raw: str) -> str:
    """Return a normalized (uppercased, trimmed) course code string."""
    return (raw or "").strip().upper()


def lookup_course(course_code: str) -> dict:
    """Return a dictionary with course info or raise CourseNotFoundError."""
    code = normalize_course_code(course_code)
    if code in COURSE_ROOMS:
        return {
            "course": code,
            "room": COURSE_ROOMS[code],
            "instructor": COURSE_INSTRUCTORS[code],
            "time": COURSE_TIMES[code],
        }
    raise CourseNotFoundError(f"Unknown course: {course_code!r}")


def render_info(info: dict) -> str:
    """Return a nicely formatted multi-line string for a course info dict."""
    return (
        f"\nCourse:      {info['course']}\n"
        f"Room:        {info['room']}\n"
        f"Instructor:  {info['instructor']}\n"
        f"Meeting:     {info['time']}\n"
    )


def main() -> None:
    print("Course Information Lookup (press ENTER to quit)\n")
    try:
        while True:
            raw = input("Enter a course number (e.g., CSC101, NET110): ")
            if not raw.strip():
                print("Goodbye!")
                break

            try:
                info = lookup_course(raw)
                print(render_info(info))
            except CourseNotFoundError as e:
                valid = ", ".join(sorted(COURSE_ROOMS.keys()))
                print(f"{e}. Please try one of: {valid}\n")
    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("\nInterrupted. Exiting...")


if __name__ == "__main__":
    main()
