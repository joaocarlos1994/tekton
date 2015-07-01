from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from tekton import router


@login_not_required
@no_csrf
def index():
    contexto = {'save_path': router.to_path(salvar)}
    return TemplateResponse(contexto, template_path='/empresa/form.html')



class Empresa(Node):
    nome = ndb.StringProperty(required=True)
    cnpj = ndb.StringProperty(required=True)
    endereco = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)

class EmpresaForm(ModelForm):
    _model_class = Empresa


@login_not_required
@no_csrf
def salvar(**propriedades):
    empresa_form = EmpresaForm(**propriedades)
    erros = empresa_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'empresa': empresa_form}
        return TemplateResponse(contexto, 'empresa/form.html')
    else:
        empresa = empresa_form.fill_model()
        empresa.put()
        return TemplateResponse(template_path='/login_rh/form.html')



@login_not_required
@no_csrf
def editar(empresa_id, **propriedades):
    empresa_id = int(empresa_id)
    empresa = Empresa.get_by_id(empresa_id)
    editar_form = EmpresaForm(**propriedades)
    erros = editar_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'empresa': editar_form}
        return TemplateResponse(contexto, 'empresa/form.html')
    else:
        editar_form.fill_model(empresa)
        empresa.put()
        return TemplateResponse(template_path='/empresa/home.html')


@login_not_required
@no_csrf
def editar_form(empresa_id):
    empresa_id = int(empresa_id)
    empresa = Empresa.get_by_id(empresa_id)
    editar_form = EmpresaForm()
    editar_form.fill_with_model(empresa)
    contexto = {'save_path': router.to_path(editar, empresa_id), 'user': editar_form}
    return TemplateResponse(contexto, '/register/form.html')

@login_not_required
@no_csrf
def delete(empresa_id):
    chave = ndb.Key(Empresa, int(empresa_id))
    chave.delete()
    return TemplateResponse(template_path="/empresa/home.html")