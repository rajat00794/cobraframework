from . import routes, service


dependency_modules = ["user"]
dependency_adaptors = ["mongodb", "sms_service", "email_service"]
dependency_common_utilities = [True]
