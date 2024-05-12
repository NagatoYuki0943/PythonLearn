from typing import NewType


UserId1 = int
AttachPoint1 = int

class Player1:
    def __init__(
        self,
        user_id: UserId1,
        attach_point: AttachPoint1
    ) -> None:
        self.user_id = user_id
        self.attach_point = attach_point

    def update_attack_point(self, point: AttachPoint1) -> None:
        self.attach_point = point
        # self.user_id = point 这样写是错误的,但是检查不出来,因为类型都是 int


# 建立一个新的 Type
UserId2 = NewType("UserId2", int)
AttachPoint2 = NewType("AttachPoint2", int)

class Player2:
    def __init__(
        self,
        user_id: UserId2,
        attach_point: AttachPoint2
    ) -> None:
        self.user_id = user_id
        self.attach_point = attach_point

    def update_attack_point(self, point: AttachPoint2) -> None:
        self.attach_point = point

# 这样会被检查出来,因为 user_id 和 attach_point 不是 int 类型
player1 = Player2(1, 2)
# 需要显示更改类型才能通过检查
player2 = Player2(UserId2(2), AttachPoint2(3))
