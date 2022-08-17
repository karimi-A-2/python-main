# method 1:
name = 'ali'
age = 19
string = 'Hi %s ' % name
print(string)

print('i like to %s chocolate ice creams' % 'eat')
string = '%s is %d years old' % ('ali', 19)
print(string)
string = '%s is %d years old' % (name, age)
print(string)

print('the value of e is: %5.2f' % (24553.7393939))

# method 2:
print('welcome to {} tutorial.'.format('my'))
print('lets {0} and {1} with me.'.format('learn', 'upskill'))
print('{} called {} to informed {} will be absent'.format('Ali', 'Aref', 'Mohammad'))
print('{2} called {1} to informed {0} will be absent'.format('Ali', 'Aref', 'Mohammad'))
print('{a} called {b} to informed {c} will be absent'.format(a='Ali', b='Aref', c='Mohammad'))

# method 3: f-string
tutorial = "python"
subject = 'programming'
place = 'simplilearn'
print(f"lets learn {tutorial} {subject} from {place}.")

n1 = 2
n2 = 3
print(f"the poroduct of {n1} and {n2} is {n1 * n2}")

num = 50
print(f"is number even? {True if num % 2 == 0 else False}")

# method 4: Template String

from string import Template

a1 = 'python'
a2 = 'simplilearn'
n = Template('Hello welcome to $n1 programming by $n2.')
print(n.substitute(n1=a1, n2=a2))

student_name = 'Johnson'
s = Template('Hey, $name! How are you?')
s.substitute(name=student_name)
