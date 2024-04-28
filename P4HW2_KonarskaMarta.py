 # Marta

 # 04/26/2024

  #P4HW2

  #Calculate gross pay for multiple employees

def main():
  """Calculates gross pay for multiple employees with overtime and displays totals."""

 
  total_overtime_pay = 0
  total_regular_pay = 0
  num_employees = 0

  
  while True:
    
    employee_name = input("Enter employee name (or 'Done' to terminate): ")

    
    if employee_name.lower() == "Done":
      break

    
    pay_rate, hours_worked = get_valid_employee_data(employee_name)

    
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)

   
    

   
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    num_employees += 1

  
    print(f"\nEmployee Summary for {employee_name}:")
    print(f"  Pay Rate: ${pay_rate:.2f}")
    print(f"  Overtime Pay: ${overtime_pay:.2f}")
    print(f"  Regular Pay: ${regular_pay:.2f}")
    

  
  print("Overall Employee Pay Summary:")
  print(f"  Total Employees Processed: {num_employees}")
  print(f"  Total Regular Pay: ${total_regular_pay:.2f}")
  print(f"  Total Overtime Pay: ${total_overtime_pay:.2f}")
  


def get_valid_employee_data(employee_name):
  """Prompts for and validates employee pay rate and hours worked.

  Args:
      employee_name: The name of the employee.

  Returns:
      A tuple containing the validated pay rate and hours worked.
  """

  while True:
    try:
      pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
      if pay_rate <= 0:
        raise ValueError("Pay rate must be positive.")
      hours_worked = float(input(f"How many hours did {employee_name} work? "))
      if hours_worked < 0:
        raise ValueError("Hours worked cannot be negative.")
      return pay_rate, hours_worked
    except ValueError as e:
      print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
  main()
