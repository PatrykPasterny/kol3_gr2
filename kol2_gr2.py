
class student(object):
	def __init__(self,scores,surname,name,attendance):
		self.name=name
		self.surname=surname
		self.attendance=attendance
		self.scores=scores

class Klasa(object):
	def __init__(self):
		self.students=[]
	
	def add_student(self,student):
		self.students.append(student)


class Szkola(object):
	def __init__(self):
		self.classes=[]
	def add_class(self,Klasa):
		self.classes.append(Klasa)		
		
	def get_totalaverage(self):
		suma=0
		n=0
		for i in self.classes:
			for j in i.students:
				suma+=sum(j.scores)	
				n+=len(j.scores)
		return suma/n

	def get_totalaverageinclass(self,klasa):
		suma=0
		n=0
		for j in klasa.students:
			
			suma+=sum(j.scores)
			n+=len(j.scores)
		return suma/n

	def get_attendance(self):
		at=0
		n=0
		for i in self.classes:
			for j in i.students:
				at+=j.attendance	
				n+=1
		return at/n
 


def main():

	s1=student([2., 3., 3. ,4.],"adam","malysz",40)
	s2=student([5., 2., 5., 4.],"john","snow",70)
	s3=student([5. ,4. ,3. ,4.],"donald","trump",10)
	s4=student([5. ,5. ,3., 4.],"ryszard","zklanu",20)
	s5=student([1. ,2. ,4. ,4.],"hillary","clinton",80)
	s6=student([2., 2., 3., 6.],"donald","tusk",100)

	

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
	
	
	

	print S.get_totalaverage()
	print S.get_totalaverageinclass(k1)
	print S.get_totalaverageinclass(k2)
	print str(S.get_attendance())+"%" # in %


if __name__ == "__main__":
	main()
