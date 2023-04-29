import numpy as np

if __name__ == "__main__":
    with open("./view_temps_output_data.data","r") as f:#需要把文件路径替换成你解压之后的地方
        data = f.read()
    data_splited = data.split('\n')
    months_data = []
    for i in range(int(len(data_splited)/(180+1))):
        one_month_data=[]
        one_month_description=""
        for j in range(i*(180+1),(i+1)*(180+1)):
            if j % (181) !=0:
                temp = data_splited[j].replace("-32768"," -32768")
                temp = [float(x) for x in temp.split(" ") if x !=""]
                one_month_data.append(temp)
            else:
                one_month_description=data_splited[j]
        months_data.append(one_month_data)
    np_data = np.array(months_data)
    print(np.shape(np_data)) #(12, 180, 360)