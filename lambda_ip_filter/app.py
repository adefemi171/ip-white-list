'''
IP Filter lambda
'''

#Read IP from IPset
with open('lambda_ip_filter/test.ipset') as f:
    client_whitelisted_ip = [line.replace("\n","") for line in f]

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