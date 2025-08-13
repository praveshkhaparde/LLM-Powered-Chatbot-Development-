import ollama

client = ollama.Client()

model = "mario" ## "gemma3"
prompt = "What is tqdm?"

response = client.generate(model = model, prompt = prompt)

print("Response from Ollama")
print(response.response)