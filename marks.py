import csv
def analyze_marks():
    students = []
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames or not {"Name", "Marks"}.issubset(reader.fieldnames):
                print("Invalid CSV headers!")
                return
            for row in reader:
                name = (row["Name"] or "").strip()
                marks_text = (row["Marks"] or "").strip()
                if not name or not marks_text:
                    print("Invalid student record!")
                    return
                marks = float(marks_text)
                if not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100!")
                    return
                students.append({
                    "name": name,
                    "marks": marks
                })
        if not students:
            print("No student records found!")
            return
        topper = max(students, key=lambda s: s["marks"])
        total = sum(s["marks"] for s in students)
        average = total / len(students)
        print("\n===== STUDENT RESULTS =====")
        print("Topper:", topper["name"])
        print("Highest Marks:", topper["marks"])
        print("Class Average:", round(average, 2))
    except FileNotFoundError:
        print("Error: students.csv not found!")
    except (ValueError, KeyError):
        print("Invalid marks or CSV data!")
    except OSError:
        print("Error reading CSV file!")
analyze_marks()
