import pytest
from base.base_analyze import analyze_with_file


class TestLogin:

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login1"))
    def test_login1(self,args):
        username = args["username"]
        password = args["password"]
        print(username)
        print(password)

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login2"))
    def test_login2(self, args):
        username = args["username"]
        password = args["password"]
        print(username)
        print(password)

