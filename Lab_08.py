def is_unique(d):
    values = []
    for key, value in d.items():
        if (value in values):
            return False
        else:
            values.append(value)
    return True

d = {'Marty': 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Wolk', 'Allison': 'Obourn', 'Hal': 'Perkins'}
print(is_unique(d))

d = {'Kendrick': 'Perkins', 'Stuart': 'Reges', 'Jessica': 'Wolk', 'Bruce': 'Reges', 'Hal': 'Perkins'}
print(is_unique(d))

