

def calculate(**kwargs):
	operation={
	"add":lambda x,y:x+y,
	"subtract":lambda x,y:x-y,
	"multiply":lambda x,y:x*y,
	"divide":lambda x,y:x/y,
	}
	message=kwargs.get("message","The result is")
	first=kwargs.get("first",0)
	second=kwargs.get("second",0) 
	opr=operation.get(kwargs.get("operation",""))

	if kwargs.get("make_float",False):
		result=float(opr(first,second))
	else:
		result=opr(first,second)
	
	return message + " " + str(result)

if __name__ == '__main__':
	print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
	print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"