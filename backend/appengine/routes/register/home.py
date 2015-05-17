from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaepermission.decorator import login_not_required
from gaegraph.model import Node
from tekton import router

__author__ = 'joao'

@login_not_required
@no_csrf
def index():
    contexto = {'save_path' : router.to_path(salvar)}
    return TemplateResponse(contexto)

class User(Node):
    nome = ndb.StringProperty(required=True)
    sobreNome = ndb.StringProperty
    endereco = ndb.StringProperty
    email = ndb.StringProperty
    password = ndb.StringProperty

@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    user = User(nome = propriedades['exampleInputNome'],
                sobreNome = propriedades['exampleInputSobreNome'],
                endereco = propriedades['exampleInputEdereco'],
                email = propriedades['exampleInputEdereco'],
                password = propriedades['exampleInputPassword'])
    user.put()
