class MLServerError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ModelNotFound(MLServerError):
    def __init__(self, name: str, version: str):
        msg = f"Model {name} with version {version} not found"
        super().__init__(msg)


class InferenceError(MLServerError):
    def __init__(self, msg):
        super().__init__(msg)
