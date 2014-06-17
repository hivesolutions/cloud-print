#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from cloud_print.models import printer

class Node(appier_extras.admin.Base):

    name = appier.field(
        index = True,
        immutable = True
    )

    printers = appier.field(
        type = appier.references(
            printer.Printer,
            name = "id"
        )
    )

    @classmethod
    def validate(cls):
        return super(Node, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name")
        ]

    @classmethod
    def list_names(cls):
        return ["name"]
