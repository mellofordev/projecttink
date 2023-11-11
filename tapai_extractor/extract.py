# Confidential tool 
# mello,inc 2023
# Doc helper : used to extract and get clean textual data from the pdfs
# access to only 2

from pypdf import PdfReader
import google.generativeai as cleaner
import os
from dotenv import load_dotenv

load_dotenv()
apikey= os.getenv("API_KEY")
cleaner.configure(api_key=apikey)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.6,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}


file_bucket=[]
for root_,dir_,files_ in os.walk(os.getcwd()):
    for filename in files_:
        if filename.endswith(".pdf"):
            file_bucket.append(filename)

for file_ in file_bucket:

    reader = PdfReader(file_)
    pages= len(reader.pages)
    init=0
    cleaned_bucket=[]
    helper_text=' remove all headers,footers,like computer science engineering,downloaded form ktunotes.in,all unwanted numbers,make data clean ,readable,remove all unwanted numbers'
    print("Current file --->",file_)
    for i in range(pages):
        print(f"cleaning page---> {init}")
        response = cleaner.generate_text(**defaults,prompt=reader.pages[i].extract_text()+helper_text)
        cleaned_bucket.append(response.result)
        init+=1
        print("---------------------------------")
    new_file_ = file_.split(".")[0]
    with open(f"cleaned_{new_file_}.txt","w") as filestream:
        for cleaned_text in cleaned_bucket:
            if cleaned_text!=None:
                filestream.write(cleaned_text)
    print(f"Finished cleaning the file {file_} check the clean_{new_file_}.txt")
