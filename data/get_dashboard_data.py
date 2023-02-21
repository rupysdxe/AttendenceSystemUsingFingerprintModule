from GoogleSheet import get_logs


# returns
# 1. Name
# 2. Check inDate
# 3. Check outDate
# 4. Status - Attended  and Attending
# 5. Professor

def get_data():
    data = list(dict())
    logs = get_logs()
    print(logs)
    return data


get_data()
