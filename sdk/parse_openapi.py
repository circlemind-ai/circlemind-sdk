import json
import re
from typing import Dict, List, Optional

NAME = "CirclemindAPI"
VERSION = "0.3.0"

DEFAULT_CONFIG = {
    "servers": [{"url": "https://api.circlemind.co"}],
    "x-speakeasy-retries": {
        "strategy": "backoff",
        "backoff": {
            "initialInterval": 500,
            "maxInterval": 60000,
            "maxElapsedTime": 3600000,
            "exponent": 1.5,
        },
        "statusCodes": ["5XX"],
        "retryConnectionErrors": True,
    },
}

IGNORE_PATHS = {
    "/user": ["get", "post"],
    "/user/demo_api_key": ["post"],
    "/graph/{graph_name}": ["get"],
    "/graph/{graph_name}/stats": ["get"],
    "/get_api_key/{input_key}": ["get"],
}

IGNORE_PARAMERTERS = [
    "increment_usage",
    "demo_allowed",
    "validate_graph_name"
]

IGNORE_SECURITY = [
    "OAuth2PasswordBearer"
]

HTTP_METHOD_TO_PYTHON_METHOD = {
    "get": "get",
    "post": "create"
}

def parse_openapi(openapi_file, ignore_paths: Optional[Dict[str, List[str]]] = None, ignore_parameters: Optional[List[str]] = None, ignore_security: Optional[List[str]] = None):
    with open(openapi_file, "r") as f:
        openapi = json.load(f)
    
    for path, path_config in openapi["paths"].items():
        if ignore_paths and path in ignore_paths:
            for ignore_path in ignore_paths[path]:
                if ignore_path in path_config:
                    path_config[ignore_path]["x-speakeasy-ignore"] = True
        for method, method_config in path_config.items():
            if "security" in method_config and ignore_security:
                method_config["security"] = [
                    security for security in method_config["security"] if tuple(security.keys())[0] not in ignore_security
                ]
            if "security" in method_config and len(method_config["security"]) == 0:
                del method_config["security"]
            
            if "parameters" in method_config:
                for parameter in method_config["parameters"]:
                    if parameter["name"] in ignore_parameters:
                        parameter["x-speakeasy-ignore"] = True
            try:
                summary = method_config["summary"].lower().split(" ")
                method_config["x-speakeasy-name-override"] = HTTP_METHOD_TO_PYTHON_METHOD[summary[0]] + "_" + "_".join(summary[1:])
            except Exception:
                method_config["x-speakeasy-name-override"] = HTTP_METHOD_TO_PYTHON_METHOD[method] + "_" + re.sub(r"{.*?}|", "", path).replace("//", "_").strip("/")
    
    openapi.update(DEFAULT_CONFIG)
    openapi["info"]["title"] = NAME
    openapi["info"]["version"] = VERSION
    
    openapi["components"]["securitySchemes"] = {
        security: openapi["components"]["securitySchemes"][security] for security in openapi["components"]["securitySchemes"] if security not in ignore_security
    }
    
    with open(openapi_file, "w") as f:
        json.dump(openapi, f, indent=2)
        
if __name__ == "__main__":
    parse_openapi("openapi.json", ignore_paths=IGNORE_PATHS, ignore_parameters=IGNORE_PARAMERTERS, ignore_security=IGNORE_SECURITY)
