import numpy as np
import pandas as pd

print("=== Student Performance Analysis System ===")


def load_marks(file_path):

    try:
        df = pd.read_csv(file_path)
        return df.values, df.columns.tolist()
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found. Check the path.")
    except Exception as e:
        raise RuntimeError(f"Error while loading CSV: {e}")


def perform_analysis(marks):

    if not isinstance(marks, np.ndarray):
        raise TypeError("Marks must be a NumPy array")
    if marks.size == 0:
        raise ValueError("Marks array is empty")

    analysis = {}

    analysis["student_avg"] = np.mean(marks, axis=1)
    analysis["student_total"] = np.sum(marks, axis=1)

    analysis["subject_avg"] = np.mean(marks, axis=0)
    analysis["subject_max"] = np.max(marks, axis=0)
    analysis["subject_min"] = np.min(marks, axis=0)

    analysis["class_avg"] = np.mean(marks)
    analysis["topper_index"] = np.argmax(analysis["student_total"])

    return analysis


def assign_grades(student_avg):

    if not isinstance(student_avg, np.ndarray):
        raise TypeError("Input must be a NumPy array")

    grades = np.where(
        student_avg >= 85, "Excellent",
        np.where(
            student_avg >= 70, "Good",
            np.where(
                student_avg >= 50, "Average",
                "Need Improvement"
            )
        )
    )
    return grades


def main():

    marks, subjects = load_marks("data/marks.csv")

    students = marks.shape[0]
    subject_count = marks.shape[1]

    analysis = perform_analysis(marks)
    grades = assign_grades(analysis["student_avg"])

    print("\n--- Student-wise Performance ---")
    for i in range(students):
        print(
            f"Student {i+1:02d} | "
            f"Avg: {analysis['student_avg'][i]:.2f} | "
            f"Grade: {grades[i]}"
        )

    print("\n--- Class Insights ---")
    print(f"Number of Students : {students}")
    print(f"Number of Subjects : {subject_count}")
    print(f"Class Average      : {analysis['class_avg']:.2f}")
    print(f"Topper             : Student {analysis['topper_index'] + 1}")


if __name__ == "__main__":
    main()
