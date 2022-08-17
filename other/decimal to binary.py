decimal = int(input("Enter decimal: "))
no_dec_digits = len(str(decimal))

# base = 2
base = int(input("Enter base: "))
no_base_digits = len(str(base))
while decimal != 0:
    rem = decimal % base
    tmp = decimal // base
    print(str(decimal).rjust(no_dec_digits), "/",
          base, "=", str(tmp).rjust(no_dec_digits),
          "  --->", str(rem).rjust(no_base_digits))
    decimal //= base
