# Marta Konarska

 # 04/26/2024

  # P4HW1

  # Edit and enhance exiting programs

def main():

  score_list = []
  num_scores = int(input("How many scores do you want to enter? "))


  total_score = 0
  lowest_score = 100


  for _ in range(num_scores):
   
    score = get_valid_score("Enter score: ")
    if 0 <= score <= 100:
        score_list.append(score)
        total_score += score
        if score < lowest_score:
          lowest_score = score
    
    else:
      print("INVALID Score entered! ! ! ! ! Score should be between 0 and 100.")

  if num_scores > 0:
    average_score = total_score / num_scores
  else:
    average_score = 0

  
  score_list.remove(lowest_score)


  letter_grade = None
  if average_score >= 90:
    letter_grade = "A"
  elif 80 <= average_score < 90:
    letter_grade = "B"
  elif 70 <= average_score < 80:
    letter_grade = "C"
  elif 60 <= average_score < 70:
    letter_grade = "D"
  else:
    letter_grade = "F"

 
  print(f"Lowest Score: {lowest_score}")
  print(f"Modified List: {score_list}")
  print(f"Scores Average: {average_score:.2f}")  # Format average with 2 decimal places
  if letter_grade is not None:
    print(f"Grade: {letter_grade}")
  else:
    print("No scores entered.")


def get_valid_score(prompt):
  """Gets a valid score (between 0 and 100) from the user.

  Args:
      prompt: The message to display to the user before input.

  Returns:
      The valid score entered by the user (integer between 0 and 100).
  """

  while True:
    try:
      score = int(input(prompt))
      if 0 <= score <= 100:
        return score
      else:
        print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
      print("Invalid input. Please enter a number.")


if __name__ == "__main__":
  main()
