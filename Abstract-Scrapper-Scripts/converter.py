
#The following code extracts Texts from PDF files
import os, glob
import pdftotext
import argparse

def convert_pdf_to_text():    
    count = 0
    errored = 0

    for filename in glob.iglob(rootdir, recursive=True):
        if os.path.isfile(filename):
            try:
                with open(filename, "rb") as f:
                    pdf = pdftotext.PDF(f)
                
                out = outdir +  os.path.basename(os.path.splitext(filename)[0]) + ".txt"
            
                with open(out, 'w') as f:
                    f.write("\n\n".join(pdf))
                count +=1
            
            except Exception as e:
                print ("Error occured in processing file: "+ filename)
                print("Error: " + str(e))
                errored +=1 
                continue
            
    print("Conversion completed")
    print("Number of files processed: "+ str(count))
    print("Processing terminated for " + str(errored) + " files")


if __name__ == '__main__':
    rootdir = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument("rootdir", help="Full path of the root directory")
    parser.add_argument("outdir", help="Full path of the output directory")
    args = parser.parse_args()
    rootdir = args.rootdir + "/*"
    outdir = args.outdir 
    pdftotext()
