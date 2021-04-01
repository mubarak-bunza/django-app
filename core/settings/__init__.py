from decouple import config

ENVIRONMENT = config('ENVIRONMENT')
if ENVIRONMENT == 'dev':
    from .dev import * # noqa

elif ENVIRONMENT == 'testing':
    from .testing import *  # noqa

elif ENVIRONMENT == 'prod':
    from .prod import *  # noqa
