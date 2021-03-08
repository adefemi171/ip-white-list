import json

# import requests

# assuming client_whitelist_ip is a sample IP
client_whitelisted_ip = ["192.168.0.1","172.16.254.1"]

def lambda_handler(event, context):
    
    try:
        ip_match = []
        non_ip_address_match = []
        body = event["body"]
        ip_array = body["ip_address"]

        for ip in ip_array:
            if ip in client_whitelisted_ip:
                ip_match.append(ip)
            else:
                non_ip_address_match.append(ip)
    
        return {
            "status": 200,
            "number_of_matching_ip": len(ip_match),
            "number_of_non_matching_address": len(non_ip_address_match),
            "ip_address_match": ip_match,
            "ip_address_non_match": non_ip_address_match
            }
                
    except Exception as e:
        return {
            "status": 500,
            "message": f"An error occured: {str(e)}"
        }
