class Config:

    _config = None

    @classmethod
    def load_config(cls, config):
        if config:
            cls._config = config

    @classmethod
    def get_config(cls):
        if cls._config:
            return cls._config
        