

def calculate_salary():
    count = 0
    increment_per_promotion = 0.3
    
    initial_sal = int(input("Enter the initial salary :"))
    final_sal = initial_sal
    joining_year = int(input("enter the joining year: "))
    current_year = int(input("enter the current year: "))
    increment_per_year = 0.1
    difference = current_year - joining_year
    for i in range(0, difference):
        count += 1
        # if i % 3 == 0 :
        #     initial_sal += initial_sal*increment_per_promotion
        if count % 3 == 0:
            initial_sal += initial_sal*increment_per_promotion
            count = 0
        else :
            initial_sal += initial_sal*increment_per_year
        final_sal += initial_sal
        round_final= round(final_sal,2)
        round_total= round(initial_sal,2)
    print("the final salary in year {} is {} INR. And the total amount of money earned until now is {}" .format(current_year, round_total, round_final))
calculate_salary()