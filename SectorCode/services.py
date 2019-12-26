from zeep import Client
import json
import xmltodict

def get_books(UserID='all'):
    client = Client(wsdl = 'http://dev.usbooking.org/us/UnitedSolutions?wsdl')
    data = client.service.SectorCode(UserID)
    result = json.loads(json.dumps(xmltodict.parse(data)))['FlightSector']['Sector']
    return result
