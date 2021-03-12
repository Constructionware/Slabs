import logging
import os
from aspire.core.security_service import GenerateId

class Config:
    #----- ABOUT APPLICATION --------
    TITLE:str = "Slabs Engineering"
    DESCRIPTION:str = "Slabs Structure Engineering Software solution is intended to provide structural, civil engineers and construction managers with a set of tools for execution and automation of their construction and engineering processes."
    TERMS:str = "https://github.com/Constructionware/Slabs/terms"
    CONTACT:dict = {
        "name": "Slabs Support Team",
        "url": "https://slabs.com/support",
        "email": "support@slabs.com"
    }
    LICENSE:dict = {
        "name": "MIT",
        "url": "opensource.org/license/MIT"
    }
    VERSION:float = 1.0
    #--- APPLICATION DIRECTORIES -----
    BASE_DIR:str = os.path.dirname(os.path.realpath(__file__))
    DATABASE_DIR:str = os.path.realpath("SlabDB")
    STATIC_DIR:str =  os.path.realpath("SlabStatic")   
    IMAGES_DIR = os.path.join(STATIC_DIR, 'imgs')    
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'Gui')
    X11_TEMPLATES = os.path.join(TEMPLATES_DIR, 'xslab')
    X11_STATIC = os.path.join(X11_TEMPLATES, 'static')

    #---  SECURITY -----

    AUTO_ESCAPE:bool = False
    SECRET_KEY:str = None
    SERVE_HTTPS:bool = False
    SSL_REDIRECT =False
    
    #--- NETWORK ------
  
    PORT:int = 5595
    HOST:str = '0.0.0.0'
    CONNECTIONS:int = 1000
    MAX_REQUESTS:int = 100
    ORIGINS:list = ["*"]
    METHODS:list = ["*"]
    HEADERS:list = ["*"]
    CREDENTIALS:bool = False
    ORIGIN_REGEX:object = None
    EXPOSED_HEADERS:list = [
        "Access-Controll-Allow-Origin",
        "Access-Controll-Allow-Credentials",
        "Access-Controll-Allow-Expose-Headers"
    ]
    MAX_AGE:int = 3600

    #---- DATABASE ------
    SQL_DATABASE_URI:dict = {        
        "admin": f"sqlite:///{DATABASE_DIR}/slabs-xam.sqlite",
        "analytics": f"sqlite:///{DATABASE_DIR}/slabs-xan.sqlite",
        "slabs": f"sqlite:///{DATABASE_DIR}/slabs-xas.sqlite"
    }
    JSON_DATABASE_URL:dict = {
        "slabs": f"http://localhost:5984/slabs/",        
    }

    #------ ROUTES -----
    STATIC_ROUTE:str = '/static'
    DOCUMENT_ROUTE:str = '/docs'

    
    #---- RUNTIME ------
    MODE:str = 'Default'
    DEBUG:bool = True
    LOOP:str = 'asyncio'
    ACCESS_LOG:bool = False

    #---- INTITIALIZE -----
    def __init__(self):
        self.__setup     

    @property
    def __set_keygeneral(self):
        self.keygeneral = GenerateId()
    
    @property
    def __set_secretkey(self):
        self.SECRET_KEY = self.keygeneral.gen_id('app')
    
    def make_dir(self, directory):
        if not os.path.isdir(directory):
            os.mkdir(directory)
        pass

    def list_directory(self, directory):
        return os.listdir( directory )

    @property
    def __create_system_directories(self):
        ''' Create System Directories '''   
        self.dirs = [
            self.DATABASE_DIR, 
            self.STATIC_DIR,
            self.IMAGES_DIR            
        ]
        for item in self.dirs:
            self.make_dir(item)

    @property
    def __setup(self):
        self.__set_keygeneral
        self.__set_secretkey
        self.__create_system_directories

    def __repr__(self):
        return f"{self.TITLE} {self.MODE} Configuration Object."



class DevelopmentConfig(Config):
    #--- NETWORK ------
    
    #---- RUNTIME ------
    MODE:str = 'Development'
    DEBUG:bool = True



class TestConfig(Config):   
    #--- NETWORK ------
    HOST:str = '127.0.0.1'
    
    #---- RUNTIME ------
    MODE:str = 'Test'
    DEBUG:bool = False



class ProductionConfig(Config): 

    #---  SECURITY -----
    AUTO_ESCAPE:bool = True     
    SERVE_HTTPS:bool = True
    SSL_REDIRECT = True

    #--- NETWORK ------
    CONNECTIONS:int = 10000
    MAX_REQUESTS:int = 1000

    #---- RUNTIME ------
    MODE:str = 'Production'
    DEBUG:bool = False



config = dict(
    default = Config(),
    dev = DevelopmentConfig(),
    test = TestConfig(),
    pro = ProductionConfig(),

)
