from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
    first_date = datetime(year, month, day)
    second_date = datetime.today()
    difference = second_date - first_date
    difference_in_day = difference.days
    if difference_in_day > 0 :
        return True

    else:
        return False


def calculate_age(year, month, day):
    # write code here
    if check_birthdate(year, month, day):
        first_date = datetime(year, month, day)
        second_date = datetime.today()
        difference = second_date - first_date
        difference_in_day = difference.days

        age = difference_in_day // 365
        print("You are " +str(age)+ " years old.")
    else:
        print("The age is invalid ")

def main():
    # write main code here
    year = int(input("Enter year of birth: "))
    month =int(input("Enter month of birth: "))
    day = int(input("Enter day of birth: "))
    calculate_age(year, month, day)



if __name__ == '__main__':
	main()
