import numpy as np
print("Student Performance Analysis System")
def generate_marks(students,subjects):
    try:
        if int(students)>0 and int(subjects)>0:
            marks=np.random.randint(low=0,high=101,size=(int(students),int(subjects)))
            return marks
        else:
            print("Enter valid number of student and subject.")
    except Exception as e:
        print(f"An error occur which is {e}.")
def performance_analyse(marks):
    if not isinstance(marks, np.ndarray):
        raise TypeError("Marks must be a array")
    if marks.size == 0:
        raise ValueError("Marks array is empty")
    analysis={}
    analysis["Student_avg"]=np.mean(marks,axis=1)
    analysis["Student_total"]=np.sum(marks,axis=1)
    analysis["Student_SD"]=np.std(marks,axis=1)
    analysis["Subjective_avg"]=np.mean(marks,axis=0)
    analysis["Subjective_max"]=np.max(marks,axis=0)
    analysis["Subjective_min"]=np.min(marks,axis=0)
    analysis["Class_avg"]=np.mean(marks)
    analysis["Topper_index"]=np.argmax(analysis["Student_total"])
    return analysis
def grades(student_avg):
    if not isinstance(student_avg,np.ndarray):
        raise TypeError("Input must be an array")
    grade=np.where(
        student_avg >=85,"Excellent",
        np.where(
            student_avg>=70,"Good",
            np.where(
                student_avg>=50,"Average",
                "Need Improvement")))
    return grade
def main():
    STUDENTS=20
    SUBJECTS=5
    marks=generate_marks(STUDENTS,SUBJECTS)
    analysis=performance_analyse(marks)
    grade=grades(analysis["Student_avg"])
    print("\n=== Student Performance Analyzer ===\n")
    for i in range(STUDENTS):
        print(f"Student {i+1:02d} | Avg: {analysis['Student_avg'][i]:.2f} | Grade: {grade[i]}")
    print("\n--- Class Insights ---")
    print(f"Class Average: {analysis['Class_avg']:.2f}")
    print(f"Topper: Student {analysis['Topper_index'] +1}")

if __name__=="__main__":
    main()
