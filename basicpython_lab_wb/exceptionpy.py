while True:
    try:
        n = int(input("Please enter integer"))
        m = int(input("Please enter integer"))
        z = n/m
        break

    except Exception as e:
        print("not an integer, please again 123")
        print(e)
    except ValueError:
        print("not an integer, please again 456")
    finally:
        print("you successfully entered an integer")