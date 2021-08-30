from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # hashing the Password


class HashingPassword:

    def bcrypt(password: str):
        return pwd_context.hash(password)


