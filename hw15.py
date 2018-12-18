class Router():
    def __init__(self,ip=[],ip_routes=[]):
        self.ip_addresses=ip_addresses
        self.ip_routes=ip_routes
        
    def add_ip_address(self, ip_address):
        self.ip_addresses.append(ip_address)
        return self.ip_addresses

    def add_ip_routes(self, ip_route):
        self.ip_routes.append(ip_route)
        return self.ip_routes

    
