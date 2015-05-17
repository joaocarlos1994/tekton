from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm

'from __future__ import absolute_import, unicode_literals'
from google.appengine.ext import ndb
from gaepermission.decorator import login_not_required
from gaegraph.model import Node
from tekton import router

@login_not_required
@no_csrf
def index():
    contexto = {'save_path' : router.to_path(salvar)}
    return TemplateResponse(contexto)

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
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'user': user_form}
        return TemplateResponse(contexto, 'register/home.html')
    else:
        user = user_form.fill_model()
        user.put()
        _resp.write(propriedades)
