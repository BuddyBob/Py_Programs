import json

# Your lists.
raw_lists = [
    ['Australia', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['Australia', ' 4', ' 4', ' 4', ' 4', ' 4', ' 4', ' 4'],
    ['Australia', ' 83', ' 92', ' 105', ' 112', ' 116', ' 123', ' 123'],
    ['Canada', ' 7', ' 8', ' 8', ' 8', ' 8', ' 8', ' 8'],
    ['Canada', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3'],
    ['Canada', ' 2807', ' 2812', ' 2813', ' 2816', ' 2819', ' 2821', ' 2822'],
    ['Canada', ' 5667', ' 5670', ' 5670', ' 5673', ' 5674', ' 5678', ' 5681'],
    ['China', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1'],
    ['China', ' 8', ' 8', ' 8', ' 8', ' 8', ' 8', ' 8'],
    ['China', ' 2', ' 2', ' 2', ' 2', ' 2', ' 2', ' 2'],
    ['China', ' 6', ' 6', ' 6', ' 6', ' 6', ' 6', ' 6'],
    ['China', ' 22', ' 22', ' 22', ' 22', ' 22', ' 22', ' 22'],
    ['China', ' 4512', ' 4512', ' 4512', ' 4512', ' 4512', ' 4512', ' 4512'],
    ['China', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1'],
    ['China', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1'],
    ['China', ' 2', ' 2', ' 2', ' 2', ' 2', ' 2', ' 2'],
    ['China', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['China', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3'],
    ['China', ' 7', ' 7', ' 7', ' 7', ' 7', ' 7', ' 7'],
    ['China', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3'],
    ['China', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['China', ' 2', ' 2', ' 2', ' 2', ' 2', ' 2', ' 2'],
    ['Denmark', ' 613', ' 613', ' 614', ' 615', ' 615', ' 615', ' 615'],
    ['France', ' 38', ' 38', ' 39', ' 39', ' 39', ' 39', ' 39'],
    ['France', ' 4', ' 4', ' 4', ' 4', ' 4', ' 4', ' 4'],
    ['France', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3', ' 3'],
    ['France', ' 30096', ' 30109', ' 30108', ' 30123', ' 30150', ' 30150', ' 30150'],
    ['Netherlands', ' 15', ' 15', ' 15', ' 15', ' 15', ' 15', ' 16'],
    ['United Kingdom', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1', ' 1'],
]

# Group the lists based on country. This will give us a dict-of-lists-of-lists.
# Like this: grouped_lists{COUNTRY} = [ [...], [...], etc ]
grouped_lists = {}
for xs in raw_lists:
    # Grab country name and the rest of the values.
    c = xs[0]
    vals = xs[1:]
    assert len(vals) == 7
    # Convert the values to integers using a list comprehension.
    nums = [int(v.strip()) for v in vals]
    # Add the list of numbers to the country's list-of-lists.
    grouped_lists.setdefault(c, []).append(nums)

# Sum up the separate lists for each country.
country_totals = {}
for c, xss in grouped_lists.items():
    # Initialize the key for the country.
    country_totals[c] = []
    # Since xss is a list-of-lists for the current country, we can use zip() to
    # weave together the values based on their positions (or indexes). For
    # example, on the first iteration tup will be a tuple holding the first
    # elements from the separate lists. On second iteration, second elements. Etc.
    for tup in zip(*xss):
        country_totals[c].append(sum(tup))

# Take a look.
print(json.dumps(country_totals))