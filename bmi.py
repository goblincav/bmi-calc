while True:
    print ("What is your height (e.g.  6'7)")
    height = input()
    height = height.split("'")
    height_inches = int(height[0])*12+int(height[1])
    print  ("what is your weight in pounds?")
    weight = abs(float(input()))
    
    bmi= round(weight/(height_inches**2)*703,1)
    #
    und = 18.5

    nor = 24.9

    over = 29.9

    obe = 39.9

    mor = 1000000
    #
    print(bmi)
    if bmi <= und:
        print("You are certified underweight™ by the NIH!")
    elif und < bmi <= nor:
        print("You are certified normal weight™ by the NIH!")
    elif nor < bmi <= over:
        print("You are certified overweight™ by the NIH!")
    elif over < bmi <= obe:
        print("You are certified obese™ by the NIH!")
    elif obe < bmi <= mor:
        print("You are certified morbidly obese™ by the NIH!")
 
##     
##inp = input("""enter your height: (e.g.  6'7) """)
##height_list = inp.split("'")
##print(height_list[0]*3)
##print(height_list[1])


