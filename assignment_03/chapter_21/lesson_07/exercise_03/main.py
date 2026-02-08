# Exercise 3: Union Types with Mixed Values
# Create a dictionary representing a website configuration:
#   - domain (string): "example.com"
#   - port (integer): 8080
#   - ssl_enabled (boolean): True
#   - cache_ttl (integer): 3600
# Use the correct type hint for mixed types. Then access and print each value

website_config : dict[str, str | bool | int] = {
    "domain" : "example.com",
    "port" : 8080,
    "ssl_enabled" : True,
    "cache_ttl" : 3600
}

print(f"Website Configuration: {website_config}")
print(f"Domain: {website_config["domain"]}")
print(f"Port: {website_config["port"]}")
print(f"SSL Enabled: {website_config["ssl_enabled"]}")
print(f"Cache TTL: {website_config["cache_ttl"]}")