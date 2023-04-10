from domain.entities.user import User

class UserImpl:
    '''User Interface Implementation'''
    cursor : any

    def __init__(self, cursor: any) -> None:
        self.cursor = cursor

    def save(self, user: User) -> None:
        '''Create user'''
        create_user = """
            INSERT INTO users(id_user,username,password,is_staff)
            VALUES(%s,%s,%s,%s);
        """
        try:
            self.cursor.execute(create_user,(
                str(user.id_user),user.username,
                user.password.decode(),user.is_staff)
            )
        except Exception as e:
            pass

    def find_user(self, username: str) -> User or None:
        '''Get user by username'''
        get_user = """
            SELECT id_user, username, password, is_staff FROM users WHERE username=%s;
        """
        self.cursor.execute(get_user, (username,))
        rst = self.cursor.fetchone()

        if rst:
            user = User(id_user=rst[0], username=rst[1], password=rst[2].encode())
            if rst[3]:
                user.set_is_staff()
            return user

        return None
