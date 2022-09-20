from dataclasses import dataclass

from environs import Env


@dataclass
class DjangoConfig:
    secret_key: str
    allowed_hosts: str


@dataclass
class EmailConfig:
    admin: str
    host: str
    host_user: str
    host_password: str
    port: str
    use_tls: str


@dataclass
class DBConfig:
    name: str
    engine: str
    user: str
    password: str
    host: str
    port: str


@dataclass
class Config:
    django: DjangoConfig
    db: DBConfig
    email: EmailConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        django=DjangoConfig(
            secret_key=env.str('SECRET_KEY'),
            allowed_hosts=env.str('ALLOWED_HOSTS')
        ),
        db=DBConfig(
            name=env.str('MYSQL_DB'),
            engine=env.str('MYSQL_ENGINE'),
            user=env.str('MYSQL_USER'),
            password=env.str('MYSQL_PASSWORD'),
            host=env.str('MYSQL_HOST'),
            port=env.str('MYSQL_PORT')
        ),
        email=EmailConfig(
            admin=env.str('EMAIL_ADMIN'),
            host=env.str('EMAIL_HOST'),
            host_user=env.str('EMAIL_HOST_USER'),
            host_password=env.str('EMAIL_HOST_PASSWORD'),
            port=env.str('EMAIL_PORT'),
            use_tls=env.str('EMAIL_USE_TLS'),
        )
    )