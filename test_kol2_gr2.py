import unittest
from kol2_gr2 import Klasa,student,Szkola

class test_Szkola(unittest.TestCase):
	def setUp(self):
		self.Szkola=Szkola()
		self.Klasa1=Klasa()
		self.Klasa2=Klasa()
		self.s1=student([2., 3.],"adam","malysz",40)
		self.s2=student([4., 2.],"john","snow",70)
		self.s3=student([5. ,4.],"donald","trump",10)
		self.s4=student([5. ,5.],"ryszard","zklanu",20)
		self.Klasa1.add_student(self.s1)
		self.Klasa1.add_student(self.s2)
		self.Klasa2.add_student(self.s3)
		self.Klasa2.add_student(self.s4)
		self.Szkola.add_class(self.Klasa1)
		self.Szkola.add_class(self.Klasa2)
		self.scores=[2.,3.]
		self.name="adam"
		self.surname="malysz"
		self.attendance=70
		self.test_instance_student = student(self.scores, self.name, self.surname,self.attendance)
	
	def test_init_student(self):
		self.assertEqual(self.test_instance_student.name, self.name)
		self.assertEqual(self.test_instance_student.surname, self.surname)
		self.assertEqual(self.test_instance_student.scores, self.scores)
		self.assertEqual(self.test_instance_student.attendance, self.attendance)
	
		
	def test_get_totalaverage_in_school(self):
		self.assertAlmostEqual(3.75,self.Szkola.get_totalaverage(),places=4)
	
	def test_get_totalaverage_in_class(self):
		self.assertAlmostEqual(2.75,self.Szkola.get_totalaverageinclass(self.Klasa1),places=4)
	
	def test_get_attendance_in_school(self):
		self.assertEqual(35,self.Szkola.get_attendance())	

	
if __name__ == "__main__":
    unittest.main()			
		
#TEST OD GOLEBIKROL

