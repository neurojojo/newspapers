import json

with open("List_local_newspapers","r") as f:
    text = f.read()

state_newspapers = {}
state_name = ""

for c,line in enumerate(text.split("\n")):
    line = line.strip()
    if line:
        if ":" in line and "http" not in line:
            state_name = line.split(":")[0]
            state_newspapers[state_name] = []
        if "http" in line:
            name, url = line.split(": ")
            state_newspapers[state_name].append({
                "newspaper": name.strip(),
                "url": url.strip(),
                "request": []
            })

with open("newspapers.json", "w") as f:
    json.dump(state_newspapers, f, indent=2)

print("JSON file created successfully!")