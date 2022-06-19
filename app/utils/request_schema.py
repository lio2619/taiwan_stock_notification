def check_request_json_schema(request_schema, json_body):
    response_body = []

    if json_body == None:
        return True, request_schema

    for parameter in request_schema:
        if parameter not in json_body:
            response_body.append(parameter)

    if len(response_body) > 0:
        return True, response_body

    return False, response_body