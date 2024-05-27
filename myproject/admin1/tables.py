
import django_tables2 as tables

from customer.models import Departments,Doctors




# class DoctorsTable(tables.Table):
#     class Meta:
#         model = Doctors
#         fields=("doc_name","doc_spec","dep_name","dep_image")
#         table_title = "Doctors"
#         edit_url = "doctor_update"
#         detail_url = "doctor_detail"
#         delete_url = "doctor_delete"


class DoctorsTable(tables.Table):
    doc_name = tables.Column(verbose_name='Doctor Name')
    doc_spec = tables.Column(verbose_name='Doctor Specialization')
    dep_name = tables.Column(verbose_name='Department Name')
    dep_image = tables.Column(verbose_name='Department Image')

    actions = tables.TemplateColumn(
        verbose_name='Actions',
        template_code='''
        <a href="{% url 'doctor2_update' record.id %}" class="btn btn-warning btn-sm"> Edit</a> 
        <a href="{% url 'doctor2_detail' record.id %}" class="btn btn-info btn-sm">Detail</a> 
        <a href="{% url 'doctor2_delete' record.id %}" class="btn btn-danger btn-sm">Delete</a>
        '''
    )

    class Meta:
        model = Doctors
        fields = ("doc_name", "doc_spec", "dep_name", "dep_image", "actions")
        table_title = "Doctors2"




class DepartmentTable(tables.Table):
    dep_name = tables.Column(verbose_name='Department Name')
    dep_description = tables.Column(verbose_name='Department Description')
    actions = tables.TemplateColumn(
        verbose_name='Actions',
        template_code='''
        <a href="{% url "department_update" record.id %}" class="btn btn-warning btn-sm"> Edit</a>
        <a href="{% url "department_detail" record.id %}" class="btn btn-info btn-sm">Detail</a>
        <a href="{% url "department_delete" record.id %}" class="btn btn-danger btn-sm">Delete</a>
        '''
    )

    class Meta:
        model = Departments
        fields = ("dep_name", "dep_description", "actions")
        table_title = "Department"