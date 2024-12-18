import random

def generate_exam_tickets(input_file, output_file, num_tickets):
    # Read questions from the input file
    try:
        with open(input_file, 'r', encoding="utf-8") as file:
            questions = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    # Separate questions into categories based on prefixes
    easy_questions = [q.replace("Asan:", "").strip() for q in questions if q.lower().startswith("asan")]
    medium_questions = [q.replace("Orta:", "").strip() for q in questions if q.lower().startswith("orta")]
    hard_questions = [q.replace("Çətin:", "").strip() for q in questions if q.lower().startswith("çətin")]

    # Ensure there are enough questions in each category
    if len(easy_questions) < 3 or len(medium_questions) < 3 or len(hard_questions) < 1:
        print("Error: Not enough questions in one or more categories.")
        return

    # Generate tickets
    tickets = []
    for _ in range(num_tickets):
        selected_easy = random.sample(easy_questions, 3)
        selected_medium = random.sample(medium_questions, 3)
        selected_hard = random.sample(hard_questions, 1)
        ticket = selected_easy + selected_medium + selected_hard
        random.shuffle(ticket)  # Shuffle the questions
        tickets.append(ticket)

    # Write tickets to the output file
    with open(output_file, 'w', encoding="utf-8") as file:
        for i, ticket in enumerate(tickets, 1):
            file.write(f"Ticket {i}\n")
            for question in ticket:
                file.write(f"{question}\n")
            file.write("\n")

    print(f"{num_tickets} tickets have been generated and saved to '{output_file}'.")

# Configuration
input_file = 'questions.txt'  # Input file containing the questions
output_file = 'exam_tickets.txt'  # Output file for the generated tickets
num_tickets = 15  # Number of tickets to generate

# Generate exam tickets
generate_exam_tickets(input_file, output_file, num_tickets)
