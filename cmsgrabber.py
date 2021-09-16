from Wappalyzer import Wappalyzer
from Wappalyzer import WebPage
import concurrent.futures,warnings,argparse

warnings.filterwarnings("ignore")
header={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}  # header is given to bypass WAF


def analyze_web(urls,output_file):
    dict={}
    cms_found=None
    wapp=Wappalyzer.latest()
    try:
        webpage= WebPage.new_from_url(urls,verify=False,headers=header)
        dict=wapp.analyze_with_categories(webpage)
    except Exception as E:
        pass
    for key,key1 in dict.items():
        for keys,values in key1.items(): 
            if(values[0]=="CMS"):
                #print("{0} : {1}".format(urls,key))
                cms_found=1
                output_file.write(urls+" : "+key+"\n")
                return urls+" : "+key
            else:
               cms_found=None
               continue
    if(cms_found==None):
        return urls+" : No CMS"


 
def file_reading(data,threads,output_file):
    for urls in data:
        urls = urls.strip()
        urls_list.append(urls)
    with concurrent.futures.ThreadPoolExecutor(threads) as executor:
        for urls in urls_list:
            wapp_threads.append(executor.submit(analyze_web,urls,output_file))
        for threads in concurrent.futures.as_completed(wapp_threads):
            print(threads.result()) 

    
def start():	
    parser=argparse.ArgumentParser()
    parser.add_argument("--file_path",required=True, type=str,help="File Path containing URLs" )
    parser.add_argument("--threads",required=False,type=int,help="Number of Threads, Default=3")
    parser.add_argument("--output",required=False,type=str,help="Path to output File , Default=results.txt, Ex: /dir/abc.txt")
    args=parser.parse_args()
    
    if(args.threads):
       threads=args.threads
    else:
       threads=args.threads

    if(args.output):
       output=args.output
    else:
       output="results.txt"
    path=args.file_path
    try:
       input_file=open(path,'r')
    except IOError:
       print("Error: can\'t find file\n")
       exit(0)
    try:
       output_file=open(output,'w')
    except IOError:
       print("Error with the Output file\n")
       exit(0)
    data=input_file.readlines()
    file_reading(data,threads,output_file)
    input_file.close()
    output_file.close()
urls_list = []
wapp_threads=[]
start()
#print(urls_list)
