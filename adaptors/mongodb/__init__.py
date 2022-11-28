import mongodb
from mongodb import errors, mongoadaptor, config, dependency_common_utilities


di_args = [
    ("client", mongodb.utils.AsyncMoter),
    ("engine", mongodb.utils.AsyncEngine),
    ("config", mongodb.config.Config),
    ("dbmanager", mongodb.mongoadaptor.DataBaseManager),
]


__all__ = ["errors", "di_args", "mongoadaptor", "config", "dependency_common_utilities"]
