from typing import List

from ninja import NinjaAPI
from .schema import ProjectIn, ProjectOut, ProjectUpdate, UserIn, UserOut
from django.shortcuts import get_object_or_404
from .models import Project , Release, User

import jwt
from ninja.security import HttpBearer

api = NinjaAPI()

@api.post("projects", tags=["projects"])
def create_project(request,payload:ProjectIn):
    project = Project.objects.create(**payload.dict())
    return {"message": f"Ajout effectuée du projet id: {project.id}"}
   

@api.get("projects/{project_id}",response=ProjectOut, tags=["projects"])
def get_project(request,project_id:int):
    project = get_object_or_404(Project,id=project_id)
    return project

@api.patch("projects/{project_id}", tags=["projects"])
def update_project(request,project_id:int,payload: ProjectUpdate):
    project = get_object_or_404(Project, id=project_id)
    for attr,value in payload.dict().items():
        if value:
            setattr(project,attr,value)
    project.save()
    return {"message": f"Modication reussite du projet id: {project.id}"}


@api.delete("projects/{project_id}", tags=["projects"])
def delete_project(request, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return {"message": f"Suppression effectuée avec id: {project_id}"}

@api.get("projects",response=List[ProjectOut], tags=["projects"])
def list_projects(request):
    qs = Project.objects.all()
    return qs


##Enregistrer un nouvel utilisateur
@api.post("users", tags=["users"])
def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        #user.set_password(password)

        #user.is_staff = True
        user.is_superuser = True
        #user.is_admin = True
        user.save(using=self._db)
        return {"message": f"Utilisateur crée avec succès"}


#@api.post("users", tags=["users"])
#def create_user(request,payload:UserIn):
#    user = User.objects.create(**payload.dict())
#    return {"message": f"Utilisateur crée avec succès"}


#Authentification avec un token