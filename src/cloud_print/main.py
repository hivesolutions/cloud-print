#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class CloudPrintApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "cloud_print",
            parts = (
                appier_extras.AdminPart,
            ),
            *args, **kwargs
        )

if __name__ == "__main__":
    app = CloudPrintApp()
    app.serve()
else:
    __path__ = []
