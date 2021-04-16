import os
import random
import shutil
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

_ = '''
target_num_folders = 0
target_num_files = 0
cur_num_folders = 0
cur_num_files = 0


def make_sub_folders(num_folders, num_files)
    if num_folders == 0 or num_files == 0:
        return
    new_num_folders = random.randint(1, num_folders)
    for i in range(new_num_folders):
        
        
    make_sub_folders(num_folders-1, num_files)
    pass


def make_random_folders(root, num_folders, num_files):
    global target_num_folders, target_num_files, cur_num_folders, cur_num_files
    target_num_folders, target_num_files, cur_num_folders, cur_num_files = num_folders, num_files, 0, 0
'''


total_folder_count = 0




def make_single_folder():
    global total_folder_count

    total_folder_count += 1
    folder_name = 'folder%04d' % total_folder_count
    os.mkdir(folder_name)
    print('make ', folder_name)
    logging.info('folder %s is created' % folder_name)
    return folder_name


root_folder = 'ScriptTestFolder'
ext_list = [
    'doc', 'ppt', 'py', 'pdf', 'hwp',
    'txt', 'cpp', 'h', 'htm', 'mov',
    'mp4', 'avi', 'dll', 'jpg', 'png',
    'tmp', 'zip', 'bin', 'bat', 'gif'
]



def make_subfolder(count):

    cur_folder = make_single_folder()
    count -= 1
    if count == 0:
        return

    os.chdir(cur_folder)

    # creat new sub folders
    while True:
        subfolder_count = random.randint(1, count)
        make_subfolder(subfolder_count)
        count -= subfolder_count
        if count == 0:
            break

    # fill this folder with random files
    random_files = ['file%03d.%s' % (i, ext_list[random.randint(0, 19)]) for i in range(random.randint(5,20))]
    for file in random_files:
        f = open(file, 'w')
        f.write('Auto Generated File')
        f.close()


    os.chdir('..')


def make_random_folders(count):
    global total_folder_count
    total_folder_count = 0

    # if same name root exist, remove it
    if os.path.exists('folder0001'):
        shutil.rmtree('folder0001')

    make_subfolder(count)

make_random_folders(100)












