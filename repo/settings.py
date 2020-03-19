# port for app by default
default_app_port = 8000

# size of rsa
rsa_size = 4096

# database_url
"""
    I know, it's not secure. But my laziness makes me do this way.
    If there was real project, I will store these data in os.environ.
"""
DATABASE_URL = 'mysql+pymysql://yqrvdUwQ4x:jsuBY9J0am@remotemysql.com:3306/yqrvdUwQ4x'
