from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from routes.empresa.form import Empresa
from tekton import router


@login_not_required
@no_csrf
def index():
    contexto = {'save_path': router.to_path(salvar), 'lista_empresa': return_empresa() }
    return TemplateResponse(contexto, template_path='/vagas/form.html')


class Vaga(Node):
    nome = ndb.StringProperty(required=True)
    quantidade = ndb.IntegerProperty(required=True)
    empresa=ndb.KeyProperty(Empresa, required=True)

class VagaForm(ModelForm):
    _model_class = Vaga



@login_not_required
@no_csrf
def salvar(**propriedades):
    vaga_form = VagaForm(**propriedades)
    erros = vaga_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'vaga': vaga_form}
        return TemplateResponse(contexto, 'vaga/form.html')
    else:
        vaga = vaga_form.fill_model()
        vaga.put()
        return TemplateResponse(template_path='/login_rh/form.html')

@login_not_required
@no_csrf
def editar(vaga_id, **propriedades):
    vaga_id = int(vaga_id)
    vaga = Vaga.get_by_id(vaga_id)
    editar_form = VagaForm(**propriedades)
    erros = editar_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'vaga': editar_form}
        return TemplateResponse(contexto, 'vagas/form.html')
    else:
        editar_form.fill_model(vaga)
        vaga.put()
        return TemplateResponse(template_path='/vagas/home.html')

@login_not_required
@no_csrf
def editar_form(vaga_id):
    vaga_id = int(vaga_id)
    vaga = Empresa.get_by_id(vaga_id)
    editar_form = VagaForm()
    editar_form.fill_with_model(vaga)
    contexto = {'save_path': router.to_path(editar, vaga_id), 'vaga': editar_form}
    return TemplateResponse(contexto, '/vagas/form.html')

@login_not_required
@no_csrf
def delete(vaga_id):
    chave = ndb.Key(Empresa, int(vaga_id))
    chave.delete()
    return TemplateResponse(template_path="/vagas/home.html")

def return_empresa():
    empresas = Empresa.query().order(Empresa.nome)
    lista = empresas.fetch()
    return lista
