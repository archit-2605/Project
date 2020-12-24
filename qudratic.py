from tkinter import*

root = Tk()
root.title("Quadratic Equation Solver")


txta = StringVar()
d = 0
def adding():
  x1 = 0
  a = float(E1.get())
  b = float(E2.get())
  c = float(E3.get())
  d = (b**2-4*a*c)
  if d >= 0:
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    txta.set("roots are"+str(x1) + "and" + str(x2))
  else:
    txta.set("No real roots")
def max():
  a= float(E1.get())
  b =float(E2.get())
  c =float(E3.get())
  d = (b ** 2 - 4 * a * c)
  if a>0:
    m=(-d)/(4*a)
    txta.set("minima is"+str(m))
  if a<0:
    n=(-d)/(4*a)
    txta.set("maxima is"+str(n))
L1=Label(root,text="Enter the value of A,B and C of Ax^2+Bx+C=0", bg="red", fg="yellow")
L1.grid(row=0, column=0, columnspan=2)
LA=Label(root, text="A=", fg="blue")
LA.grid(row=1,column=0)
LB=Label(root, text="B=", fg="orange")
LB.grid(row=2,column=0)
LC=Label(root, text="C=", fg="green")
LC.grid(row=3,column=0)
E1=Entry(root)
E1.grid(row=1,column=1)
E2=Entry(root)
E2.grid(row=2,column=1)
E3=Entry(root)
E3.grid(row=3,column=1)
L4=Label(root, text="ANSWER=",fg="purple")
L4.grid(row=5,column=0)
E4=Entry(root, textvariable = txta)
E4.grid(row=5,column=1)


Button(root, text = "Find Roots",bg="yellow",fg="blue", command = lambda :adding()).grid(row=4,column=1)
Button(root, text= "Find Maxima or Minima",bg="grey",fg="pink", command = lambda : max()).grid(row=7,column=1)
mainloop()

