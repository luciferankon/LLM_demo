import openai
import os

# Set your OpenAI API key
openai.api_key = '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'

# Function to read content from text files in a directory
def read_text_files(directory):
    files_content = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                files_content[filename] = file.read()
    return files_content

# Function to ask questions using OpenAI API
def ask_questions(content, question):
    prompt = f"Content: {content}\nQuestion: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    generated_answer = response.choices[0].text.strip()
    return generated_answer

# Main function
def main():
    # Directory containing text files
    text_files_directory = '/Users/luciferankon/projects/sample_LLM_demo'

    # Read content from text files
    files_content = read_text_files(text_files_directory)

    # Interactive loop to ask questions
    while True:
        # Ask user for a question
        question = input("Ask a question (type 'exit' to quit): ")

        if question.lower() == 'exit':
            break

        # Provide answers based on the content of text files
        for filename, content in files_content.items():
            answer = ask_questions(content, question)
            print(f"Question: {question}\nFile: {filename}\nAnswer: {answer}\n")

if __name__ == "__main__":
    main()
