import argparse

from emp_mgmt import empmgr
from emp_mgmt import Employee

if __name__ == "__main__":
    parser = argparse.ArgumentParser()


    parser.add_argument("--id", type=int ,help="provide employee id")
    parser.add_argument("--action", choices=['add', 'edit', 'delete', 'view'], default='view')
    parser.add_argument("-fs", "--fsname", help="first name")
    parser.add_argument("-ls", "--lsname", help="last name")
    parser.add_argument("-dp", "--dprtmt", help="department", default='bose')
    parser.add_argument("-sl" ,"--salary", help="salary", default=0, type=int)

    args = parser.parse_args()

    empid = args.id
    action = args.action
    fsname = ''
    lsname = ''
    dprtmt = ''
    salary = 0

    if args.fsname:
        fsname = args.fsname

    if args.lsname:
        lsname =args.lsname

    if args.dprtmt:
        dprtmt = args.dprtmt

    if args.salary:
        salary = args.salary

    print(args)

    if action == 'add':
        emp = Employee(empid, fsname, lsname, dprtmt, salary)
        added_emp = empmgr.add(emp)
        print(added_emp)

    elif action == 'edit':
        edited_emp = empmgr.edit(empid, fsname=fsname, lsname=lsname, dprtmt=dprtmt, salary=salary)
        print(edited_emp)

    elif action == 'delete':
        deleted_emp = empmgr.delete(empid)
        print(deleted_emp)

    elif action == 'view':
        empmgr.view(empid)

