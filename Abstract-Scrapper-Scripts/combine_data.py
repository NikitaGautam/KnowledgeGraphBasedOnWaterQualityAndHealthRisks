#The following code converts the collected abstracts from different keywords into a single file removing the duplicates
import pandas
import os, glob
import time
import csv
import argparse 
import numpy as np

def combine_unique_data():
    url_list = set()
    count = 0 
    files = os.listdir(rootdir)
    for filename in files:
        if ".csv" in filename:
            print(filename)
            pd = pandas.read_csv(rootdir+filename)
            f = open(outdir, 'a')
            for row in pd.itertuples():
                data = row[4]
                url = row[3]
                if data and data is not np.nan:
                    if url not in url_list:
                        url_list.add(url)
                        f.write(str(data))
                        f.write("\n\n")
                    else:
                        count +=1
            f.close()
    

    print("Number of duplicate data found "+ str(count), " URL count ", len(url_list))
    
if __name__ == '__main__':
    rootdir = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.dirname(os.path.abspath(__file__)) 
    parser = argparse.ArgumentParser()
    parser.add_argument("rootdir", help="Full path of the root directory")
    parser.add_argument("outdir", help="Full path of the output directory")
    args = parser.parse_args()
    rootdir = args.rootdir 
    outdir = args.outdir +  "/combined_data_from_keywords.txt" 

 
    combine_unique_data()
    
