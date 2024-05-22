
import django_tables2 as tables

from customer.models import Departments,Doctors

# class DepartmentTable(tables.Table):
#     class Meta:
#         model= Departments
#         template_name="django_tables2/semantic.html"
#         fields=("dep_name","dep_description")




class DepartmentTable(tables.Table):
    class Meta:
        model = Departments
        fields=("dep_name","dep_description")
    table_title = "Department"
    edit_url = "update"
    detail_url = "detail"
    delete_url = "delete"



class DoctorsTable(tables.Table):
    class Meta:
        model = Doctors
        fields=("doc_name","doc_spec","dep_name","dep_image")
    table_title = "Doctors"
    edit_url = "update"
    detail_url = "detail"
    delete_url = "delete"
