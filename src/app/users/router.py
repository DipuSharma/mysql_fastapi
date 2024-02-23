from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from src.database.modals import User
from src.database.db_config import get_db
from src.app.users.schema import UserSchema, ShowUserSchema

router = APIRouter()

@router.get("/", name="All Users")
async def user_list_view(db: Session = Depends(get_db)):
    user_list = db.query(User).order_by(User.id.desc()).all()
    if user_list:
        return [ShowUserSchema.from_orm(user) for user in user_list]
    else:
        return "Record not found"
    
@router.post("/", name="Create user")
async def add_users(payload: UserSchema, db:Session = Depends(get_db)):
    existed_user = db.query(User).filter(User.username == payload.username).first()
    if existed_user:
        raise HTTPException(status_code=status.HTTP_226_IM_USED, detail="User existed")
    data = User(**payload.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return ShowUserSchema.from_orm(data)



