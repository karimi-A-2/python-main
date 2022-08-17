n = int(input())
link_dict = dict()
for i in range(n):
    name, link = input().strip().split(' ')
    link_dict[name] = link

class Command:
    def __init__(self, name, params):
        self.name = name
        self.param_dict = dict()
        for item in params:
            param, value = item.split('=', 1)  #
            # param, value = item.split('=')  #  --> wrong:
            # <<<*** we don't know if split returns 2 items we should make sure ***>>>
            self.param_dict[param] = value


t = int(input())
command_list = []
for i in range(t):
    (name, *param_list) = input().strip().split(' ')
    command_list.append(Command(name, param_list))

out_list = []
for command in command_list:
    if command.name not in link_dict:
        out_list.append('[Error] url not found')
        continue
    link_str = link_dict[command.name]
    for param, value in command.param_dict.items():
        if f'<{param}>' not in link_str:
            continue
        link_str = link_str.replace(f'<{param}>', value)
    if '<' not in link_str:  # no parameters left
        out_list.append(link_str)
    else:
        out_list.append('[Error] missing parameter(s)')
for out in out_list:
    print(out)
