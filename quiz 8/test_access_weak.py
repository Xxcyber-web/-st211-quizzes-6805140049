from access import check_access
def test_admin_active():
    assert check_access(role="admin",is_active=True)== "granted"
def test_user_inactive():
    assert check_access(role="user",is_active=False) == "denied"    