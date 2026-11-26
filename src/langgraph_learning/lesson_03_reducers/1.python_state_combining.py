# target => "logs" => ["Started", "Text normalisazion"] after update
# ------------------------------------------------------------------
state = {
    "text": "Hello",
    "logs": ["Started"]
}

update = {
    "logs": ["Text normalized"]
}

# It replace logs instead of combining
state.update(update)

print(state) # {'text': 'Hello', 'logs': ['Text normalized']}
print("-----------------------------------------------------")
# ----------------------------------------------------------

state = {
    "text": "Hello",
    "logs": ["Started"]
}

update = {
    "logs": ["Text normalized"]
}

state["logs"] = state["logs"] + update["logs"]

print(state) # {'text': 'Hello', 'logs': ['Started', 'Text normalized']}