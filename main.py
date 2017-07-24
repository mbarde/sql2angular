from sqlTable import SQLTable
from serviceGenerator import generate_service

fields = ['username', 'email', 'password']
table = SQLTable('users', 'user', fields)

generate_service(table)
