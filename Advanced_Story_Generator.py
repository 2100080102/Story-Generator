import random
nouns = [
    "wizard", "castle", "dragon", "forest", "knight", "princess",
    "river", "village", "king", "queen", "monster", "hero", "treasure",
    "sword", "magic", "spell", "adventure", "journey", "quest", "mystery"
]
verbs = [
    "run", "jump", "fly", "fight", "explore", "discover", "find",
    "save", "escape", "defeat", "battle", "search", "uncover", "rescue",
    "transform", "cast", "bewitch", "enchant", "travel", "navigate"
]
adjectives = [
    "brave", "mysterious", "magical", "ancient", "dark", "bright",
    "fearless", "cunning", "wise", "noble", "fierce", "majestic",
    "hidden", "legendary", "enchanted", "haunted", "forbidden", "dangerous",
    "glorious", "heroic"
]
adverbs = [
    "quickly", "silently", "bravely", "mysteriously", "magically",
    "boldly", "cunningly", "wisely", "nobly", "fiercely", "majestically",
    "secretly", "heroically", "fearlessly", "gloriously", "dangerously",
    "gracefully", "elegantly", "powerfully", "stealthily"
]
pronouns = [
    "he", "she", "they", "we", "I", "you", "it", "me", "him", "her",
    "us", "them", "this", "that", "these", "those"
]
conjunctions = [
    "and", "but", "or", "so", "because", "although", "while", "if",
    "when", "since", "unless", "until", "where", "after", "before",
    "as", "even", "though", "although"
]
prepositions = [
    "in", "on", "at", "by", "with", "about", "against", "between",
    "under", "over", "through", "during", "before", "after", "above",
    "below", "near", "far", "inside", "outside"
]
def generate_story():
    story = []
    story.append(f"Once upon a time, in a {random.choice(adjectives)} {random.choice(nouns)},")
    story.append(f"there was a {random.choice(adjectives)} {random.choice(nouns)} who loved to {random.choice(verbs)}.")
    story.append(f"One day, they decided to {random.choice(verbs)} {random.choice(adverbs)} in the {random.choice(nouns)}.")
    story.append(f"Along the way, they met a {random.choice(adjectives)} {random.choice(nouns)} who helped them {random.choice(verbs)}.")
    story.append(f"After many adventures, they finally found the {random.choice(adjectives)} {random.choice(nouns)} they were looking for.")
    story.append("And they lived happily ever after.")
    return " ".join(story)