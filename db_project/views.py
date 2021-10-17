from django.shortcuts import render
from db_project.models import SqlServerConn
import pyodbc


def connsql(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=localhost;',
                          'Database = master;',
                          'Trusted_Connection = yes;')

    cursor = conn.cusror()
    cursor.execute('select * from employee')
    result = cursor.fetchall()
    return render(request, 'Index.html', {'SqlServerConn': result})
