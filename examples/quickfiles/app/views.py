from flask.ext.appbuilder.models.datamodel import SQLAModel
from flask.ext.appbuilder.views import ModelView, CompactCRUDMixin
from app.models import Project, ProjectFiles
from app import appbuilder, db


class ProjectFilesModelView(ModelView):
    datamodel = SQLAModel(ProjectFiles)

    label_columns = {'file_name': 'File Name', 'download': 'Download'}
    add_columns = ['file', 'description','project']
    edit_columns = ['file', 'description','project']
    list_columns = ['file_name', 'download']
    show_columns = ['file_name', 'download']


class ProjectModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAModel(Project)
    related_views = [ProjectFilesModelView]

    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

    add_columns = ['name']
    edit_columns = ['name']
    list_columns = ['name', 'created_by', 'created_on', 'changed_by', 'changed_on']
    show_fieldsets = [
        ('Info', {'fields': ['name']}),
        ('Audit', {'fields': ['created_by', 'created_on', 'changed_by', 'changed_on'], 'expanded': False})
    ]


db.create_all()
appbuilder.add_view(ProjectModelView, "List Projects", icon="fa-table", category="Projects")
appbuilder.add_view_no_menu(ProjectFilesModelView)
