import building_database as bdb
import matplotlib.pyplot as plt

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
    
    for address in addresslist:
        addres_dict = addressResolver(address)
        
        id, pp, zip, city, street, num, ts, gid, pic = bdb.open_building(addres_dict["zip"], addres_dict["city"], addres_dict["street"], addres_dict["number"])
        print(id + "; " + pp + "; " + str(zip) + "; " + city + "; " + street + "; " + str(num) + "; " + str(ts) + "; " + gid)
        plt.imshow(pic)
        plt.show()


if __name__ == "__main__":
    main()