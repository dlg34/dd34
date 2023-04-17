def f1():
    print("""
        -------菜单选项-------
        1. 添加功能
        2. 删除功能
        3. 查询功能
        4. 展示功能
        5. 修改功能
        6. 退出
        ----------------------
    """)

l=[]
def add():
    print('--------欢迎来到信息添加页面---------')
    name = input('请输入姓名：')
    age = int(input('请输入年龄：'))
    sex = input('请输入性别：')
    for i in l:
        if i['name']== name and i['age'] == age and i['sex'] == sex:
            print('该学生已存在')
            return
    d = {}
    d['name']=name
    d['age'] = age
    d['sex']=sex
    print('添加成功')
    l.append(d)

def delete():
    print('--------欢迎来到学生信息删除页面---------')
    n = int(input('请输入你要删除的学生序号：'))
    if 0 <= n <= len(l) -1:
        m = input('你是否要删除(Y/N)：')
        if m == 'Y':
            del l[n]
            print('删除成功')
        elif m == 'N':
            print('取消删除！')
    else:
        n = int(input('请重新输入你要删除的学生序号：'))
        if 0 <= n <= len(l) - 1:
            m = input('你是否要删除(Y/N)：')
            if m == 'Y':
                del l[n]
                print('删除成功')
            elif m == 'N':
                print('取消删除！')


def find():
    print('--------欢迎来到学生信息查找页面---------')
    n = input('请输入你要查询的姓名：')
    for i in l:
        if i['name'] == n:
            print(i)
        else:
            print('该学生不存在')

def show():
    print('--------欢迎来到学生信息展示页面---------')
    for i,j in enumerate(l):
        print(f'序号：{i} 姓名：{j["name"]} 年龄：{j["age"]} 性别：{j["sex"]}')

def update():
    print('--------欢迎来到学生信息修改页面---------')
    show()
    print('以上是所有学生的信息！')
    n= int(input('请输入你要修改的学生序号：'))
    if 0<= n <= len(l)-1:
        print("""
        -------修改选项-------
        1. 姓名
        2. 年龄
        3. 性别
        4. 全部
        ---------------------
        """)
        m = int(input('请输入修改选项：'))
        if m == 1:
            l[n]['name']=input('修改后的姓名：')
            print('修改成功！')
        elif m == 2:
            l[n]['age'] = int(input('修改后的年龄：'))
            print('修改成功！')
        elif m == 3:
            l[n]['sex'] = input('修改后的性别：')
            print('修改成功！')
        elif m == 4:
            l[n]['name']=input('修改后的姓名：')
            l[n]['age'] = int(input('修改后的年龄：'))
            l[n]['sex'] = input('修改后的性别：')
            print('修改成功！')
    print(l[n])



def z():
    while True:
        f1()
        a=int(input('请输入你的选项：'))
        if a == 1:
            add()
        elif a == 2:
            delete()
        elif a == 3:
            find()
        elif a == 4:
            show()
        elif a == 5:
            update()
        elif a == 6:
            break

if __name__ == '__main__':
    z()
