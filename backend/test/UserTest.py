# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
import user
from base import GAETestCase

from config.template_middleware import TemplateResponse
from mock import Mock
from routes.register.home import salvar, User

from tekton.gae.middleware.redirect import RedirectResponse


class NewTests(GAETestCase):
    def test_sucesso(self):
        resposta = salvar(nome='Renzo', sobreNome='Nuccitelli', endereco='Fatec', email='renzo@gmail', password='python123')
        self.assertIsInstance(resposta, TemplateResponse)
        self.assertEqual('/login_rh/form.html', resposta.template_path)
        user = User.query().fetch()
        self.assertEqual(1, len(user))
        use = user[0]
        self.assertEqual('Renzo', use.nome)
        self.assertEqual('Nuccitelli', use.sobreNome)
        self.assertEqual('Fatec', use.endereco)
        self.assertEqual('renzo@gmail', use.email)
        self.assertEqual('python123', use.password)



    def test_erro_validacao(self):
        resposta = salvar()
        self.assertIsInstance(resposta, TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(User.query().get())
        expected = {'nome': u'Required field', 'password': u'Required field', 'sobreNome': u'Required field',
                             'email': u'Required field', 'endereco': u'Required field'}
        self.assertDictEqual(expected, resposta.context['erros'])



mock = Mock()

mock.bizarro(9)
mock.bizarro.assert_called_once_with(9)
