from datetime import date

def calculate_age(day_of_birth: int, month_of_birth: int, year_of_birth: int):
    today = date.today()
    birth_date = date(year_of_birth, month_of_birth, day_of_birth)
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        months -= 1
        days += (birth_date.replace(month=birth_date.month % 12 + 1, day=1) - birth_date.replace(day=1)).days
    
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

def main():
    day_of_birth = int(input("Enter day of birth (1-31): "))
    month_of_birth = int(input("Enter month of birth (1-12): "))
    year_of_birth = int(input("Enter year of birth: "))
    
    years, months, days = calculate_age(day_of_birth, month_of_birth, year_of_birth)
    print(f"Age: {years} years, {months} months, {days} days")

main()
