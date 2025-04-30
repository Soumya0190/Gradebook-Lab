import collections

class Assignment:
    def __init__(self, name, earnedPts, possiblePts):
        self.description = name
        self.score = earnedPts
        self.total = possiblePts

    def getDescription(self) -> str:
        return str(self.description)
    
    def getScore(self) -> float:
        return float(self.score)
    
    def getTotal(self) -> float:
        return float(self.total)
    
    def changeScore(self, score: float):
        self.score = float(score)

class CategoryAssignment(Assignment):   
    def __init__(self, description1, category1, score1, total1):
        super().__init__(description1, score1, total1)
        self.category = category1

    def getCategory(self) -> str:
        return self.category

class Student:     
    def __init__(self, ID: int):
        self.assignments = list()
        self.id = ID

    def getId(self) -> int:
        return int(self.id)

    def getScore(self, assignmentName: str) -> float:
        for assignment in self.assignments:
            if assignment.getDescription() == assignmentName:
                return float(assignment.getScore())
        return None

    def addAssignment(self, score: Assignment):
        self.assignments.append(score)

    def changeScore(self, assignmentName: str, score: float):
        for assignment in self.assignments:
            if assignment.getDescription() == assignmentName:
                assignment.changeScore(score)
                return self.assignments
        return None

    def removeScore(self, assignmentName: str):
        for assignment in self.assignments:
            if assignment.getDescription() == assignmentName:
                self.assignments.remove(assignment)
                return self.assignments
        return None

    def getScores(self) -> list:
        return self.assignments

class Gradebook:
    def __init__(self):
        self.gradebook = dict()

    def addStudent(self, student: Student):
        if student.getId() in self.gradebook:
            raise Exception('Student already in gradebook')
        self.gradebook[student.getId()] = student

    def dropStudent(self, id: int):
        if id in self.gradebook:
            del self.gradebook[id]
            return self.gradebook
        return None

    def search(self, id: int) -> Student:
        return self.gradebook.get(id, None)
    
    def addAssignment(self, id: int, score: Assignment):
        student = self.search(id)
        if student:
            student.addAssignment(score)
        else:
            print(f"Student with ID {id} not found.")

class TotalPointsGradebook(Gradebook):
    def __init__(self):
        super().__init__()

    def writeGradebookRecord(self, id: int, fileName: str):
        try:
            with open(fileName, 'w') as file:
                student = self.search(id)
                if student:
                    earned_pts = 0
                    total_pts = 0
                    for assignment in student.getScores():
                        file.write(f"{assignment.getDescription()}\n")
                        fraction = f"{assignment.getScore()}/{assignment.getTotal()}"
                        file.write(f"{fraction}\n")
                        earned_pts += assignment.getScore()
                        total_pts += assignment.getTotal()

                    total_fraction = f"{earned_pts}/{total_pts}"
                    file.write(f"Total: {total_fraction}\n")
                    file.write(f"Percentage: {earned_pts / total_pts * 100:.2f}%")
                else:
                    file.write("Student Not Found")

        except FileNotFoundError:
            return "File Not Found"
        except Exception as e:
            return f"Error: {e}"

    def classAverage(self) -> float:
        earned_pts = 0
        total_pts = 0
        for student in self.gradebook.values():
            for assignment in student.getScores():
                earned_pts += assignment.getScore()
                total_pts += assignment.getTotal()
        return (earned_pts / total_pts) * 100 if total_pts > 0 else 0

class CategoryGradebook(Gradebook):
    def __init__(self):
        super().__init__()
        self.categories = dict()

    def addCategory(self, description: str, weight: float):
        self.categories[description] = weight

    def isBalanced(self) -> bool:
        return sum(self.categories.values()) == 100

    def writeGradebookRecord(self, id: int, fileName: str):
        try:
            with open(fileName, 'w') as file:
                student = self.search(id)
                if student:
                    records = dict()

                    for assignment in student.getScores():
                        category = assignment.getCategory()
                        category_name = f"{category}: {assignment.getDescription()}"
                        fraction = f"{assignment.getScore()}/{assignment.getTotal()}"
                        file.write(f"{category_name}\n{fraction}\n")

                        percentage = assignment.getScore() / assignment.getTotal()
                        if category in records:
                            records[category].append(percentage)
                        else:
                            records[category] = [percentage]

                    for category, percentages in records.items():
                        avg_percentage = sum(percentages) / len(percentages) * 100
                        file.write(f"{category}: {avg_percentage:.2f}%\n")

                    total_percentage = 0
                    for category, percentage in records.items():
                        weight = self.categories.get(category, 0)
                        total_percentage += sum(percentage) / len(percentage) * (weight / 100)

                    file.write(f"Percentage: {total_percentage:.2f}%")
                else:
                    file.write("Student Not Found")

        except FileNotFoundError:
            return "File Not Found"
        except Exception as e:
            return f"Error: {e}"

    def classAverage(self) -> float:
        earned_pts = 0
        total_pts = 0
        for student in self.gradebook.values():
            for assignment in student.getScores():
                category = assignment.getCategory()
                weight = self.categories.get(category, 0)
                earned_pts += assignment.getScore() * (weight / 100)
                total_pts += assignment.getTotal() * (weight / 100)

        return (earned_pts / total_pts) * 100 if total_pts > 0 else 0
