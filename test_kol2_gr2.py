import unittest
from kol2_gr2 import Klasa,student,Szkola

class test_Szkola(unittest.TestCase):
	def setUp(self):
		self.Szkola=Szkola()
		self.Klasa1=Klasa()
		self.s1=student([2., 3.],"adam","malysz",40)
		self.s2=student([4., 2.],"john","snow",70)
		self.s3=student([5. ,4.],"donald","trump",10)
		self.s4=student([5. ,5.],"ryszard","zklanu",20)
		self.Klasa1.add_student(s1)
		self.Klasa1.add_student(s2)
		self.Klasa2.add_student(s3)
		self.Klasa2.add_student(s4)
		self.Szkola.add_class(k1)
		self.Szkola.add_class(k2)
		
	def test_get_totalaverage_in_school(self):
		self.assertAlmostEqual(3.75,self.Szkola.get_totalaverage(),places=4)
	
	def test_get_totalaverage_in_class(self, Klasa1):
		self.assertAlmostEqual(2.75,self.Szkola.get_totalaverageinclass(),places=4)
	
	def test_get_attendance_in_school(self):
		self.asserEqual(53,self.Szkola.get_attendance())	
			
		
#TEST OD GOLEBIKROL
###POPRAWA###
"""MINIMUM 12-14 testow"""
