import re

match = re.search("test", "this is test")
print(match)

pattern = re.compile('Py...n')
match = pattern.search('Python is great')
print(match)

pattern = re.compile('Py...n')
match = pattern.search('Python is great')
if match:
    print(match.group())
else:
    print("pattern not found")

match = re.search("(\\w+) (\\w+)", "Isaac Newton , physicist")
print(match)
print(match.group())        # The entire match
print(match.groups())
print(match.group(0))       # The entire match
print(match.group(1))       # The first parenthesized subgroup.
print(match.group(2))       # The second parenthesized subgroup.
print(match.group(1, 2))    # Multiple arguments give us a tuple.

match = re.search("(\\d+)\\.(\\d+)", "24.1632")
print(match.group())
print(match.groups())
match = re.search("\\d+\\.\\d+", "24.1632")
print(match.group())
print(match.groups())

# match.groupdict([dafault = None])

match = re.search("(?P<first_name>\\w+) (?P<last_name>\\w+)", "Elvis Presley")
print(match.groupdict())
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.groups())

match = re.search('(\\w+),(\\w+),(\\w+)', 'Jazz,Rock,Pop')
print(match.groups())
print(match.expand('-->\1---->\2------>\3'))  # Warning!!!
print(match.expand('-->\\1---->\\2------>\\3'))
print(match.expand(r'-->\1---->\2------>\3'))


match = re.search(r'(?P<num>\d+)', 'Top 100 songs')
print(match.group(1))
print(match.expand(r'--- \g<num> ---'))
print(match.expand(r'--- \g<1> ---'))

# match.start([group]) & match.end([group])

email = "tony@tiremove_thisger.net"
match = re.search(r"remove_this", email)
print(match.start())
print(match.end())
print(email[match.start() : match.end()])
print(email[:match.start()] + email[match.end():])

match = re.search(r"(\d+)\.(\d+)", "24.1632")
print(match.start())
print(match.end())
print(match.start(1))
print(match.end(1))
print(match.start(2))
print(match.end(2))

# Match.span([group])

match = re.search(r"(\d+)\.(\d+)", "24.1632")
print(match.span())
print(match.span(1))
print(match.span(2))
print(match.span(3))

# Match.re & Match.string

email = "tony@tiremove_thisger.net"
match = re.search("remove_this", email)
print(match.re)
print(match.string)
print(match.string[match.start() : match.end()])
print("\n")
match = re.search(r"(\d+)\.(\d+)", "24.1632")
print(match.re)
print(match.string)

# match(pattern, string, flags=0)

match = re.match(r'\d+', '123@USERNAME')
print(match)
match = re.match(r'\d+', 'USERNAME@123')
print(match)
match = re.search(r'\d+', '123@USERNAME')
print(match)
match = re.search(r'\d+', 'USERNAME@123')
print(match)

# fullmatch(pattern, string, flags=0)

match = re.fullmatch(r'\d+', '123@USERNAME')
print(match)
match = re.fullmatch(r'\d+', '123')
print(match)
print("\n")

match = re.search(r'^\d+$', '123')
print(match)
match = re.match(r'\d+$', '123')
print(match)
match = re.fullmatch(r'\d+', '123')
print(match)

# findall(pattern, string, flags=0)

string = "My number is 123456789 and my friend's number is 987654321"
results = re.findall(r'\d+', string)
print(type(results))
print(results)
print("\n")

results = re.findall(r'#(\w+)#', '#Perl#.#Python#.#Ruby#')
print(results)
results = re.findall(r'#\w+#', '#Perl#.#Python#.#Ruby#')
print(results)
print("\n")

results = re.findall(r'(\w+)@(\d+)', 'Perl@1987,Python@1991,Ruby@1995')
print(results)

# finditer(pattern, string, flags=0)

string = "My number is 123456789 and my friend's number is 987654321"
result = re.finditer(r'\d+', string)
print(type(result))
print(result.__next__())
print(result.__next__())
# result.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
print("\n")

for match in re.finditer(r'#(\w+)#', '#Perl#.#Python#.#Ruby#'):
    print(match)
print("\n")

for match in re.finditer(r'#\w+#', '#Perl#.#Python#.#Ruby#'):
    print(match)
print("\n")

for match in re.finditer(r'(\w+)@(\d+)', 'Perl@1987,Python@1991,Ruby@1995'):
    print(match)

# sub(pattern, repl, string, count=0, flags=0)

string = 'Perl@1987,Python@1991,Ruby@1995'
repl = ' - '
pattern = r'@\d+,?'
result = re.sub(pattern, repl, string)
print(type(result))
print(result)
result = re.sub(pattern, repl, string, 2) #  count=2
print(result)
result = re.sub(pattern, repl, string, 1) #  count=1
print(result)
print("\n")


#                                 # -------------- with expand ------------- ##
result = re.sub(r'(\w+),(\w+),(\w+)', r'(\1) (\2) (\3)', 'Jazz,Rock,Pop')
print(result)
print(re.sub(r'(\w+),(\w+),(\w+)', r'(\g<1>) (\g<2>) (\g<3>)', 'Jazz,Rock,Pop'))
print(re.sub(r'(?P<num>\d+)', r'#\g<num>#', 'Top 100 songs'))
print(re.sub('x*', '-', 'abc@123,456'))  # *******
re.sub(r'\d', '-', 'abc@xyz')  # Without matching


#                                  # -------------- when repl is function ------------- ##
def mask_numbers(match):
    string = match.group(0)  # The matching string
    # string.isdigit() returns True if all characters in string are digits
    if string.isdigit():
        return '_' * len(string)
    else:
        return string
    

print(re.sub(r'\w+', mask_numbers, 'Perl.1987.Python.1991.Ruby.1995'))
print(re.sub(r'\w+', mask_numbers, 'My ID is 123.45679 and your ID is 98521.2'))
print(re.sub(r'\d+', lambda match : '_' * len(match.group(0)), 'Perl.1987.Python.1991.Ruby.1995'))
print(re.sub(r'\d+', lambda match : '_' * len(match.group(0)), 'My ID is 123.45679 and your ID is 98521.2'))

# subn(pattern, repl, string, count=0, flags=0)

string = 'Perl@1987,Python@1991,Ruby@1995'
repl = ' - '
pattern = r'@\d+,?'
result = re.subn(pattern, repl, string)
print(type(result))
print(result)
print(re.subn(pattern, repl, string, count=2))
print(re.subn(pattern, repl, string, count=1))

# split(pattern, string, maxsplit=0, flags=0)

string = 'Perl,Python,Ruby'
pattern = ','
result = re.split(pattern, string)
print(type(result))
print(result)
print(re.split(pattern, string, maxsplit=1))
print(re.split(pattern, string, maxsplit=2))
print("\n")

print(re.split('(_)', 'Perl_Python_Ruby'))
print(re.split('/', '/Perl/Python/Ruby/'))
print(re.split('(/)', '/Perl/Python/Ruby/'))
print("\n")

print(re.split('(?:_)', 'Perl_Python_Ruby'))
print(re.split('(?:/)', '/Perl/Python/Ruby/'))
