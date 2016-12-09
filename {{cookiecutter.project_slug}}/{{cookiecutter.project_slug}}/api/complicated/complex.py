import datetime


def get():
    # Returns a complex result.
    response = {
        "text": "This a text",
        "number": 1234,
        "specialText": "A long enough text",
        "specialNumber": 12,
        "good": True,
        "createdAt": datetime.datetime.utcnow(),
        "aNiceList": ["Element One", "Element Two"],
        "aNestedObject": {
            "iAmNested": "Just a text in a nested dict."
        }
    }
    return response, 200