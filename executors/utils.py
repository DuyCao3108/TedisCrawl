import os


def from_dirname_to_fullpath(scrape_out_dirname):
    return f"./storage/{scrape_out_dirname}/data.json"

def from_dirname_to_storagepath(scrape_out_dirname): 
    return f"./storage/{scrape_out_dirname}/generated/gen.pkl"

def from_dirname_to_uploaddir(scrape_out_dirname): 
    return os.path.join(os.getcwd(), f"storage/{scrape_out_dirname}/")

