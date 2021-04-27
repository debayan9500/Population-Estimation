

#year = [1901, 1911, 1921, 1931, 1941, 1951, 1961, 1971] #1901 1911 1921 1931 1941 1951 1961 1971
#population = [60, 65, 68, 72, 79, 89, 97, 107] # 60 65 68 72 79 89 97 107
#AMM
def amm():

    year = yearinp.get().split()
    year = [int(x) for x in year]
    population = populationinp.get().split()
    population = [int(x) for x in population]
    x = int(xinp.get())
    increment = [0]
    year_increment = [0]
    percentage_increase = [0]
    for i in range(len(year) - 1):
        a = population[i + 1] - population[i]
        increment.append(a)
    for i in range(len(year) - 1):
        b = year[i + 1] - year[i]
        year_increment.append(b)
    for i in range(len(increment) - 1):
        c = increment[i + 1] * 100 / population[i]
        percentage_increase.append(c)
    avg_increase = sum(increment) / (len(increment) - 1)
    avg_per_increase = sum(percentage_increase) / (len(percentage_increase) - 1)
    n= (x - year[-1])/(sum(year_increment)/(len(year_increment)-1))
    pn = population[-1] + (n*avg_increase)
    print(pn)
    explanation = pn
    w2 = Label(master,

               bg='white',
               width="25",
               padx=10,
               text=explanation).place(x = 170, y = 240)



#GPM/GMM
def gmm():
    year = yearinp.get().split()
    year = [int(x) for x in year]
    population = populationinp.get().split()
    population = [int(x) for x in population]
    x = int(xinp.get())
    increment = [0]
    year_increment = [0]
    percentage_increase = [0]
    for i in range(len(year) - 1):
        a = population[i + 1] - population[i]
        increment.append(a)
    for i in range(len(year) - 1):
        b = year[i + 1] - year[i]
        year_increment.append(b)
    for i in range(len(increment) - 1):
        c = increment[i + 1] * 100 / population[i]
        percentage_increase.append(c)
    avg_increase = sum(increment) / (len(increment) - 1)
    avg_per_increase = sum(percentage_increase) / (len(percentage_increase) - 1)
    n= (x - year[-1])/(sum(year_increment)/(len(year_increment)-1))
    pn = population[-1]*(1+(avg_per_increase/100))**n
    print(pn)
    explanation = pn
    w2 = Label(master,
               bg='white',
               width="25",
               padx=10,
               text=explanation).place(x = 170, y = 240)

#______________________________________________________________________________________
from tkinter import *
def show_values():
    a = yearinp.get().split()
    a= [int(x) for x in a]
    print(a)

master = Tk()

mb =  Menubutton ( master, text="About" )
mb.place()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
mb.menu.add_command ( label="©Debayan Ghosh" )
mb.place(x=0, y=0)

mb = Label ( master, text="*Arithmetic Mean Method" )
mb.place(x=500, y=200)
mb = Label ( master, text="*Geometric Mean Method" )
mb.place(x=500, y=220)

master.geometry("755x393")
master.wm_iconbitmap('population.ico')
master.title("Population Estimation")
t1 = Label(master, text  ="Enter the values of year with sapces").place(x = 10, y = 50)
yearinp = StringVar()
yspsp = Entry(master, textvariable = yearinp,width="75" )
yspsp.place(x = 240, y = 50)
t2 = Label(master, text  ="Enter the values of population eith sapces").place(x = 10, y = 90)
populationinp = StringVar()
pspsp = Entry(master, textvariable = populationinp,width="75")
pspsp.place(x = 240, y = 90)
t1 = Label(master, text  ="Enter the value of year ").place(x = 95, y = 130)
xinp = IntVar()
spsp = Entry(master, textvariable = xinp)
spsp.place(x = 240, y = 130)

pn  ="Result "

Button( text='amm', command=amm).place(x = 240, y = 190)
Button( text='gmm', command=gmm).place(x = 300, y = 190)

explanation = pn
w2 = Label(master,
           bg = 'white',
           width = "25",
           fg = "#696969",
           padx=10,
           text=explanation).place(x = 170, y = 240)

master.mainloop()
#print(amm(1994))
