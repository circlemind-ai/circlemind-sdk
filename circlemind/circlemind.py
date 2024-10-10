import requests
from requests.adapters import HTTPAdapter, Retry
import time
import logging

# Custom Exceptions
class CirclemindError(Exception):
    """Base class for exceptions in the Circlemind API."""
    pass

# Circlemind API Client
class Circlemind:
    REQUEST_RETRY_LIMIT = 5
    REQUEST_RETRY_DELAY_SECONDS = 1
    REQUEST_RETRY_DELAY__INCREMENT_SECONDS = 1

    def __init__(self, api_key: str, base_url: str = "https://api.circlemind.co"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {'apiKey': self.api_key}
        logging.basicConfig(level=logging.INFO)
        
        retry_config = Retry(total=self.REQUEST_RETRY_LIMIT, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504], raise_on_status=False)
        self.request_session = requests.Session()
        self.request_session.mount('https://', HTTPAdapter(max_retries=retry_config))

    def add(self, memory: str, memory_id: str = None):
        """Add a new memory."""
        url = f"{self.base_url}/memory"
        payload = self._create_memory_payload(memory, memory_id)
        
        response = self._send_post_request(url, payload)
        return response
    
    def configure(self,  prompt: str, example_queries: str):
        self._configure(prompt=prompt, example_queries=example_queries)

    def query(self, query: str):
        """Retrieve a list of memories based on a query."""
        url = f"{self.base_url}/reasoning"
        payload = self._create_query_payload(query)
        
        response = self._send_post_request(url, payload)
        memories = self._wait_for_response(response)
        
        return memories
    
    def _configure(self, prompt: str, example_queries: str):
        """Retrieve a list of memories based on a query."""
        try:
            url = f"{self.base_url}/configure"
            payload = self._create_configure_payload(prompt=prompt, example_queries=example_queries)
            self._send_post_request(url, payload)
        except:
            raise CirclemindError("Something went wrong during configuration.")
    
    def _create_configure_payload(self, prompt: str, example_queries: str):
        """Create payload for querying memories."""
        return {"domain": prompt, "exampleQueries": example_queries}

    def _create_memory_payload(self, memory: str, memory_id: str):
        """Create payload for adding memory."""
        return {"memory": memory, "memoryId": memory_id}

    def _create_query_payload(self, query: str):
        """Create payload for querying memories."""
        return {"query": query}

    def _send_post_request(self, url: str, payload: dict):
        """Send a POST request to the given URL with the provided payload."""
        try:
            response = self.request_session.post(url, json=payload, headers=self.headers)
            return response.json()
        except requests.HTTPError as e:
            logging.error(f"Failed to send POST request: {e}")
            
            raise CirclemindError(f"Error adding memory: {str(e)}")

    def _wait_for_response(self, initial_response):
        """Poll the API until the memory processing is done."""
        status = "CREATED"
        request_id = initial_response.get("requestId")
        request_time = initial_response.get("requestTime")

        while status not in ["DONE", "FAILED"]:
            logging.info("Waiting for response...")
            time.sleep(1)
            response = self._send_get_request(request_id, request_time)
            status = response.get("status", "")
        
        if status == "FAILED":
            raise CirclemindError("Fetching memories failed.")

        return response.get("memories", "")

    def _send_get_request(self, request_id: str, request_time: str):
        """Send a GET request to check the status of the processing."""
        url = f"{self.base_url}/reasoning"
        params = {"requestId": request_id, "requestTime": request_time}
        
        try:
            response = self.request_session.get(url, params=params, headers=self.headers)
            return response.json()
        except requests.HTTPError as e:
            logging.error(f"Failed to send GET request: {e}")
            
            raise CirclemindError(f"Error adding memory: {str(e)}")
