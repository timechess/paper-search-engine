import asyncio
import grpc
from paper_search_be.api import PaperSearchServicer
import logging
from paper_search_be.paper_search.v1.paper_search_pb2_grpc import (
    add_PaperSearchServiceServicer_to_server,
)
import json
from utils import json2paper


async def serve() -> None:
    server = grpc.aio.server()
    with open("data/iclr.json", "r") as f:
        papers = list(map(lambda p: json2paper(p), json.load(f)))
    add_PaperSearchServiceServicer_to_server(PaperSearchServicer(papers=papers), server)

    listen_addr = "[::]:7720"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)

    await server.start()
    await server.wait_for_termination()


def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())


if __name__ == "__main__":
    main()
