import logging
from contextlib import asynccontextmanager

import project.processPingRequest_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(title="ping", lifespan=lifespan, description="simple ping server")


@app.get("/ping", response_model=project.processPingRequest_service.PingResponse)
async def api_get_processPingRequest(
    request: project.processPingRequest_service.PingRequest,
) -> project.processPingRequest_service.PingResponse | Response:
    """
    This endpoint processes incoming ping requests and responds with 'pong'. Upon receiving a GET request at this path, the Ping Processor Module interacts directly with the API Gateway Module to accept incoming requests. It does not require any input parameters. It is designed to simply respond with a plaintext 'pong' message. This is an essential part of the module to verify connectivity and server responsiveness.
    """
    try:
        res = project.processPingRequest_service.processPingRequest(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
