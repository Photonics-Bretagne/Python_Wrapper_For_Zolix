from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway._send("string")
    test_common.print_result('SendCommand(string)', m)


if __name__ == '__main__':
    test()
