import os
def main(folder_path):
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
    while True:
        name=input('🤖Enter nothing to stop, enter the file name here: ')
        if name=='':
            break
        name=InputUntillValid(name)
        with open(name,'w') as f:
            pass
        cnt+=1
    print(f'Done! Converted {cnt-1} file(s) 🙂')