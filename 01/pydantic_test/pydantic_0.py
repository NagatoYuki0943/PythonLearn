from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, lt=120)


class UserResponse(BaseModel):
    id: int
    user: User

global_id = 1  # 全局ID

def create_user(user: User) -> UserResponse:
    global global_id
    # 模拟创建用户的逻辑
    user_response = UserResponse(id=global_id, user=user)
    global_id += 1

    return user_response


# 使用函数
new_user = User(name="jerry", age=8)
response = create_user(new_user)
print(response)
# id=1 user=User(name='jerry', age=8)

# gender 是多余的, 所以不会被赋值, 但是不会报错
new_user = dict(name="Tom", age=10, gender="male")
response = create_user(new_user)
print(response)
# id=2 user=User(name='Tom', age=10)

# gender 是多余的, 所以不会被赋值, 但是不会报错
new_user = User(name="Dog", age=11, gender="male")
response = create_user(new_user)
print(response)
# id=3 user=User(name='Dog', age=11)

# 报错, 数据不足
# new_user = dict(name="Duck")
# response = create_user(new_user)
# print(response)

# 报错, 数据类型错误
# new_user = "Any"
# response = create_user(new_user)
# print(response)
