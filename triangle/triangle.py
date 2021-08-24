from typing import List
import itertools

def is_triangle(sides: List[float]) -> bool:
	all_nonzero = len([0 for side in sides if side <= 0]) == 0
	triangle_inequality = sum(sides[0:2]) >= sides[2] and sum(sides[1:3]) >= sides[0] and sides[0] + sides[2] >= sides[1]
	return all_nonzero and triangle_inequality

def equilateral(sides: List[float]) -> bool:
	return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: List[float]) -> bool:
	return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: List[float]) -> bool:
	return is_triangle(sides) and len(set(sides)) == 3
