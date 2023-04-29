with open("./view_temps_output_data.data","r") as f:#需要把文件路径替换成你解压之后的地方
    data = f.read()

data_splited = data.split('\n')
# print(len(data_splited))#2173，是因为180个纬度*12个月+12个月的说明+1行空行(在最后)=2173
# print("第一行:", data_splited[0])#每个月的说明     1     1  2004   180 rows    360 columns
# print("最后一行:", data_splited[-1])#最后一行是个空的
# print(data_splited[1])
# -1000 *360，也就是经度
#这是北纬90度，-10是因为HadiSST测量的海表温度的最低值是-10摄氏度。这代表着北纬90度的有360个-10度的数据。其从哪里开始可以看官网说明https://www.metoffice.gov.uk/hadobs/hadisst/data/Read_instructions_sst.txt，从180W开始的。


# print(data_splited[1].split(" "))#把每个经度给分开了
# print(len(data_splited[1].split(" ")))#361，因为一开始有个空格，就把前面的""也给分出来了

# print([x for x in data_splited[1].split(" ") if x !=""])#使用build in去除掉""即可
# print(len([x for x in data_splited[1].split(" ") if x !=""]))#360,这是正确的

# res = {}
months_description = []
months_data = []
for i in range(int(len(data_splited)/(180+1))):#0-11，因为int会把float强转
    one_month_data=[]
    one_month_description=""
    for j in range(i*(180+1),(i+1)*(180+1)):
        if j % (181) !=0:
            temp = data_splited[j].replace("-32768"," -32768") #-缺省值32768没有空格，所以会出问题，给所有出现-32768的加一个空格
            temp = [float(x) for x in temp.split(" ") if x !=""]#根据上面的进行分行
            one_month_data.append(temp)
        else:
            one_month_description=data_splited[j]
    months_data.append(one_month_data)
    months_description.append(one_month_description)

# print(months_description)
# print(len(months_data))
# print(len(months_data[0]))
# print(len(months_data[0][0]))
#print(len(months_data[0][90]))
#print(len(months_data[0][179]))
#print(months_data[0][179])


