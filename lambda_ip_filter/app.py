'''
IP Filter lambda
'''
from lambda_ip_filter.get_ip import getBaseIP


url ='https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de.ipset'

#Read IP from IPset
client_whitelisted_ip = getBaseIP(url)

def lambda_handler(event, context):
    try:
        
        ip_match = []
        non_ip_address_match = []
        ip_array = event["ip_address"]

        for ip in ip_array:
            if ip in client_whitelisted_ip:
                ip_match.append(ip)
            else:
                non_ip_address_match.append(ip)
    
        response = {
            "status": 200,
            "body": {
                "number_of_matching_ip": len(ip_match),
                "number_of_non_matching_address": len(non_ip_address_match),
                "ip_address_match": ip_match,
                "ip_address_non_match": non_ip_address_match
                }
            }
    
        return response
    
    except Exception as e:
        
        response = {
            "status": "500",
            "message": f"An error occured: {str(e)}",
        }