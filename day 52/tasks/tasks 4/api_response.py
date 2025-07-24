def ApiResponse(status, message=None, data=None):
    return {
        "status": status,
        "message": message,
        "data": data
    }
