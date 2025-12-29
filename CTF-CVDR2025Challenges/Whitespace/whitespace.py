stl = """
S S S T	S S S S T	T	L
T	L
S S S S S T	S T	S T	T	S L
T	L
S S S S S T	S S S T	S S L
T	L
S S S S S T	S T	S S T	S L
T	L
S S S S S T	T	T	T	S T	T	L
T	L
S S S S S T	T	T	S T	S S L
T	L
S S S S S T	T	S T	S S S L
T	L
S S S S S T	T	S T	S S T	L
T	L
S S S S S T	T	T	S S T	T	L
T	L
S S S S S T	S T	T	T	T	T	L
T	L
S S S S S T	T	S T	S S T	L
T	L
S S S S S T	T	T	S S T	T	L
T	L
S S S S S T	S T	T	T	T	T	L
T	L
S S S S S T	T	S T	S S S L
T	L
S S S S S T	T	S S S S T	L
T	L
S S S S S T	T	T	S S T	S L
T	L
S S S S S T	T	S S T	S S L
T	L
S S S S S T	T	T	T	T	S T	L
T	L
S S L
L
L

"""

emojis = [
    "UwU", "uwu", "uwu", "OwO", "(◡w◡)", "(UᵕU❁)", "(ᴜωᴜ)",
    "(ᵘʷᵘ)", "uwu"
]

emoji_index = 0
out = ""

for token in stl.split():
    # place emoji
    out += emojis[emoji_index % len(emojis)]
    emoji_index += 1

    # place whitespace AFTER emoji
    if token == "S":
        out += " "
    elif token == "T":
        out += "\t"
    elif token == "L":
        out += "\n"

with open("emoji_whitespace.txt", "w", encoding="utf-8") as f:
    f.write(out)

print("Done. Emojis separated by encoded whitespace.")
