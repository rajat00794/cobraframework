import mongodb

di_args = [
    ("client", mongodb.utils.AsyncMoter),
    ("engine", mongodb.utils.AsyncEngine),
    ("config", mongodb.config.Config),
    ("dbmanager", mongodb.mongoadaptor.DataBaseManager),
]
