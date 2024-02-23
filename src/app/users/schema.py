from pydantic import Field, BaseModel

class UserSchema(BaseModel):
    username: str = Field(description="username")
    password: str = Field(description="password")

class ShowUserSchema(BaseModel):
    username: str = Field(description="username")
    id:int = Field(description="Unique users id")

    class Config():
        from_attributes=True
