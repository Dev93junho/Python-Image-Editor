"""
@ Data Loader 
1. get data folder / file path
2. if read data file convert to folder, check data folder structure
3. create & save json
4. if find editorial data from main.py, then load json

input : data path 
output : data folder with img folder, copied tck, 

@ Author : Junho Shin, 2022.10
"""
"""
@ image update rule
1. get data file path
2. read 
3. print 10 frame's trajectory
4. if get update request, windowing to next 10 frames trajectory
"""
"""
@ trajectory update rule
1. get data file path
2. convert binary to numpy array per 10 frames
3. print 10 frame's trajectory
4. if get update request, windowing to next 10 frames trajectory
"""


import os, shutil
import datetime
import numpy as np
from PIL import Image
import argparse
import json

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

class DataLoader:
    def __init__(self, __file__):
        super().__init__()
        # parse data  path
        # self.root = self.argParse(__file__)
        abs_data_path = os.path.abspath(__file__) 
        splited_path = os.path.dirname(__file__)
        data_name = abs_data_path.split('/')[-1].split('.')[0]
        print("디렉토리 경로 : ", splited_path, "파일(폴더)명 : ", data_name) # print data path & folder name
               
        # if img folder not exist
        if os.path.exists(splited_path + '/' + data_name + '/img'):
            return None
        if not os.path.isdir(splited_path + '/' + data_name):
            print("데이터 폴더가 존재하지 않습니다. 데이터 폴더를 생성합니다.")
            
            os.mkdir(splited_path + '/' + data_name) # create img folder
            shutil.copyfile(splited_path + '/' + data_name + '.tck', splited_path + '/' + data_name + '/' + data_name + '.tck')
            
            new_data_path = splited_path + '/' + data_name  
            new_tck_path = splited_path + '/' + data_name + '/' + data_name + '.tck' # get tck file path
            
            # savd json
            DataLoader.create_json(new_data_path, new_tck_path, data_name) 
            
            if os.path.exists(new_data_path + '/img'):
                return None
            else:
                os.mkdir(new_data_path + '/' + 'img') # create img folder
                new_img_path = new_data_path + '/' + 'img' # get img folder path
            
                # save png file to img folder from img file
                img_root = splited_path + '/' + data_name + '.img' # get img file path
                for i in range(1000):
                    img = self.imgfile_read_frame(img_root)
                    img.save(new_img_path + '/' + str(i) + '.png') # save png file to img folder

            
    # uint8 to PIL Image
    def imgfile_read_frame(self):
        imghdr = np.fromfile(__file__, dtype=np.int32, count=2)
        if len(imghdr) < 2: return None
        w, h = imghdr
        if w * h <= 0: return None
        img = np.fromfile(__file__, dtype=np.int16, count=w*h)
        if len(img) < w * h:
            return None
        
        img = Image.fromarray(img.reshape(h, w))
        return img  

    # iterable create in json file
    def create_json(img_data_path, traj_data_path, filename):
        # create json array per frame
        make_json = []
        with open(filename + '.json', 'w') as f:
            for i in range(len(img_data_path)):
                make_json.append({
                    'frame_idx': i,
                    'sequence' : None, # need to be changed
                    'img_path': img_data_path[i],
                    'traj_info': traj_data_path[i],
                    'move_state' : None, # 0 : stop, 1 : move
                    "label" :None, # need to be changed
                }),
            json.dump(make_json, f, indent=4) # save json file
        
        
    def read_json(json_data_path):
        # find json file in data root
        with open(json_data_path, 'r') as f:
            json_data = json.load(f)
            return json_data

    def update_json(path, idx, value):
        with open(path, 'w+') as f:
            pre_data = json.load(f)
            suf_data = pre_data[idx] = value
            return suf_data

    def delete_json(path, idx):
        with open(path, 'w+') as f:
            pre_data = json.load(f)
            suf_data = pre_data[idx] = None
            return suf_data
    
    # # define argument parser
    # def argParse(self):
    #     self.parser = argparse.ArgumentParser(description='input data path')
    #     self.parser.add_argument('--data_path', default=True, help='input data path', action='store_true')
    #     self.parser.add_argument('--json_path', default=False, help='input json path')
    #     self.parser.add_argument('--frm_idx', default=False, help='input frame index')
    #     self.parser.add_argument('--idx', default=False, help='input data index')
    #     self.parser.add_argument('--value', default=False, help='input change value')
       
    #     # 입력 인자 args에 저장
    #     self.args = self.parser.parse_args()
    #     return self.args
    
if __name__ == '__main__':
    # class instance
    dataloader = DataLoader(__file__)
    # parser = argparse.ArgumentParser(description='input data path')
    # parser.add_argument('--data_path', default=True, help='input data path', action='store_true')
    # parser.add_argument('--json_path', default=False, help='input json path')
    # parser.add_argument('--frm_idx', default=False, help='input frame index')
    # parser.add_argument('--idx', default=False, help='input data index')
    # parser.add_argument('--value', default=False, help='input change value')
    
    # args = parser.parse_args()
    # print(args)
    
