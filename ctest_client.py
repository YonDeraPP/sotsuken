from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683
path ="basic/"

client = HelperClient(server=(host, port))
payload = open("./image.jpg", "rb").read().encode('base64')
response = client.get (path=path)
print(response.pretty_print())
client.stop()