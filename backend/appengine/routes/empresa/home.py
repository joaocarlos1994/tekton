# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.empresa.form import Empresa, EmpresaForm, editar_form, delete, salvar
from tekton import router


@login_not_required
@no_csrf
def index():
    query = Empresa.query()
    empresa_lista = query.fetch()
    form = EmpresaForm()
    empresa_lista = [form.fill_with_model(user) for user in empresa_lista]
    editar_form_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for empresa in empresa_lista:
        empresa['edith_path'] = '%s/%s' % (editar_form_path, empresa['id'])
        empresa['delete_path'] = '%s/%s' % (delete_path, empresa['id'])
    contexto = {'save_path': router.to_path(salvar), 'empresa_lista': empresa_lista}
    return TemplateResponse(contexto)





