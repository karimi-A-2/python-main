# todo: solve the issue and complete this:

from collections import deque


def sort_dependencies(packages, package_name):
    package_dependencies = []
    q = deque()
    q.extend(packages[package_name])
    while len(q) != 0:
        popped = q.popleft()
        package_dependencies.append(popped)
        q.extend(filter(lambda x: (x not in q) and (x not in package_dependencies), packages[popped]))
    package_dependencies.reverse()
    return package_dependencies


# my_packages = {'pkg1': ['pkg3'], 'pkg2': ['pkg3'], 'pkg3': [], 'pkg4': ['pkg1', 'pkg2']}
my_packages = {'1': ['3'],
               '2': ['5'],
               '3': [],
               '4': ['2'],
               '5': [],
               }
key = '4'
print(sort_dependencies(my_packages, key))
