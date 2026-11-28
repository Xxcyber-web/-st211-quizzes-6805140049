def check_access(role, is_active):
    if role == "admin" and is_active:
        return "granted"
    return "denied"