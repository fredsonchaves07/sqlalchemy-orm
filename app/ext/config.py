from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.toml"],
    envvar_prefix=False,
    environments=True,
    load_dotenv=True,
)
