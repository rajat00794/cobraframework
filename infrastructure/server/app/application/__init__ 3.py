"""Flask Main Application Setup and globle variables cross apps"""

import os
from pathlib import Path
from typing import Optional
import logging
import logging.config
import yaml
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from infrastructure.server.app.application.service import str_import
from flask_cors import CORS

# Globally accessible libraries
logging.config.dictConfig(yaml.safe_load(open("logging.conf", encoding="utf-8")))
logfile = logging.getLogger("file")
logconsole = logging.getLogger("console")
logfile.debug("Debug FILE")
logconsole.debug("Debug CONSOLE")
info = Info(title="Test API", version="1.0.0")
user_tag = Tag(name="user", description="user")
static_root = (
    Path.joinpath(Path(os.path.dirname(os.path.abspath(__file__))))
    .parent.parent.parent.joinpath("static")
    .joinpath("build")
)


def init_app(config: Optional[str] = None):
    """Initialize the core application."""
    app = OpenAPI(__name__, info=info, instance_relative_config=False)
    CORS(app, origins=["http://localhost:3000"])
    if config is None:
        app.config.from_object("infrastructure.server.app.config.Config")
    else:
        app.config.from_object(config)
    # Initialize Plugins
    with app.app_context():
        # Include our Routes
        # Register Blueprints
        user_bp = str_import(
            "infrastructure.server.app.application.user.routes", "user_bp"
        )
        usersbp = str_import(
            "infrastructure.server.app.application.commands", "usersbp"
        )
        app.register_blueprint(usersbp)
        app.register_api(user_bp)

        return app
