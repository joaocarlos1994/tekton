# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.register.home import User
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
@login_not_required
def index():
    contexto = {'save_path': router.to_path(verifica_registro)}
    return TemplateResponse(contexto, template_path="/login_rh/form.html")


@no_csrf
@login_not_required
def verifica_registro(**propriedades):
    query = User.query(User.email == propriedades['email']).get()
    result = query
    if result.email == propriedades['email'] and result.password == propriedades['password']:
        return TemplateResponse(template_path="/candidato/home.html")
    return RedirectResponse(router.to_path(index))