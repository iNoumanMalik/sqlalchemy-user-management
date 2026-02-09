from app.database import engine
from app.models import Base
from app.database import SessionLocal
from app import crud

Base.metadata.create_all(bing=engine)

db = SessionLocal()

#CREATE
user = crud.create_user(db,"Nomi","nouman@emumba.com")
print(user)

#READ 
users = crud.get_all_users(db)
print(users)

user = crud.get_user_by_email(db,"nouman@emumba.com")
print(user)

#UPDATE
user = crud.update_user_name(db,user.id,"Nouman")

#DELETE
crud.delete_user(db,user.id)

db.close()