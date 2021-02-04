import string
import secrets


def gen_checking_code() -> str:
    # Gen alphabet for generate code
    alphabet: str = string.ascii_letters + string.digits

    code: str = ''.join(secrets.choice(alphabet) for i in range(5))

    return code
