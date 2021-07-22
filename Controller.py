import socket
from pydantic import BaseModel
from time import gmtime, strftime
from Messages import MessagesController

class RequestData(BaseModel):
    objects: list
    script_name: str
    user_config_name: str
    devices: list


class Controller:
    message_ctrl = MessagesController()
    def __init__(self):
        pass

    def service_info(self):
        return f"Service running at {socket.gethostbyname(socket.gethostname())}"

    def upload_info(self, req:RequestData):
        if req:
            self.message_ctrl.push_message(f'{req.devices} / {strftime("%Y-%m-%d %H:%M:%S", gmtime())} /  {req.user_config_name} / {req.script_name}')
            return {"time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                    "upload_status":"Script was successfully uploaded"}