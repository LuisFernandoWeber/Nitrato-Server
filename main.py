import argparse

from core.database import db
from pony.orm import db_session
from models import *




db.generate_mapping(create_tables=False)



def main():
    print("Iniciando execução do sistema")

   


if __name__ == "__main__":
    main()
