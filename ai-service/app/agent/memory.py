conversation_memory = {}

def save(store_id, question, answer):
    conversation_memory.setdefault(store_id, []).append({
        "q": question,
        "a": answer
    })
