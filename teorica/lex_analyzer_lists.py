import re
import json

ex = "[John, 10, 20, Jane, 30, 40, ??]"

with open ("tokens_list.json", "r") as f:
    tokens_dict = json.load(f)

regexs = []

for key, value in tockens_dict.items():
    regexs.append((f"?P<{key}>{value}"))

regex = "|".join(regexs) + "|(?P<ERROR>.)"
tokens = re.finditer(regex, ex)

for tok in tokens:
    d = tok.groupdict()
    for key in d:
        if d[key]:
            if key != "IGNORE":
                print(key, d[key], tok.span())
    