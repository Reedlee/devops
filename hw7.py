f = open("/etc/passwd","r")
a = f.readlines()
f.close()
users=[]
for line in a:
    users.append(line.split(":"))


f = open("/etc/group","r")
a = f.readlines()
f.close()
groups = []
for line in a:
    groups.append(line.split(':'))

counter = {}
users_guids = {}
for user in users:
    shell = user[-1].replace('\n','')
    guid = user[2]
    username = user[0]
    if counter.get(shell):
        counter[shell] += 1
    else:
        counter[shell] = 1

    if not users_guids.get(shell):
        users_guids[username] = guid

print(users_guids)

group_with_u_guids = {}
for group in groups:
    groupname = group[0]
    users = group[-1].replace('\n','').split(',')
    u_guids = []

    for user in users:
        if len(user) != 0:
            u_guids.append(users_guids[user])
            group_with_u_guids[groupname] = u_guids

with open('./output.txt','a') as f:
    for shell, count in counter.items():
        f.write("%s - %s\n"%(shell,count))

with open('./output.txt','a') as f:
    for group, guids in group_with_u_guids.items():
        f.write("%s: %s\n"%(group,guids))
