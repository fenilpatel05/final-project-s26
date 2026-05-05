from flask import Flask, request, redirect

app = Flask(__name__)

notes = []

@app.route("/")
def home():
    note_list = "".join(
        f"<li>{note} <a href='/delete/{i}'>Delete</a></li>"
        for i, note in enumerate(notes)
    )

    return f"""
    <h1>Simple Notes App</h1>

    <form action="/add" method="post">
        <input name="note" placeholder="Enter a note" required>
        <button type="submit">Add Note</button>
    </form>

    <ul>
        {note_list}
    </ul>
    """

@app.route("/add", methods=["POST"])
def add_note():
    note = request.form.get("note")
    if note:
        notes.append(note)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
