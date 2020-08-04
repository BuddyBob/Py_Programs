import json
file = open('similar.txt','r')
raw_list = []
for row in file:
    row = row.replace('\'','')
    row = row.replace('[','')
    row = row.replace(']','')
    row = row.split(',')
    raw_list.append(row)
grouped_lists = {}
for xs in raw_list:
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