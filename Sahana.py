import google.generativeai as genai
genai.configure(api_key="AIzaSyCUgragjDxpjobcMxYO9GFdVFzvTPqsY18")
model = genai.GenerativeModel("gemini-1.5-flash")
system_prompt = "Translate the sentences to the specified language"
def chat_with_bot(user_input):
    prompt = system_prompt + user_input
    response = model.generate_content(prompt)
    return response.text
if __name__ == "__main__":
    print("Heyyy!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Get lost and Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"Bot: {response}")
