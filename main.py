
#### main.py

```python
#!/usr/bin/env python3
import random

dynasties = [
    "The Obsidian Lords – An empire of scholars and mystics, erased by an unknown force.",
    "The Azure Pact – A kingdom built on trade and diplomacy, shattered by betrayal.",
    "The Ivory Court – Ruled by an eternal queen, her fate unknown after the final war.",
    "The Moonveil Dynasty – A civilization of astronomers, lost when the stars vanished from their sky.",
    "The Emberborn Kings – Fire-wielding monarchs who burned their own empire to prevent invasion."
]

def get_random_dynasty():
    return random.choice(dynasties)

def main():
    print("Welcome to Forgotten Dynasties!")
    print("Here is a randomly generated lost dynasty and its fate:")
    print(get_random_dynasty())

if __name__ == "__main__":
    main()
