import chromadb
import json
import ollama

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="courses")
client.heartbeat()

with open("courses.json", "r") as f:
    data = json.load(f)
    
for i, course in enumerate(data):
    collection.add(
        documents=[course["innhold"]],
        metadatas=[{
            "emnekode": course["emnekode"],
            "tittel": course["tittel"],
            "url": course["url"]
        }],
        ids=[str(i)]
    )
