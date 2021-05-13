from dataclasses import dataclass
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

# dataclass 데코레이터 이유: 해당 클래스를 Dict 형태로 추출해서 사용 가능
@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    # postgresql://federer:grandestslam@localhost:5432/tennis
    # user, password, host, port, db
    DB_URL: str = "postgresql://iztbj:1234@192.168.21.204:2345/pidb"

    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False

    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]

# @dataclass
# class PathConfig(Config):
#     # Folder path
#     SAMPLE_FOLDER_PATH = r'D:\\Project\\tesseract\\sample\\'
#     TRAIN_FOLDER_PATH = r'D:\\Project\\tesseract\\tesseract_Project\\Scripts\\tp\\ml\\train\\'

#     # File path
#     KEYWORD_DICTIONARY_PATH = r'D:\\Project\\tesseract\\tesseract_Project\Scripts\\tp\\nlp\\dic.txt'
#     DEFAULT_CSV_PATH = r'D:\\Project\\tesseract\\tesseract_Project\\Scripts\\tp\\ml\\train\\model.csv'

#     # Save h2o model
#     H2O_MODEL_PATH = r'D:\\Project\\tesseract\\model'

#     USING_MODEL_PATH = H2O_MODEL_PATH + '/GBM_1_AutoML_20210324_171907'


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))

# print(asdict(LocalConfig()))

