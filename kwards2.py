def show_test_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
show_test_details(
    Test_Name ="Login Test",
    Test_Status ="Passed",
    Browser ="Chrome"
)

