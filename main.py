import My_File_Tools
import os
from colorama import init,Fore,Style
init()
print(Fore.GREEN+'PD20W File Tools ver. 0.0.1'+Style.RESET_ALL)
folder_path=input(Fore.CYAN+'Enter nothing to use the default Input folder, or enter your folder path: '+Style.RESET_ALL)
current_folder=os.path.dirname(os.path.abspath(__file__))
if(folder_path==''):
    folder_path=os.path.join(current_folder,'Input')
while not os.path.exists(folder_path):
    folder_path=input('Path not found! Please try again')
while os.path.isfile(folder_path):
    folder_path=input('This is not a folder! Please try again')
print('Enter "quit" to quit')
tools_list=[
'extension_converter', 
'massive_renamer',
'file_creator'
]
while True:
    operation=input(Fore.CYAN+'Welcome! Enter the tool name or number to use it! Enter "tools" to see all the tools: '+Style.RESET_ALL)
    if operation.isdigit():
        operation=tools_list[int(operation)-1]
    if operation=='quit':
        break
    try:
        tool_module = getattr(My_File_Tools, operation)
        main_func = getattr(tool_module, 'main')
        main_func(folder_path)
    except AttributeError:
        print(f"Error: Tool '{operation}' not found in My_File_Tools, please try again!")
    except Exception as e:
        print(f"Error running tool: {e}, please try again!")
print(Fore.GREEN+'See you again!'+Style.RESET_ALL)