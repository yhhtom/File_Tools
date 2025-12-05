import os
def main(folder_path):
    cnt=1
    new_ext=input('🤖Type the new extension here: ')
    avoid_same_name=1
    while new_ext[0] != '.':
        new_ext=input('😡Invalid input! Extension must starts with a ".", try again: ')
    for file_name in os.listdir(folder_path):
        file_path=os.path.join(folder_path,file_name)
        if not os.path.isfile(file_path):
            continue
        name_without_tail,_=os.path.splitext(file_name)
        if _==new_ext:
            continue
        new_file_name=name_without_tail+new_ext
        while os.path.exists(os.path.join(folder_path,new_file_name)):
            new_file_name=name_without_tail+f'({avoid_same_name})'+new_ext
            avoid_same_name+=1
        new_file_path=os.path.join(folder_path,new_file_name)
        os.rename(file_path,new_file_path)
        cnt+=1
    print(f'Done! Converted {cnt-1} file(s) 🙂')