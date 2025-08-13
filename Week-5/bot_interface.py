from main_chain import main_chain

print("Hey, you can ask me anything about the UGAC Rulebook!!:)")
while True:
    query = input()
    resp = main_chain.invoke(query)
    print(f'Bot: {resp}')
    print('Anything Else?')