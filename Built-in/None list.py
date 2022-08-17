band = list()
for i in range(3):
    band.append(None)
print(band)

band_2 = [None for i in range(3)]
print(band_2)

if band[0] is None:
    print('yes')
    