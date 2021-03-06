from test_helper import run_common_tests, failed, passed, get_file_output


def test_outputs():

    outputs = get_file_output()
    if len(outputs) < 3:
        failed(message='Please reset the file and try again')

    if outputs[-3:] == ['R LIWVIVW VRTSG KRAAZH', 'DV ZIV VCKVXGRMT TFVHGH', 'GSVB OLEV KRAAZ']:
        passed()
    else:
        failed(message='Please try again.')

if __name__ == '__main__':
    run_common_tests()
    test_outputs()
