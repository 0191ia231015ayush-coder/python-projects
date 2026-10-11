"""AI Study Buddy - Rule-Based Chat Assistant (console, no external AI models)."""

from datetime import datetime

# Keyword -> response dictionary
RESPONSES = {
    "python": "Python is a great first language! Practice daily: variables, loops, functions, then OOP.",
    "oop": "OOP has 4 pillars: Encapsulation, Abstraction, Inheritance, Polymorphism.",
    "dsa": "Start with arrays, strings, linked lists, stacks, queues, then trees and graphs.",
    "array": "Arrays store elements in contiguous memory. Access is O(1), search is O(n).",
    "sorting": "Learn bubble, selection, insertion, merge and quick sort. Merge sort is O(n log n).",
    "recursion": "Recursion = a function calling itself with a base case to stop. Try factorial first!",
    "study": "Try the Pomodoro method: 25 minutes focus, 5 minutes break.",
    "exam": "Make a timetable, revise key topics, and solve previous year papers.",
    "motivate": "Small progress every day beats big effort once in a while. Keep going!",
    "html": "HTML is the structure of a web page, while CSS styles it.",
    "css": "CSS controls colors, layout and fonts of a web page.",
    "help": "Ask me about: python, oop, dsa, array, sorting, recursion, study, exam, html, css.",
}

EXIT_WORDS = ("bye", "exit", "quit")


def get_greeting():
    """Return a greeting based on the current time."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    if hour < 17:
        return "Good afternoon"
    return "Good evening"


def get_response(user_input):
    """Find a keyword in the user's message and return the matching reply."""
    text = user_input.lower()
    for keyword, reply in RESPONSES.items():
        if keyword in text:
            return reply
    return "Sorry, I don't know that yet. Type 'help' to see what I can answer."


def main():
    print(f"{get_greeting()}! I'm AI Study Buddy.")
    print("Ask me a study question. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in EXIT_WORDS:
            print("Study Buddy: Goodbye! Keep learning.")
            break
        print("Study Buddy:", get_response(user_input))


if __name__ == "__main__":
    main()
