x = 5 
done = False



while done == False:
    a = 2 * x**2
    b = 5 * x
    c = -10
    f = a + b + c
    #print(f)

    am = 2 * 2 * x ** (2-1)
    bm = 5
    fm = am + bm
    #print(fm)
   
    Nx = x - (f/fm)
    #print(x)
    #print(Nx)
    if round(Nx, 3) == round(x, 3):
        done = True
        print("x1 = " + str(round(Nx, 3)))

    x = Nx

x = -5
done = False

while done == False:
    a = 2 * x**2
    b = 5 * x
    c = -10
    f = a + b + c
    #print(f)

    am = 2 * 2 * x ** (2-1)
    bm = 5
    fm = am + bm
    #print(fm)
   
    Nx = x - (f/fm)
    #print(x)
    #print(Nx)
    if round(Nx, 3) == round(x, 3):
        done = True
        print("x2 = " + str(round(Nx, 3)))

    x = Nx


 

