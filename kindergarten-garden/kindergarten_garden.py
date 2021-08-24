from typing import List, Union, Tuple

PLANTS = {
	plant[0]: plant for plant in ["Violets", "Clover", "Radishes", "Grass"]
}

STUDENTS = ("Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", 
			"Ileana", "Joseph", "Kincaid", "Larry")

class Garden:
	def __init__(self, diagram: str, students: Union[List[str], Tuple[str, ...]]=STUDENTS) -> None:
		self.students = tuple(sorted(students))
		self.student_plants = {
			student: [
				PLANTS[plant] 
				for plant_row in diagram.split()
				for plant in plant_row[student_index * 2 : (student_index + 1) * 2]
			] 
			for student_index, student in enumerate(self.students)
		}
	
	def plants(self, name: str) -> List[str]:
		return self.student_plants[name]
