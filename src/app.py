from fastapi import FastAPI, APIRouter
import uvicorn
from utils.utils_methods import Utils
from utils.db_utils import DatabaseManager
from api_entrypoint import ApiEntrypoint
from contextlib import asynccontextmanager, contextmanager
from starlette.concurrency import run_in_threadpool


class MainEntryPoint:


    def __init__(self, config):
        self.config = config
        self.app = FastAPI(title='FastAPI_Learning', lifespan=lambda app1 : lifespan(app1, config))
        self.add_endpoints()

    
    def add_endpoints(self):
        ApiEntrypoint(self.app)


@asynccontextmanager
async def lifespan(app, config):
    try:
        # Run synchronous methods in a thread pool
        await run_in_threadpool(DatabaseManager.initialize_connection, config)
        # logging.info('Database Connection Initialized Successfully')

        # Yield control for FastAPI to proceed with the application lifecycle
        yield
    except Exception as e:
         pass


def main(config_filepath='D:\\Fastapi_project\\config.json'):
    config = Utils.read_config_file(config_filepath)
    entrypoint = MainEntryPoint(config)
    app = entrypoint.app
    uvicorn.run(app=app, host = config['uvicorn']['host'], port = config['uvicorn']['port'])

main()
