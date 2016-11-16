import unittest
from kol2_gr2 import Klasa,student,Szkola

class test_Szkola(unittest.TestCase):
	def setUp(self):
		self.Klasa=Szkola()
		self.student=student()
		self.Szkola=Szkola()
		s1=student([2., 3., 3. ,4.],"adam","malysz",40)
		s2=student([5., 2., 5., 4.],"john","snow",70)
		s3=student([5. ,4. ,3. ,4.],"donald","trump",10)
		s4=student([5. ,5. ,3., 4.],"ryszard","zklanu",20)
		s5=student([2., 2., 3., 6.],"donald","tusk",100)
		k1=Klasa()
		k1.add_student(s1)
		k1.add_student(s2)
		k1.add_student(s3)
		k2=Klasa()
		k2.add_student(s4)
		k2.add_student(s5)
		k2.add_student(s6)

		S=Szkola()
		S.add_class(k1)
		S.add_class(k2)
		
	def test_get_totalaverage(self):
		self.assertEqual()
		
		
