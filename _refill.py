# encoding: utf-8
# 補給

cmd = {}
cmd['bmo'] = ''
cmd['shared_menu'] = dict()

cmd['refill'] = dict()

for key, value in cmd['shared_menu'].items():
    cmd['refill'][key] = value

cmd['refill']['f1'] = ("f1 cmd", 0, (150,233))

print cmd['refill']['f1']
