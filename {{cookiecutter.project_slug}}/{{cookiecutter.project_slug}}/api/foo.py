
def post(request):
    # 'request' is a dictionary containing the parameters defined in
    # config/api.yml and validated by connexion.

    # Return always a tuple of an object that validates under the schema
    # defined in the config/api.yml and an HTTP status code.
    # 200 = Everything good, 404 = Not found, 500 = Server error
    return {
        "returnData": request.get("data", ""),
    }, 200


def get():
    return {
        "bar": True
    }, 200
