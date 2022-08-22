a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

zip_obj = zip(a, b)
print(next(zip_obj))

iter_zip_obj = iter(zip_obj)  # iter(iterator) --> return self
print(next(iter_zip_obj))

print(zip_obj == iter_zip_obj)  # True
print(zip_obj is iter_zip_obj)  # True

# zip objects are iterators
