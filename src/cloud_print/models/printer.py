#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class Printer(appier_extras.admin.Base):

    name = appier.field(
        index = True,
        immutable = True
    )

    type = appier.field(
        index = True
    )

    @classmethod
    def validate(cls):
        return super(Printer, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),

            appier.not_null("type"),
            appier.not_empty("type")
        ]

    @classmethod
    def list_names(cls):
        return ["name", "type"]
