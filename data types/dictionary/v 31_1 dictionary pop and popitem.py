me = {
    "name": "mohammad",
    "family": "ordookhani",
    "email": "moh96ordo@gmail.com",
    "address": "nemuneh",
    "phone": "0900",
}
print(me)

pop_value = me.pop("name")
print(pop_value)

# dict.popitem()
# Remove and return a (key, value) pair as a 2-tuple.
# Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.
popitem = me.popitem()
print(popitem)
popitem = me.popitem()
print(popitem)
