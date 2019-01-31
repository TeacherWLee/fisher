from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from fisher import app

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://root:7insummer@localhost/fisher'

from app.models import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
