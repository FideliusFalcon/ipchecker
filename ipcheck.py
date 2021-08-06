import requests, sys, argparse

def checkIP(ip, method):
    #change this variable to your email address
    contactEmail=""
    #if probability from getIPIntel is grater than this value, return 1
    maxProbability=0.99
    timeout=5.00

    url = "http://check.getipintel.net/check.php?ip=" + ip + "&contact=" + contactEmail + "&flags=" + method + "&format=json"
    result = requests.get(url, timeout=timeout)

    #if (result.status_code != 200) or (float(result.content) < 0):
    #    sys.stderr.write("An error occured while querying GetIPIntel")
    
    return result.json()

def PrintResult(result):
    print("Status:", result["status"])
    print("Scanned IP:", result["queryIP"])
    print("Result:", result["result"])


if __name__ == "__main__":
    # Read arguments
    parser = argparse.ArgumentParser(description='OTX CLI IP Bulk Search')
    parser.add_argument('-ip', help='IP to Scan', required=True)
    parser.add_argument('-method', help='m, b, f. Default = m. Read documentation', required=False)

    args = vars(parser.parse_args())


    if args['method'] == "m" or "b" or "f":
        method = args['method']
    else:
        print("No method input. Uses default instead\n")
        method = "m"

    result = checkIP(args["ip"], method)

    PrintResult(result)