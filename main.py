import HolesCounter

text = input()
characters = [(character, text.count(character)) for character in set(text)]
holes_count = sum([number * HolesCounter.count(character) for character, number in characters])

print(f'"{text}" has {holes_count} holes.')