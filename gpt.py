import openai
from key import key

q = input("Recommend based on this movie: ")
# q = input("ask a question")

openai.api_key = key


def generate_prompt(movie) -> str:
    return f"Recommend me a movie that is similar to this one {movie}"


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=generate_prompt(q),
    temperature=1,
    max_tokens=150,
)

print(response["choices"][0]["text"])
