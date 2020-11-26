import os
import pandas as pd
import time

def main():
    while True:
        time.sleep(3600)
        delete_extra_file()
def delete_extra_file():
    restart_names = []
    file_dataframe = pd.DataFrame(columns=['file_creat_time', 'file_name'])
    file_names = os.listdir()
    for file_name in file_names:
        if file_name.find('restart_flow') != -1:
            restart_names.append(file_name)
    if len(restart_names) > 5:
        for files in restart_names:
            file_dataframe = file_dataframe.append({'file_creat_time':os.path.getctime(files), 'file_name': files}, ignore_index=True)

    file_dataframe = file_dataframe.sort_values(by='file_creat_time', ascending=True, ignore_index=True)
    delete_files = file_dataframe.loc[0:file_dataframe.shape[0]-5]['file_name'].values
    for file_delete in delete_files:
        os.remove(file_delete)

if __name__ == '__main__':
    main()