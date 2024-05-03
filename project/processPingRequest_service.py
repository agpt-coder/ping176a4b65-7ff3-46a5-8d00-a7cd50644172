from pydantic import BaseModel


class PingRequest(BaseModel):
    """
    Request model for the ping endpoint. This endpoint does not require any input parameters.
    """

    pass


class PingResponse(BaseModel):
    """
    Response model for the ping endpoint. It returns a plaintext message to confirm connectivity.
    """

    message: str


def processPingRequest(request: PingRequest) -> PingResponse:
    """
    This endpoint processes incoming ping requests and responds with 'pong'. Upon receiving a GET request at this path, the Ping Processor Module interacts directly with the API Gateway Module to accept incoming requests. It does not require any input parameters. It is designed to simply respond with a plaintext 'pong' message. This is an essential part of the module to verify connectivity and server responsiveness.

    Args:
    request (PingRequest): Request model for the ping endpoint. This endpoint does not require any input parameters.

    Returns:
    PingResponse: Response model for the ping endpoint. It returns a plaintext message to confirm connectivity.

    Example:
        request = PingRequest()
        response = processPingRequest(request)
        print(response.message)
        > 'pong'
    """
    response = PingResponse(message="pong")
    return response
