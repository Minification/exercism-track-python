from typing import List
from collections import defaultdict
from bisect import insort_left

class School:
    def __init__(self) -> None:
    	# No need to initialize new keys
        self.grades = defaultdict(list)

    def add_student(self, name: str, grade: int) -> None:
    	# Insert, keeping the list sorted
        insort_left(self.grades[grade], name)

    def roster(self) -> List[str]:
        return [
        	name
        	for grade in sorted([*self.grades])
        	for name in self.grades[grade]
        ]

    def grade(self, grade_number: int) -> List[str]:
    	# Fresh copy. List is sorted due to bisect.insort_left()
        return self.grades[grade_number].copy()
