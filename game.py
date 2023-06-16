import openai

# Set up your OpenAI API credentials
openai.api_key = 'OPENAPI_KEY'

# Function to generate AI response using LLAMA
def generate_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.6,
        top_p=1.0,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Function to validate word input
def validate_word(word, last_word):
    if last_word == "":
        return True
    elif word.lower() == last_word[-1].lower():
        return True
    return False

# Game logic
def play_game():
    print("Welcome to Word Chain Chat!")
    print("The game begins with a randomly chosen starting word.")
    print("You and the AI will take turns forming a word chain.")
    print("Each word you suggest must start with the last letter of the previous word.")
    print("Let's start!")

    last_word = ""  # Store the last word used in the chain

    while True:
        # Player's turn
        if last_word == "":
            word = input("Enter a starting word: ")
        else:
            word = input("Your word (starting with '{}'): ".format(last_word[-1]))

        if not validate_word(word, last_word):
            print("Invalid word! Please try again.")
            continue

        last_word = word

        # AI's turn
        message = "Player: {}\nAI:".format(last_word)
        ai_response = generate_response(message)
        print("AI:", ai_response)

        # Check if AI cannot think of a word or repeats a word
        if ai_response.startswith("I'm sorry") or not validate_word(ai_response, last_word):
            print("AI cannot continue the chain. You win!")
            break

play_game()
