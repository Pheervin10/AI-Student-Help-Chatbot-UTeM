def chatbot_response(user_input):
    faq = {
        "course registration": "Course registration is done through the UTeM student portal.",
        "exam schedule": "Exam schedules are published on the faculty notice board and portal.",
        "academic calendar": "The academic calendar is available on the UTeM official website.",
        "assignment submission": "Assignments are submitted through the LMS platform."
    }

    user_input = user_input.lower()

    for key in faq:
        if key in user_input:
            return faq[key]

    return "Sorry, I could not find an answer to your question. Please contact the faculty office."

if __name__ == "__main__":
    while True:
        query = input("Ask a question (type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        print(chatbot_response(query))
