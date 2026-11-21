def log_test_result(**kwargs):
    print("Test:", kwargs.get("test_name"))
    print("Status:", kwargs.get("status"))
log_test_result(test_name="login", status ="Passed")
log_test_result(test_name="payment", status ="failed")