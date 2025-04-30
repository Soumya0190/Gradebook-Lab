# Gradebook-Lab
https://canvas.eee.uci.edu/courses/16697/assignments/329545


---

The **STAR method** is a structured way to describe experiences or projects by breaking them down into four components: **Situation**, **Task**, **Action**, and **Result**. Here's how you can explain the Gradebook project using this method:

### **S - Situation**:
The Gradebook project involved creating a system for managing student assignments, calculating grades, and handling categories with weighted assignments. The main objective was to enable teachers or instructors to track student performance, adjust scores, and generate reports, while also supporting the computation of class averages based on different grading methods (total points or category-based).

### **T - Task**:
The primary task was to design and implement a Gradebook system that:
- Manages student records, including adding, modifying, or removing assignments and scores.
- Supports two types of gradebook systems: Total Points and Category-based (where assignments are grouped into categories like exams, quizzes, projects, etc.).
- Generates reports that display students’ grades for individual assignments and their overall scores.
- Calculates the class average based on the grading method selected, either by total points or category weights.
- Ensures that the gradebook is balanced when using categories, i.e., the sum of category weights equals 100%.

### **A - Action**:
To achieve the task, the following actions were taken:
1. **Data Structure Design**:
   - Developed a `Student` class to represent individual students, including methods for adding and modifying assignments, and calculating the total score.
   - Created `Assignment` and `CategoryAssignment` classes to represent assignments and categorized assignments (with different categories like quizzes, exams, etc.).
   - Built a `Gradebook` class to manage multiple students and store their assignments, with methods to add, search, or remove students, and generate class reports.

2. **Grade Calculation Logic**:
   - In the `TotalPointsGradebook` class, implemented the logic for calculating grades by summing up earned points and possible points from all assignments.
   - In the `CategoryGradebook` class, built the logic for handling category weights and computing averages based on those categories, ensuring that the gradebook remained balanced by checking that category weights sum to 100%.

3. **File Handling**:
   - Designed a method (`writeGradebookRecord`) to write student grade records into files, including assignment details and final grade calculations.
   - Handled errors, such as missing files, and ensured that the file system operations were robust and clear.

4. **Class Average Calculation**:
   - Created methods in both `TotalPointsGradebook` and `CategoryGradebook` for calculating the class average based on either total points or category-based grading.

5. **User Experience**:
   - Ensured that the system allowed for easy modifications, such as adding, changing, or removing scores, and could generate comprehensive reports for students and teachers.

### **R - Result**:
As a result of these actions:
- The Gradebook system was fully functional, with features to manage student data, calculate grades, and produce reports.
- Teachers could generate grade reports, track individual student performance, and adjust scores as needed.
- The class average and grading distribution were accurately computed based on the chosen grading method.
- The system allowed for seamless handling of category-based grading, ensuring that the gradebook was balanced and that category weights were correctly enforced.
- The project successfully addressed the goal of simplifying the grading process and enhancing report generation, making it easier for both students and instructors to track academic progress.

The project ultimately provided a comprehensive and flexible system for managing grades, improving both the efficiency and accuracy of grading in educational settings.

---

# Gradebook Project README

## Project Overview
This project is designed to simulate an electronic gradebook. The gradebook can calculate student grades based on two systems: **Total Points** and **Weighted Categories**. The gradebook will store assignments, categories, and calculate grades for individual students.

### Key Features:
1. **Total Points System**: Calculate a student’s grade based on the total points earned divided by the total points available.
2. **Weighted Category System**: Calculate a student’s grade using weighted categories for assignments (e.g., Labs, Quizzes, Exams).
3. **Student Management**: Track student IDs, assignments, and their scores.
4. **Gradebook Management**: Add/remove students, add/remove assignments, and generate grade reports.

## Classes
The following classes are implemented in this project:
- **Assignment**: Represents an individual assignment, including the description, score, and total possible points.
- **CategoryAssignment**: A subclass of `Assignment` that includes a category for each assignment.
- **Student**: Stores information about a student, including their assignments and scores.
- **Gradebook**: The base class for managing students and their assignments.
- **TotalPointsGradebook**: A subclass of `Gradebook` that calculates grades using the total points system.
- **CategoryGradebook**: A subclass of `Gradebook` that calculates grades using a weighted category system.

## Class Details and Methods

### 1. **Assignment Class**
- **Constructor**: `__init__(self, description, score, total)`
  - Initializes assignment with a description, score, and total points.
- **Methods**:
  - `getDescription() -> str`: Returns the description of the assignment.
  - `getScore() -> float`: Returns the points earned.
  - `getTotal() -> float`: Returns the total points possible.
  - `changeScore(score: float)`: Changes the score for the assignment.

### 2. **CategoryAssignment Class** (Subclass of `Assignment`)
- **Constructor**: `__init__(self, description, category, score, total)`
  - Initializes the assignment with category, description, score, and total points.
- **Methods**:
  - `getCategory() -> str`: Returns the category of the assignment.

### 3. **Student Class**
- **Constructor**: `__init__(self, student_id)`
  - Initializes the student with an ID and an empty list of assignments.
- **Methods**:
  - `getId() -> int`: Returns the student’s ID.
  - `getScore(assignmentName: str) -> float`: Returns the score of an assignment by name.
  - `getScores() -> list`: Returns a list of the student's assignments.
  - `addAssignment(assignment: Assignment)`: Adds an assignment to the student’s list.
  - `changeScore(assignmentName: str, score: float)`: Changes the score of an assignment by name.
  - `removeScore(assignmentName: str)`: Removes an assignment by name.

### 4. **Gradebook Class**
- **Constructor**: `__init__(self)`
  - Initializes an empty gradebook.
- **Methods**:
  - `addStudent(student: Student)`: Adds a student to the gradebook.
  - `dropStudent(id: int)`: Removes a student from the gradebook by ID.
  - `search(id: int) -> Student`: Searches for a student by ID.
  - `addAssignment(id: int, score: Assignment)`: Adds an assignment to a student’s list by ID.

### 5. **TotalPointsGradebook Class** (Subclass of `Gradebook`)
- **Constructor**: `__init__(self)`
  - Initializes the total points gradebook.
- **Methods**:
  - `writeGradebookRecord(id: int, fileName: str)`: Writes a summary of a student's grades to a file.
  - `classAverage() -> float`: Returns the average grade of the entire class.

### 6. **CategoryGradebook Class** (Subclass of `Gradebook`)
- **Constructor**: `__init__(self)`
  - Initializes the category gradebook with categories and weights.
- **Methods**:
  - `addCategory(description: str, weight: float)`: Adds a category to the gradebook.
  - `isBalanced() -> bool`: Returns `True` if the category weights add up to 100%.
  - `writeGradebookRecord(id: int, fileName: str)`: Writes a summary of a student's grades and category breakdown to a file.
  - `classAverage() -> float`: Returns the average grade of the entire class.

---

## How to Run the Code

**Run the Script**:
   - Navigate to the folder where the script is located in your terminal.
   - Run the script with the following command:
     ```bash
     python Lab3_YOURID.py
     ```
   - This will execute the gradebook code, and the output will be saved to a specified file.

---

## Example Output
For the `TotalPointsGradebook` and `CategoryGradebook`, the gradebook file for each student should be formatted as follows:

### Total Points Gradebook Example:
```
12345678
Assignment 1
12/13
Assignment 2
14/20
Assignment 3
5/10
Total: 31/43
Percentage: 72.0930233
```

### Category Gradebook Example:
```
12345678
Labs: Lab #1
15/20
Labs: Lab #2
12/15
Midterm: Exam
40/55
Final: Exam
72/100
Final: 72.00
Midterm: 72.7272
Labs: 77.1428571
Percentage: 73.246753
```
---