class Leapx_org():
	mul_num = 1.20
	count= 0
	def __init__(self,first,last,pay):
		self.f_name = first
		self.l_name = last
		self.pay_amt = pay 
		self.full_name = first+" "+last
		Leapx_org.count = Leapx_org.count+1
				
	def make_email(self):
		return self.f_name+ "."+self.l_name+"@xyz.com"
		
	def incrementpay(self):
		self.pay_amt = int(self.pay_amt*self.mul_num)
		return self.pay_amt
	
class instructor(Leapx_org):
	pass
	
I_obj1 = instructor('mohit', 'RAJ', 60000)
I_obj2 = instructor('Ravender', 'Dahiya',70000) 

print "number of employees ", instructor.count

print I_obj1.make_email()
print I_obj2.make_email()

print (help(instructor))
