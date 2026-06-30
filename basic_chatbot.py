from datetime import datetime

print("=" * 45)
print("        Welcome to CodeAlpha Chatbot")
print("=" * 45)
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Hope you're having a wonderful day.")

    elif "what is your name" in user or "may i know your name" in user:
        print("Bot: My name is CodeBot.")

    elif "who made you" in user or "who created you" in user:
        print("Bot: I was created as a Python project for the CodeAlpha Internship.")

    elif "what is python" in user or "tell me about python" in user:
        print("Bot: Python is an easy, powerful, and beginner-friendly programming language.")

    elif "what time is it" in user or "can you tell me the time" in user or "what is the current time" in user:
        print("Bot: Current time is", datetime.now().strftime("%I:%M %p"))

    elif "what is today's date" in user or "tell me today's date" in user or "what is the date today" in user:
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif "what day is today" in user or "which day is today" in user:
        print("Bot: Today is", datetime.now().strftime("%A"))

    elif "good morning" in user:
        print("Bot: Good Morning! Have a productive day!")

    elif "good afternoon" in user:
        print("Bot: Good Afternoon! Hope you're doing well!")

    elif "good evening" in user:
        print("Bot: Good Evening!")

    elif "good night" in user:
        print("Bot: Good Night! Sweet dreams.")

    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    elif "tell me a joke" in user or "can you tell me a joke" in user:
        print("Bot: Why do programmers prefer Python? Because it's easy to 'byte' into!")

    elif "how old are you" in user or "what is your age" in user:
        print("Bot: I'm just a computer program, so I don't have an age.")

    elif "what is your favorite color" in user:
        print("Bot: I like blue because it reminds me of Python!")

    elif "what is your favorite food" in user:
        print("Bot: I don't eat, but pizza smells amazing!")

    elif "how is the weather today" in user or "what is the weather today" in user:
        print("Bot: Sorry, I can't check live weather without internet.")

    elif "where are you from" in user:
        print("Bot: I live inside your Python program!")

    elif "can you help me" in user or "what can you help me with" in user:
        print("Bot: You can ask me about time, date, Python, jokes, greetings, and more.")

    elif "which programming language should i learn" in user or "tell me about python course" in user:
        print("Bot: Python is one of the best programming languages to start with.")

    elif "what is codealpha internship" in user or "tell me about codealpha internship" in user:
        print("Bot: CodeAlpha internships help students build practical programming skills.")

    elif "what is your hobby" in user:
        print("Bot: My hobby is answering your questions!")

    elif "do you love me" in user or "i love you" in user:
        print("Bot: That's kind of you!")

    elif "what can you do" in user:
        print("Bot: I can answer simple questions, tell the time and date, and chat with you.")

    else:
        print("Bot: Sorry, I don't understand that. Please ask another question.")