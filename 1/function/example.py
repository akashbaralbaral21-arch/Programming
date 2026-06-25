def bank_transfer(sender, receiver, amount):
    print(f"Transferring {amount} from {sender} to {receiver}")
bank_transfer("ram", "sita", 500)

def book_fight(from_city, to_city):
    print(f"Booking a flight from {from_city} to {to_city}")
book_fight(to_city="Nepalgunj", from_city="Kathmandu")


def area(l,b):
    a=l*b
    print(a)
area(10,20)

if __name__=="__main__":
    area(10,20)
    print("Hello")
    print("python")
    
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score, score must be between 0 and 100"
    if score>=90:
        return "A+"
    if score >= 80:
        return "A"
    if score >=70:
        return "B"
    if score >=60:
        return "C"
    if score>=50:
        return "D"
    else:
        return "F"
    
print(calculate_grade(95))
print(calculate_grade(75))
print(calculate_grade(45))
print(calculate_grade(105))
    
