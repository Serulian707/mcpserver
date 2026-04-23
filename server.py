
from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP(name="Course Assistant MCP Server")

COURSES = {
    "ai": {
        "title": "Introduction to Artificial Intelligence",
        "instructor": "Dr. Sara",
        "credit_hours": 3
    },
    "ml": {
        "title": "Machine Learning",
        "instructor": "Dr. Omar",
        "credit_hours": 3
    },
    "db": {
        "title": "Database Systems",
        "instructor": "Dr. Mona",
        "credit_hours": 4
    }
}

@mcp.tool()
def get_course_info(course_name: str) -> dict:
    """Return information about a course by its short name."""
    course_name = course_name.strip().lower()
    if course_name in COURSES:
        return COURSES[course_name]
    return {"error": "Course not found"}

@mcp.tool()
def calculate_final_grade(assignments: float, midterm: float, final_exam: float) -> dict:
    """Calculate total grade from three assessment components."""
    total = assignments + midterm + final_exam
    return {
        "assignments": assignments,
        "midterm": midterm,
        "final_exam": final_exam,
        "total": total
    }

@mcp.tool()
def days_until_deadline(deadline_date: str) -> dict:
    """Return number of days between today and a deadline. Format: YYYY-MM-DD"""
    today = datetime.today().date()
    deadline = datetime.strptime(deadline_date, "%Y-%m-%d").date()
    diff = (deadline - today).days
    return {
        "today": str(today),
        "deadline": str(deadline),
        "days_remaining": diff
    }

@mcp.tool()
def gpa_to_letter(gpa: float) -> dict:
    """
    Convert GPA (0–4 scale) to letter grade.
    """
    if gpa >= 3.75:
        letter = "A"
    elif gpa >= 3.25:
        letter = "A-"
    elif gpa >= 2.75:
        letter = "B"
    elif gpa >= 2.25:
        letter = "B-"
    elif gpa >= 1.75:
        letter = "C"
    elif gpa >= 1.25:
        letter = "C-"
    elif gpa >= 0.75:
        letter = "D"
    else:
        letter = "F"

    return {"gpa": gpa, "letter": letter}

    
if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
