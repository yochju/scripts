import os, sys
# from os import listdir
# from os.path import isfile, join, dirname
# from os import walk
# from pathlib import Path

# inputFile = sys.argv[-1]
# root_dir = "/c/projects/uasr-data/izfp-simultrain/common/sig/Z02"
# path = os.path.join(root_dir, "Z01")
# cwd = os.getcwd()

# cwd = "/home/yon47118/project/uasr-data/wildlife/train-class04-aug"
cwd = "/home/yon47118/project/uasr-data/wildlife/valid-class04-aug"

# outputFile = "train-deer-fight-bing01-all.txt"
# outputFile = "train-wildlife04-all.txt"
# outputFile = "valid-wildlife04-all.txt"

# outputFile = "train-wildlife04-sp-clouds.txt"
outputFile = "valid-wildlife04-sp-clouds.txt"

jpg = "jpg"

noise = ['sp', 'addPoissonNoise']
weather = ['clouds', 'fog', 'corrupt-fog-sev01', 
                            'corrupt-fog-sev02', 
                            'corrupt-fog-sev03', 
                            'corrupt-fog-sev04', 
                            'corrupt-fog-sev05']
# noise_weather = []
exclude = ['lists-backup']
selectedDirs = ['clouds', 'sp','clouds-sp_0.3']
# selectedDirs = ['cloud', 'fog', 'sp']
visitingDirs = []


def getVisitingDirs():
    import itertools
    combinedDirs = list(map('-'.join, itertools.product(noise, weather)))
    visitingDirs = noise + weather + combinedDirs 
    print("visitingDirs", visitingDirs)
    return visitingDirs

# print('path', path)
# file_set = set()
# for dir_, _, files in os.walk(root_dir):
#     for file_name in files:
#         rel_dir = os.path.relpath(dir_, root_dir)
#         print('rel_dir', rel_dir)
#         rel_file = os.path.join(rel_dir, file_name)
#         print('rel_file', rel_file)
#         file_set.add(rel_file)


# for subdir, dirs, files in os.walk(root):
#     for file in files:
#         # print ('subdir', os.path.join(subdir, file))
#         print ('subdir', subdir)
#         print ('file', file)
#         filepath = subdir + os.sep + file

#         if filepath.endswith(".html"):
#             print (filepath)

def last_3digits(x):
    print("x[3:5]: ", x[3:6])
    return x[3:6]

file_list = []
def getAllFiles(dir):
    # dir = os.path.join(dir, selectedDirs)
    # print("dir", dir)
    for path, subdirs, files in os.walk(dir):
        subdirs[:] = [dir for dir in subdirs if dir in selectedDirs and 
                                                dir not in exclude and 
                                            not dir.startswith('.')]
        print("subdirs: ", subdirs)
        for file in files:
            if (file.endswith(".txt") and 
                not file.startswith("class") and
                not file.startswith("train")):

                full_name = os.path.join(path, file)
                pre, ext = os.path.splitext(full_name)
                print('pre: ', pre)
                print('ext: ', ext)
                # new_name = os.rename(full_name, pre + jpg)
                # print('new_name: ', os.rename(full_name, pre + jpg))
                # full_name = full_name[:-3] + jpg
                file_name_jpg = pre + '.' + jpg
                print("file_name_jpg: ", file_name_jpg)
                file_list.append(os.path.join(path, file_name_jpg))
    
    for item in sorted(file_list):
        print("item: ", item)
    
    return file_list
    

def writeFileLists(file_list):
    with open(outputFile, 'w') as outFile:
        for item in sorted(file_list):
            outFile.write(item + '\n')

location = os.getcwd()
files_in_dir = []

def test():
    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in f:
            if '.txt' in item:
                files_in_dir.append(os.path.join(r, item))

    for item in sorted(files_in_dir):
        print("file in dir: ", item)


def old():
    # flst_path=[]
    with open(outputFile, 'w') as outFile:
        # listOfFiles = list()
        # for (dirpath, dirnames, filenames) in os.walk(cwd):
        #     listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        #     print("listOfFiles: ", listOfFiles)
        
        for path, subdirs, files in os.walk(cwd):
        # for path, subdirs, files in os.walk('.'):        
            # flst_data1 = ""
            # flst_data = ""
            #files.sort(key=lambda f: int(filter(str.isdigit, f)))
            #sorted(files, key=last_3digits)
            print("files: ", files)
            # print("os.listdir(): ", os.listdir())
            for file in sorted(files):
                # print (os.path.join(subdirs, files))

                if (file.endswith(".txt") and 
                    not file.startswith("class") and
                    not file.startswith("train")):

                    print('path: ', path)
                    print('file_name: ', file)
                    full_name = os.path.join(path, file)
                    print("full_path + file_name: ", full_name)

                #if (file_name[-3:] == 'jpg'):            
                    # print('file_name[:6]: ', file_name[:5])
                    #print('file_name[:-3]: ', file_name[:-3])
                #    if (os.path.isfile(file_name[:-3] + 'txt')):
                    # base = os.path.split(file)                
                    # file = file[:-3] + ext

                    pre, ext = os.path.splitext(full_name)
                    print('pre: ', pre)
                    print('ext: ', ext)
                    # os.rename(renamee, pre + new_extension)
                    # new_name = os.rename(full_name, pre + jpg)
                    # print('new_name: ', os.rename(full_name, pre + jpg))

                    # full_name = full_name[:-3] + jpg
                    full_name = pre + '.' + jpg
                    # print('file: ', file)
                    print('changed full_name: ', full_name)
                    # outFile.write(file + '\n')
                    outFile.write(full_name + '\n')
                else: 
                    continue    


            # if (os.path.splitext(file_name)[1] == '.wav'):
            #     print('os.path.split(path)[0]', os.path.split(path)[0])
            #     dir = os.path.split(path)
            #     # print('dir[0]:', dir[0])
                
            #     # rel_path = os.path.realpath(path)
            #     # print('rel_path:', rel_path)                

            #     rel_dir = os.path.relpath(path, root_dir)
            #     two_up = dirname(dirname(rel_dir))
            #     print('two_up', two_up)
            #     # two_up =  path.abspath()

            #     print('rel_dir1:', rel_dir)
            #     # print('rel_dir[:5]:', rel_dir[:5])
            #     # sub_dir1 = os.path.dirname()
            #     # print('rel_dir2:', rel_dir2)
            #     rel_file = os.path.join(rel_dir, file_name)
            #     print('rel_file:', rel_file)
            #     print('rel_file[-7:-4]:', rel_file[-7:-4])
            #     print('rel_file[-8:-4]:', rel_file[-8:-4])

                # ##### ===== for Z02 data =====
                # # if (rel_file[:3] == 'Z02' and rel_file[-7:-4] == 'Ch1'):
                # if (rel_file[:3] == 'Z02' and rel_file[-7:-4] == 'Ch2'):
                # if (rel_file[:3] == 'Z02' and rel_file[-8:-4] == 'Wav3'):                                        
                #     print('rel_file Z01:')
                #     flst_data = Z02 + rel_file[:-4] + ' ' + 'OK'
                #     # flst_data = Z01 + rel_file[:-4] + ' ' + 'UNK'
                # else:
                #     continue

                # flst_data = rel_file[:-4] + ' ' + 'OK'
                
                # print('flst_data:', flst_data)
                # outFile.write(flst_data + '\n')
                # outFile.write(flst_data+'\n')
                # print ('last:', os.path.join(path, file_name))


# os.path.split(os.path.split(x)[0])[1]

# # sig_path="C:\projects\uasr-data\izfp-simultrain\common\sig\Z01"
# sig_path="/c/projects/uasr-data/izfp-simultrain/common/sig/Z01" 

# dir_path = os.path.dirname(os.path.realpath(__file__))
# cwd = os.getcwd()
# print('dir_path', dir_path)
# print('cwd', cwd)
# print('cwd', )

# file_path = [f for f in listdir(sig_path) if isfile(join(sig_path, f))]
# print('onlyFiles', file_path)



# f = []
# for (dirpath, dirnames, filenames) in walk(sig_path):
#     f.extend(filenames)
#     print('f:', f)
#     break

if __name__ == '__main__':
    # old()
    # getVisitingDirs()
    getAllFiles(cwd)
    writeFileLists(file_list)
    # test()