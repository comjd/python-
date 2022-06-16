#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/19 下午2:17
# @Author : tyler
# @File : fileprocess.py
# @Project : code1
import os
import time


class FileProcess:
    def __init__(self):
        self.is_first = True

    @staticmethod
    def file_exists(filepath):
        """
            判断文件路径是否存在
        :return: True文件路径存在, False文件路径不存在
        """
        return os.path.exists(filepath)

    @staticmethod
    def get_file_status(filepath):
        """
        获取文件属性
        :return:文件属性
        """
        return os.stat(filepath)

    @staticmethod
    def get_file_update_time(filepath, format_str=''):
        """
            获取文件最后修改时间
        :param filepath: 文件路径
        :param format_str: 时间格式化字符串，不传值就返回时间戳
        :return: 文件最后修改时间
        """
        if not format_str:
            return os.path.getctime(filepath)
        return time.strftime(format_str, time.localtime(os.path.getmtime(filepath)))

    @staticmethod
    def get_file_visit_time(filepath, format_str=''):
        """
            获取文件最后访问时间
        :param filepath: 文件路径
        :param format_str: 时间格式化字符串，不传值就返回时间戳
        :return: 文件访问时间
        """
        if not format_str:
            return os.path.getctime(filepath)
        return time.strftime(format_str, time.localtime(os.path.getatime(filepath)))

    @staticmethod
    def get_file_create_time(filepath, format_str=''):
        """
            获取文件创建时间
        :param filepath: 文件路径
        :param format_str: 时间格式化字符串，不传值就返回时间戳
        :return: 文件创建时间
        """
        if not format_str:
            return os.path.getctime(filepath)
        return time.strftime(format_str, time.localtime(os.path.getctime(filepath)))

    @staticmethod
    def get_file_size(filepath):
        """
            获取文件的字节数
        :return: 文件大小（字节数）
        """
        return os.path.getsize(filepath)

    @staticmethod
    def get_file_name(filepath):
        """
            获取文件名称
        :return: 文件名称
        """
        return os.path.basename(filepath)

    @staticmethod
    def get_file_abspath(filepath):
        """
            获取文件绝对路径
        :return: 文件绝对路径
        """
        return os.path.abspath(filepath)

    @staticmethod
    def get_file_path(filepath):
        """
            获取文件路径
        :return: 文件路径
        """
        return os.path.dirname(filepath)

    @staticmethod
    def is_file(filepath):
        """
            判断文件路径是否为文件
        :return: True是文件 False不是文件
        """
        return os.path.isfile(filepath)

    @staticmethod
    def is_dir(filepath=''):
        """
            判断路径是否为目录
        :return: True是目录 False不是目录
        """
        return os.path.isdir(filepath)

    @staticmethod
    def dir_exists(filepath=''):
        """
            判断目录是否存在
        :return: True存在 False不存在
        """
        return os.path.isdir(filepath)

    @staticmethod
    def delete_file(filepath):
        """
            删除单个文件
        :return: True删除成功，False删除失败
        """
        if FileProcess.file_exists():
            os.remove(filepath)
            return True
        return False

    @staticmethod
    def read_all_file(filepath, model=1):
        """
            一次读取文件所有内容
        :return:读取到的文件内容
        """
        model = 'rb' if model == 1 else 'r'
        with open(filepath, model) as f:
            return f.read()

    @staticmethod
    def read_line_file(filepath, model=1):
        """
            一次读取文件一行内容
        :return:读取到的一行内容
        """
        model = 'rb' if model == 1 else 'r'
        with open(filepath, model) as f:
            for line in f:
                yield line

    @staticmethod
    def file_rename(filepath, new_name):
        """
            文件重命名
        :param filepath:
        :param new_name: 新文件名称
        :return:
        """
        os.rename(FileProcess.get_file_name(filepath), new_name)

    @staticmethod
    def write_file(filename, data, path='', write_model=1):
        """
            将内容一次性写入到文件
        :param filename: 写入的文件名称
        :param data: 写入的内容
        :param path: 写入文件的路径，为空是，路径为当前文件夹
        :param write_model: 写入的类型,1覆盖模式，2在末尾追加模式 3在开头追加
        :return: True写入成功，False写入失败
        """
        if path == '':
            path = os.getcwd()
        path = os.path.join(path, filename)
        if write_model == 1:
            fd = 'wb'
        elif write_model == 2:
            fd = 'ab'
        elif write_model == 3:
            fd = 'rb+'
        with open(path, fd) as f:
            if write_model == 3:
                content1 = f.read()
                f.seek(0, 0)
            f.write(data)
            if write_model == 3:
                f.write(content1)
            f.flush()
            return True
        return False

    @staticmethod
    def create_dir(dir_name, path=''):
        """
            创建文件目录
        :param dir_name: 需要创建文件夹的名称
        :param path: 创建的文件路径,为空时路径为当前程序所在路径
        :return: True创建成功，False创建失败
        """
        if path == '':
            path = os.getcwd()
        path = os.path.join(path, dir_name)
        if FileProcess.is_dir(path) and not FileProcess.dir_exists(path):
            os.mkdir()
            return True
        return False

    @staticmethod
    def get_path_all_files(path):
        """
        获取目录下的所有文件及目录
        :param path: 目录
        :return:
        """
        if FileProcess.is_dir(path):
            return os.listdir(path)
        return None

    @staticmethod
    def get_path_all_filenames(path):
        """
        获取目录下的所有文件名
        :param path: 目录
        :return:
        """
        if FileProcess.is_dir(path):
            return [name for name in os.listdir(path) if FileProcess.is_file(os.path.join(path, name))]
        return None


if __name__ == '__main__':
    path = 'test_tcp_files'
    print(FileProcess.get_path_all_files(path))
    # print(FileProcess.file_exists(path))
    # print(FileProcess.get_file_status(path))
    # print(FileProcess.get_file_update_time(path, '%Y-%m-%d %H:%M:%S'))
    # print(FileProcess.get_file_visit_time(path, '%Y-%m-%d %H:%M:%S'))
    # print(FileProcess.get_file_create_time(path, '%Y-%m-%d %H:%M:%S'))
    # print(FileProcess.get_file_size(path))
    # print(FileProcess.get_file_name(path))
    # print(FileProcess.get_file_abspath(path))
    # print(FileProcess.get_file_path(path))
    # print(FileProcess.is_dir(path))
    # print(FileProcess.is_file(path))
    # print(FileProcess.read_all_file(path))
    # # print(f.file_rename('test.py'))
    # print('all-w', FileProcess.write_file('test1.py', data=FileProcess.read_all_file(path)))
    # for line in FileProcess.read_line_file(path):
    #     FileProcess.write_file('test2.py', line, '/home/tyler/dev/code1/projects', 3)

    # print(FileProcess.create_dir('test', '/home/tyler/dev/code1/projects/'))
    # print(f.delete_file())
    # a = time.time()
    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(a)))
