from hash_table import HashTable

table = HashTable(capacity=1)
for i in range(20):
    num_pairs = len(table)
    num_empty = table.capacity - num_pairs
    print(f"{num_pairs}/{table.capacity}: ",
          ("X" * num_pairs) + ("." * num_empty)
          )
    table[i] = i


# table["name"] = "Peter"
# table["age"] = 25
#
# print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
