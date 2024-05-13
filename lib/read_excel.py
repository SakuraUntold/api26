import xlrd
# #打开excel文件
# wb=xlrd.open_workbook("test_user_data.xlsx")
# #读取工作簿
# sheet1=wb.sheet_by_name("test_user_reg")
# #行数
# print(sheet1.nrows)
# #列数
# print(sheet1.ncols)
# #输出第一行第一列
# print(sheet1.cell(0,0).value)
# # #输出第一行的所有值
# # print(sheet1.row_values(0))
# # #将数据和标题组装成字典
# # print(dict(zip(sheet1.row_values(0),sheet1.row_values(1))))
# for i in range(sheet1.nrows):
#     print(sheet1.row_values(i))

class readexcel():

    def excel_to_list(self,data_file,sheet):
        wb=xlrd.open_workbook(data_file)
        sheet1=wb.sheet_by_name(sheet)
        #获取第一行的数据
        keys=sheet1.row_values(0)
        list1=[]
        #从第二行开始获取数据
        for i in range(1,sheet1.nrows):
            j=dict(zip(keys,sheet1.row_values(i)))
            list1.append(j)
        return list1

    def get_test_data(self,data_list,case_name):   #从全部用例数据中读取指定的用例数据
        for case_data in data_list:
            if case_name == case_data['case_name']:  #如果字典数据中case_name与参数一致
                return case_data  #如果查询不到会返回none

if __name__ == '__main__':
    r=readexcel()

    l=r.excel_to_list("test_user_data.xlsx", "test_user_login")
    print(l)
    print(r.get_test_data(l, 'login_ok'))

