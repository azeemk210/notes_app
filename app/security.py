from passlib.context import CryptContext

pwsd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwsd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwsd_context.verify(plain_password, hashed_password)
