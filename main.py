from google_street_extractor import ImageExtractor
from multiprocessing.dummy import Pool as ThreadPool
import building_database as bdb

def addressResolver(address):
    address = address.replace(","," ")
    address = address.split(" ")
    address = {"zip":address[2],"city":address[3],"street":address[0],"number":address[1]}
    return address

def main():

    #Read addresses
    addresslist = []
    with open('addresses.txt', 'rb') as adr:
        addresslist = adr.read().decode("UTF-8").replace("\n","").replace("\r","").split(";")
    
    #Reed GoogleStretViewAPI key information
    # with open('key.txt', 'r') as f:
    #     key = f.read()
    
    # Key will not be uploaded to git. In production usage of file is advised.
    key = input("Enter Goolge API key: ")

    pool = ThreadPool(8)

    #Loop over addresses and generate ImageExtractor objects to ingest data in pg-database
    def thread_line(address):
        addres_dict = addressResolver(address)
        
        image_object = ImageExtractor(zip=addres_dict["zip"],
                                    city=addres_dict["city"],
                                    street=addres_dict["street"],
                                    number=addres_dict["number"],
                                    key=key)

        #Make a API request
        image_object.get_metadata()

        #Downloade image data as Pillow and NumpyObject
        image_object.get_image()

        # Save to database (see building_database.py)
        bdb.save_building(image_object.zip, image_object.city, image_object.street, image_object.number, image_object.image,image_object.location[0]["pano_id"])


    results  = pool.map(thread_line, addresslist)

    for element in results:
        print(element)

if __name__ == "__main__":
    main()