import json
import socket
from pydantic import BaseModel
from time import gmtime, strftime
from RedisSender import Redis
import auth.auth_handler
class RequestData(BaseModel):
    user_token: str
    objects: list
    script_name: str
    user_config_name: str
    devices: list


class Controller:
    message_ctrl = Redis()
    def __init__(self):
        pass

    def service_info(self):
        return f"Service running at {socket.gethostbyname(socket.gethostname())}"

    def upload_info(self, req:RequestData):
        if req:
            token = auth.auth_handler.signJWT(req.user_token)
            data = {
                "type": "script-creation",
                "devices": req.devices,
                "time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                "config_name": req.user_config_name,
                "script_name": req.script_name,
                "token": req.user_token
            }
            self.message_ctrl.send_data(json.dumps(data))
            return {"time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                    "upload_status":"Script was successfully uploaded", "acess_token": token}