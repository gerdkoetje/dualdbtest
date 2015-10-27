class SecondRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'seconddbapp':
            return 'seconddb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'seconddbapp':
            return 'seconddb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'seconddbapp' and obj2._meta.app_label == 'seconddbapp':
            return True
        elif 'seconddbapp' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, model):
        if db == 'seconddb' or model._meta.app_label == "seconddbapp":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True