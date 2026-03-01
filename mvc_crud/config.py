class Config:
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"  # la que usas en Workbench
    MYSQL_HOST = "localhost"
    MYSQL_PORT = "3307"
    MYSQL_DB = "mvc_crud"

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False