# mainserver.py
from time import ctime
from aspire.core.security_service import CORSMiddleware
from aspire import API
from Application.config import config

gco = config.get('dev')  #  Global Config Object  == Development config
print(gco.TEMPLATES_DIR)
slabs = API(
    debug=gco.DEBUG,
    title=gco.TITLE,
    version=gco.VERSION,
    description=gco.DESCRIPTION,
    terms_of_service=gco.TERMS,
    contact=gco.CONTACT,
    license=gco.LICENSE,
    auto_escape=gco.AUTO_ESCAPE,
    templates_dir=gco.TEMPLATES_DIR,
    static_dir=gco.STATIC_DIR,
    secret_key=gco.SECRET_KEY,
    enable_https=gco.SERVE_HTTPS,
    static_route=gco.STATIC_ROUTE,
    #docs_route=gco.DOCUMENT_ROUTE
)
slabs.add_middleware(
    CORSMiddleware,
    allow_origins=gco.ORIGINS,
    allow_methods=gco.METHODS,
    allow_headers=gco.HEADERS,
    allow_credentials=gco.CREDENTIALS,
    allow_origin_regex=gco.ORIGIN_REGEX,
    expose_headers=gco.EXPOSED_HEADERS
)
