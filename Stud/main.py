import stud, exception, log

def process_students(students_data):
    print("--- Processing Student Results ---")
    
    for student in students_data:
        try:
            name = student.get("name")
            marks = student.get("marks")

            # Check for missing student information
            if not name or marks is None:
                #raise KeyError(f"Missing name or marks in record: {student}")
                log.log_msg("error", f"Missing name or marks in record: {student}")
                continue
                

            # Check if exactly 5 subjects are provided
            if len(marks) != 5:
                #raise ValueError(f"{name} must have exactly 5 subjects. Found {len(marks)}.")
                log.log_msg("error", f"{name} must have exactly 5 subjects. Found {len(marks)}.")
                continue

            # Perform calculations
            results = stud.calculate_result(marks)
            print(f"Student: {name}, Result: {results}")
        except Exception as e:
            log.log_msg("error", f"Exception occurred while processing student {student}: {e}")
            continue

sample_students = [
    {"name": "Alice", "marks": [85, 90, 78, 92, 88]},                 # Valid
    {"name": "Bob", "marks": [40, 30, 55, 60, 45]},                   # Valid (Fails a subject)
    {"name": "Charlie", "marks": [70, 105, 80, 90, 85]},              # Error: Mark > 100
    {"name": "Daisy", "marks": [80, "abc", 75, 70, 90]},              # Error: Non-numeric
    {"name": "", "marks": [60, 70, 80, 90, 100]},                     # Error: Missing Name
    {"name": "Ethan", "marks": [80, 85, 90]},                         # Error: Missing subjects
]

if __name__ == "__main__":
    process_students(sample_students)