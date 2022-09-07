list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["nazla", "dewi", "lulu"]
list_mix = [20, "arya", True, "bryan"]

print("data sebelum diubah", list_string)
list_string[0] = "lev"
print("data setelah diubah", list_string)

print("data sebelum diubah", list_string)
list_string[0] = "lev"
list_string[1] = "albedo"
list_string[2] = "william"
print("data setelah diubah", list_string)

print("data sebelum diubah", list_mix)
list_mix[0] = 19
list_mix[1] = "adinata"
list_mix[2] = False
list_mix[3] = "duke"
print("data setelah diubah", list_mix)

# perulangan for

x = ['lev', 'albedo', 'william']

for y in x:
    print(y)


for o in list_string:
    print(o)

for s in list_integer:
    print(s)

for t in list_mix:
    print(t)
