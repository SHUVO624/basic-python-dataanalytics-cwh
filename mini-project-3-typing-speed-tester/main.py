import time     # time module is used to measure the time taken by the user to type the text.
import random   # random module is used to select a random text from the list of texts.

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "A quick move by the enemy will jeopardize six fine gun boats.",
    "All the faith he had had had had no effect on the outcome of his life.",
    "John Prady, give me a black walnut box of quite small size."
    ]   # List of sentences for the typing test.

def measure_accuracy (user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)   # Count the number of correct characters typed by the user and zip is used to iterate over both the user input and the test sentence simultaneously.
    accuracy = (correct_chars / len(test_sentence)) * 100 if len(test_sentence) > 0 else 0   # Calculate the accuracy percentage.
    return accuracy #  Return the accuracy percentage.



def typing_test():
    test_sentence = random.choice(sentences)   # Select a random sentence from the list.
    print("Type the following sentence as fast as you can:")
    print(test_sentence)   # Display the selected sentence to the user.
    input("Press Enter when you are ready to start...")   # Wait for the user to press Enter to start the test.
    start_time = time.time()   # Record the start time.
    user_input = input("\nStart typing here: \n")   # Get the user's input.
    end_time = time.time()   # Record the end time.
    time_taken = end_time - start_time   # Calculate the time taken by the user.
    time_taken_in_seconds = round(time_taken, 2)   # Round the time taken to 2 decimal places.
    word_count = len(user_input.split())   # Count the number of words typed by the user.

    print("results:")   # Display the results of the typing test.
    print(f"Time taken: {time_taken_in_seconds} seconds")   # Display the time taken by the user.
    print(f"Words typed: {word_count}")   # Display the number of words typed by the user.
    print(f"Typing speed: {word_count / time_taken_in_seconds * 60:.2f} WPM" if time_taken_in_seconds > 0 else "Typing speed: 0 WPM")   # Display the typing speed in WPM.
    
    accuracy = measure_accuracy(user_input, test_sentence)   # Measure the accuracy of the user's typing.
    print(f"Accuracy: {accuracy:.2f}%")   # Display the accuracy percentage


typing_test()