#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class BaseController(appier.Controller):

    @appier.route("/hello", "GET")
    def hello(self):
        return "Hello World"
