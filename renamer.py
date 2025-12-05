import os
def main(folder_path):
    print('🤖Enter nothing to skip file!')
    cnt=1
    def InputUntillValid(s):
        while True:
            for i in s:
                if i.isdigit() or i.isalpha() or i=='_' or i=='.':
                    pass
                else:
                    s=input(f'😡Your input has invalid characters "{i}"! Try again: ')
                    break
            else:
                break
        return s
    for file_name in os.listdir(folder_path):
        file_path=os.path.join(folder_path,file_name)
        if not os.path.isfile(file_path):
            continue
        new_file_name=input(f'🤖Rename "{file_name}" to: ')
        if(new_file_name==''):
            continue
        new_file_name=InputUntillValid(new_file_name)
        new_file_path=os.path.join(folder_path,new_file_name)
        os.rename(file_path,new_file_path)
        cnt+=1
    print(f'Done! Converted {cnt-1} file(s) 🙂')