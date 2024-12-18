import random

def generate_exam_tickets(input_file, output_file, questions_per_ticket, num_tickets):
    # Read questions from the input file
    try:
        with open(input_file, 'r', encoding="utf-8") as file:
            questions = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    # Check if there are enough questions
    if len(questions) < questions_per_ticket:
        print("Error: Not enough questions in the input file to create a ticket.")
        return

    # Generate tickets
    tickets = []
    for _ in range(num_tickets):
        ticket = random.sample(questions, questions_per_ticket)
        tickets.append(ticket)

    # Write tickets to the output file
    with open(output_file, 'w', encoding="utf-8") as file:
        for i, ticket in enumerate(tickets, 1):
            file.write(f"Ticket {i}\n")
            file.write("".join(ticket))
            file.write("\n")

    print(f"{num_tickets} tickets have been generated and saved to '{output_file}'.")

# Configuration
input_file = 'questions.txt'  # Input file containing the questions
output_file = 'exam_tickets.txt'  # Output file for the generated tickets
questions_per_ticket = 5  # Number of questions per ticket
num_tickets = 30  # Number of tickets to generate

# Generate exam tickets
generate_exam_tickets(input_file, output_file, questions_per_ticket, num_tickets)
