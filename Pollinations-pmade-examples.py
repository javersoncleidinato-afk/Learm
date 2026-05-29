# Non-streaming (simple)
answer = p.gen_text("Explain Python list comprehensions", model="openai-fast")
print(answer)

# Streaming (fancy)
for chunk in p.gen_text("Write a poem", stream=True):
    print(chunk, end="", flush=True)