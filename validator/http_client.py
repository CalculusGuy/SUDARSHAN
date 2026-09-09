# validator/http_client.py
import requests
import urllib3
from typing import Optional, Dict, Any

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SafeHTTPClient:
    """Safe HTTP client for validation with configurable parameters."""
    
    def __init__(self, timeout: int = 10, verify: bool = False, allow_redirects: bool = True):
        self.timeout = timeout
        self.verify = verify
        self.allow_redirects = allow_redirects
        self.session = requests.Session()
        
    def request(self, method: str, url: str, params: Optional[Dict] = None, 
                data: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Make an HTTP request with safe defaults."""
        
        if headers is None:
            headers = {}
            
        headers.setdefault("User-Agent", "SUDARSHAN-Validator/1.0")
        
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                params=params,
                data=data,
                headers=headers,
                timeout=self.timeout,
                verify=self.verify,
                allow_redirects=self.allow_redirects
            )
            return response
        except requests.RequestException as e:
            raise Exception(f"HTTP request failed: {str(e)}")
    
    def get(self, url: str, params: Optional[Dict] = None) -> requests.Response:
        return self.request("GET", url, params=params)
    
    def post(self, url: str, data: Optional[Dict] = None) -> requests.Response:
        return self.request("POST", url, data=data)