'''
module will provide a class for employee and operations with employee.
'''

from pathlib import Path
from abc import abstractmethod
from src.ems import csvdb as db

BASE_DIR = Path(__file__).resolve().parent
DBPATH = BASE_DIR / 'EMPFILE.csv'


class ERROR:
    ADD = 'error in add emplyee',
    DEL = 'error in delete employee',
    EDT = 'error in edit employee',
    VWT = 'error in view employee'


class Employee:
    '''
    class represent Employee.

    :param str empid: Employee id with unique
    :param str fsname: Employee first name
    :param str lsname: Employee last name
    :param str dprtmt: Employee work department
    :param int salary: Employee salary

    '''

    LIMIT = 3   # limit for changing fsname and lsname

    def __init__(self, empid, fsname, lsname=None, dprtmt=None, salary=0):
        self.id = empid
        self.fsname = fsname
        self.lsname = lsname
        self.dprtmt = dprtmt
        self.salary = salary
        self._limit = Employee.LIMIT
        self._status = 1


class Manager:

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def view(self):
        pass


class EMPManager(Manager):

    ACTIVE = 1  # added and active
    DELETED = 0 # deleted and inactive

    def add(self, emp):
        ''' add an emp to system with status active '''

        # check if employee exists
        allempdict = self.get_all_emp()
        if self.emp_exists(emp.id, allempdict):
            return ERROR.ADD

        # normalize employee values
        allempdict = self._build_dict(allempdict, emp)

        # add employee to db
        db.dict_to_csv(allempdict, DBPATH, delimiter=',')

        return emp.id

    def edit(self, empid, **kwargs):
        ''' edit an emp details of active account only '''

        # check if employee exists
        allempdict = self.get_all_emp()
        if not self.emp_exists(empid, allempdict):
            return ERROR.EDT

        # check if employee deleted
        empdict = self.get_emp(empid, allempdict)

        if self.emp_deleted(empdict):
            return ERROR.EDT

        # update existing employee details

        # check limit to edit first and last name
        limit = int(empdict[-1]['limit'])
        change_limit = False

        for key, value in kwargs.items():

            if key == 'fsname' and value.strip() != '' and limit:
                empdict[0]['fsname'] =  str(value)
                change_limit = True
            elif key == 'fsname' and value.strip() != '' and limit == 0:
                print(f"{empdict[0]['fsname']} have reached limit to change first name.")


            if key == 'lsname' and value.strip() != '' and limit:
                empdict[1]['lsname'] =  str(value)
                change_limit = True
            elif key == 'lsname' and value.strip() != '' and limit == 0:
                print(f"{empdict[0]['fsname']} have reached limit to change last name.")

            if key == 'dprtmt':
                empdict[2]['dprtmt'] =  str(value)

            if key == 'salary':
                empdict[3]['salary'] =  str(value)

        # update limit when changing first or last name
        if change_limit:
            limit -= 1
            empdict[-1]['limit'] =  str(limit)


        empdict = {('empid', str(empid)): empdict}
        allempdict = self._build_dict(allempdict, empdict)

        # update employee to db
        db.dict_to_csv(allempdict, DBPATH, delimiter=',')

        return empid


    def delete(self, empid):
        ''' delete an emp with setting status 0 means inactive'''

        # check if employee exists
        allempdict = self.get_all_emp()
        if not self.emp_exists(empid, allempdict):
            return ERROR.DEL

        # check if employee already deleted
        empdict = self.get_emp(empid, allempdict)

        if self.emp_deleted(empdict):
            return ERROR.DEL

        # delete an emp with setting status 0
        empdict[-2]['status'] = str(EMPManager.DELETED)

        empdict = {('empid', str(empid)): empdict}
        allempdict = self._build_dict(allempdict, empdict)

        # delete employee from db
        db.dict_to_csv(allempdict, DBPATH, delimiter=',')

        return empid


    def view(self, empid, filtter):
        ''' display employee by empid or filter '''

        empdict = {}
        allempdict = self.get_all_emp()

        if empid:

            # check if employee exists
            if not self.emp_exists(empid, allempdict):
                print(ERROR.VWT)
                return ERROR.VWT

            empdict[('empid', str(empid))] = self.get_emp(empid, allempdict)

        else:
            empdict = self.get_emp_by_filter(allempdict, filtter)

        # print employee
        for key, value in empdict.items():
            print (key[1], ' => ' ,value)


    def emp_exists(self, empid, empdict):
        empid = ('empid', str(empid))
        return empid in empdict

    def emp_deleted(self, empdict):
        status = empdict[-2]['status']
        return str(EMPManager.DELETED) == str(status)


    def get_all_emp(self):
        ''' return a dict for emp '''

        empdict = db.csv_to_dict(DBPATH, delimiter=',')
        return empdict

    def get_emp(self, empid, empdict):
        ''' return a list of values for emp '''

        return empdict[('empid', str(empid))]

    def get_emp_by_filter(self, empdict, filtter):

        actempdict = {}
        dltempdict = {}

        for key, value in empdict.items():
            status = int(value[-2]['status'])
            if status == 1:
                actempdict[key] = value
            else:
                dltempdict[key] = value

        if filtter == 'active':
            return actempdict
        elif filtter == 'deleted':
            return dltempdict

        return empdict

    def _build_dict(self, empdict, emp):
        ''' update all empdict with emp object/dict '''

        if not isinstance(emp, dict):

            empdict[('empid', f"{emp.id}")] = [
                {'fsname' : f"{emp.fsname}"},
                {'lsname' : f"{emp.lsname}"},
                {'dprtmt' : f"{emp.dprtmt}"},
                {'salary': f"{emp.salary}"},
                {'status': f"{emp._status}"},
                {'limit': f"{emp._limit}"}
            ]

        else:
            key = list(emp.keys())[0]
            values = list(emp.values())[0]

            empdict[key] = [
                {'fsname' : values[0]['fsname']},
                {'lsname' : values[1]['lsname']},
                {'dprtmt' : values[2]['dprtmt']},
                {'salary':  values[3]['salary']},
                {'status':  values[4]['status']},
                {'limit':   values[-1]['limit']}
            ]


        return empdict


    def str_to_int(self, empdict):
        buildict = {}
        for key, value in empdict.items():
            buildict[key] = value
            if key in ['empid', 'salary', 'status', 'limit']:
                buildict[key] = int(value)

        return buildict

    def int_to_str(self, empdict):
        buildict = {}
        for key, value in empdict.items():
            buildict[key] = value
            if key in ['empid', 'salary', 'status', 'limit']:
                buildict[key] = str(value)

        return buildict

empmgr = EMPManager() # create a manager for employee
