from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import requests
import ollama

OLLAMA_MODEL = "llama3.2"
messages = [
    {"role": "system", "content": "You are a helpful pirate assistant."}
]

def ask(user_text: str, direction: str = "You are a helpful assistant.") -> str:
    messages[0]["content"] = direction
    messages.append({"role": "user", "content": user_text})
    res = ollama.chat(model=OLLAMA_MODEL, messages=messages)
    reply = res["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

def on_submit_clicked():

    # build the prompt 
    text = conversation_entry.get("1.0", "end-1c")
    direction = direction_text.get("1.0", "end-1c")

    # get response from ollama
    reply = ask(text,direction)

    # post the reply
    conversation_log_entry.configure(state="normal")
    conversation_log_entry.insert(END, reply+"\n")
    conversation_log_entry.configure(state="disabled")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="NPC Chat").grid(column=0, row=0)
ttk.Label(frm, text="Direction").grid(column=0, row=1)
direction_text = ScrolledText(frm,height=10)
direction_text.insert("1.0", "You are a helpful pirate assistant.")
direction_text.grid(column=0, row=2)

ttk.Label(frm, text="Conversation log").grid(column=0, row=3)
conversation_log_entry = ScrolledText(frm, height=10, state="disabled" )
conversation_log_entry.grid(column=0, row=4)

ttk.Label(frm, text="Ask the NPC something.").grid(column=0, row=5)
conversation_entry = ScrolledText(frm, height=10)
conversation_entry.grid(column=0, row=6)
ttk.Button(frm, text="Submit", comman = on_submit_clicked).grid(column=0, row=7)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=8)
root.mainloop()
