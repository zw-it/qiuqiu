def calculator():
    """命令行交互式计算器"""
    print("=== 简易计算器 ===")
    print("支持运算符: +, -, *, /, **")
    while True:
        try:
            #获取用户输入
            expr=input('请输入(输入q退出程序)：').strip()
            if expr.lower()=='q':
                print('程序终止')
                break
            #检查字符串
            allowed_chars = set("123456789+-*/.()**")#允许的字符集合
            if not all(c in allowed_chars for c in expr):
                raise ValueError('包含非法字符')
            result=eval(expr)
            print(f"结果为：{result}\n")
        except ZeroDivisionError:
            print('被除数不能为零')
        except (SyntaxError,NameError):
            print('错误，表达式格式错误')
        except ValueError as e:
            print(f"错误：{e}")
if __name__ == '__main__':
    calculator()

import csv
from pathlib import Path                                     # 1. 导入库

def csv_statistics(file_path, column_name):
    values=[]
    #检查文件路径是否正确
    try:
        if not Path(file_path).exists():
            raise FileNotFoundError(f'文件路径{file_path}错误或不存在')
        #打开文件
        with open(file_path,'r',encoding='utf-8') as f:
        #读取文件为字典格式
            reader=csv.DictReader(f)
        #查询列是否存在
        if  column_name not in reader.fieldnames:
            raise ValueError(f'列{column_name}不存在')
        #遍历每一行
        for row in reader:
            # 转化为浮点数
            # 添加到value中
            value=float(row[column_name])
            values.append(value)
        # 空数据检查
        if not values:
            return None
        stats={
            '总和':sum(values),
            '平均值':sum(values)/len(values),
            '最大值':max(values),
            '最小值':min(values),
            '数据量':len(values)
        }
        return stats
        #计算结果
    except  Exception as e:
        print(f'错误：{e}')
        return None