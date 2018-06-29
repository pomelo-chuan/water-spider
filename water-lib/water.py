# -*- coding: utf-8 -*-
import os
import requests


class Water(object):
    def __init__(self, url, save_dir):
        self.url = url
        self.save_dir = save_dir

    def save_img(self, url, save_dir, name):
        if os.path.exists(save_dir):
            pass
        else:
            os.mkdir(save_dir)
        ir = requests.get(url, stream=True)
        if ir.status_code == 200:
            with open(save_dir + '/' + name, 'wb') as f:
                for chunk in ir:
                    f.write(chunk)
                f.close()
            print ('successful saved: ' + url)


