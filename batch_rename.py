import os

# to be replaced string and file extension filter
search = "file"
replace = "document"
folder = "new_folder"
type_filter = ".py"


# get all files from current directory 
dir_content = os.listdir(folder)
docs = [os.path.join(folder,doc) for doc in dir_content if os.path.isfile(os.path.join(folder, doc))]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files.")

#go through all the files and check if they match the search pattern
for doc in docs:
  #check if search text is in doc name 
  if search in doc:
    
    #replace with the given text 
    new_name = doc.replace(search, replace)
    os.rename(doc, new_name)
    renamed += 1
    
    print(f"Renamed file {doc} to {new_name}")
    
print(f"Renamed {renamed} of {len(docs)} files.")