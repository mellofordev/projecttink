from openai import OpenAI
client = OpenAI(api_key='')
instruction_string ='''
You're a friendly assistant named TapAI 
Helping students learn and understand each modules of KTU syllabus 2019 scheme
Youre provided with pdfs of question papers and notes of respective subject 
Give response in detailed point by point manner if needed
'''
files=[]
file = client.files.create(
  file=open("sys_mod1.pdf", "rb"),
  purpose='assistants'
)
# for i in direc:
#   file= client.files.create(
#   file=open(i, "rb"),
#   purpose='assistants')
#   files.append(file.id)
assistant = client.beta.assistants.create(
    instructions=instruction_string,
    model="gpt-3.5-turbo-1106",
    tools=[{"type":'retrieval'}],
    file_ids=[file.id]
)
thread = client.beta.threads.create()
thread_id = thread.id
prompt = input("Prompt >>>")
print(prompt)
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role='user',
    content=prompt
)
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant.id
)
response = client.beta.threads.runs.retrieve(thread_id=thread_id,run_id=run.id)

print(response)