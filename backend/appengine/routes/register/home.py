import json
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb import form
from gaeforms.ndb.form import ModelForm
from tekton.gae.middleware.json_middleware import JsonResponse
from tekton.gae.middleware.redirect import RedirectResponse

'from __future__ import absolute_import, unicode_literals'
from google.appengine.ext import ndb
from gaepermission.decorator import login_not_required
from gaegraph.model import Node
from tekton import router

@login_not_required
@no_csrf
def index():
    query = User.query()
    user_lista = query.fetch()
    form = UserForm()
    user_lista = [form.fill_with_model(user) for user in user_lista]
    str_json = json.dumps(user_lista)
    editar_form_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for user in user_lista:
        user['edith_path'] = '%s/%s' % (editar_form_path, user['id'])
        user['delete_path'] = '%s/%s' % (delete_path, user['id'])
    contexto = {'user_lista': str_json, 'rest_new_path': router.to_path(salvar)}
    return TemplateResponse(contexto)

@login_not_required
@no_csrf
def delete(user_id):
    chave = ndb.Key(User, int(user_id))
    chave.delete()
    return TemplateResponse(template_path="/register/home.html")

@login_not_required
@no_csrf
def form():
    contexto = {'save_path': router.to_path(salvar)}
    return TemplateResponse(contexto, template_path='/register/form.html')

@login_not_required
@no_csrf
def editar_form(user_id):
    user_id = int(user_id)
    user = User.get_by_id(user_id)
    user_form = UserForm()
    user_form.fill_with_model(user)
    contexto = {'save_path': router.to_path(editar, user_id), 'user': user_form}
    return TemplateResponse(contexto, '/register/form.html')

@login_not_required
@no_csrf
def editar(user_id, **propriedades):
    user_id = int(user_id)
    user = User.get_by_id(user_id)
    user_form = UserForm(**propriedades)
    erros = user_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'user': user_form}
        return TemplateResponse(contexto, 'register/form.html')
    else:
        user_form.fill_model(user)
        user.put()
        return TemplateResponse(template_path='/login_rh/form.html')

class User(Node):
    nome = ndb.StringProperty(required=True)
    sobreNome = ndb.StringProperty(required=True)
    endereco = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)


class UserForm(ModelForm):
    _model_class = User

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    user_form = UserForm(**propriedades)
    erros = user_form.validate()
    if erros:
        _resp.status_code=400
        return JsonResponse(erros)
    else:
        user = user_form.fill_model()
        user.put()
        return JsonResponse(user_form.fill_with_model(user))












