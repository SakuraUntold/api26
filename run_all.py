# if __name__ == '__main__':
#     # now=time.strftime("%Y_%m_%d_%H_%M_%S")
#     logging.info("============run_all开始测试================")
#     fe=open(report_file,'wb')
#     runner=HTMLTestRunner(
#         stream=fe,  # 相当于f.write(报告)
#         title='xzs测试报告',
#         description='xzs登录和注册测试报告',
#         verbosity=2  # 为每个测试用例生成测试报告
#     )
#     suit=unittest.defaultTestLoader.discover(prj_path,'test*.py')
#     runner.run(suit)
#     fe.close()
#     send_email(report_file)
#     logging.info("============run_all测试结束================")




import time,pickle,sys
import unittest,logging
from lib.HTMLTestRunner import HTMLTestRunner
from config.config import *
from lib.send_email import send_email
from test.suit.test_suit import get_suit
def discover():
    return unittest.defaultTestLoader.discover(test_case_path,'test*.py')

def run(suite):
    logging.info("===============开始测试=====================")
    with open(report_file,'wb') as f:
            result=HTMLTestRunner(
                stream=f,  # 相当于f.write(报告)
                title='接口测试报告',
                description='接口登录和注册测试报告',
                verbosity=2  # 为每个测试用例生成测试报告
            ).run(suite)
    if result.failures:
        sava_failures(result,last_fails_file) #保存失败用例到文件
        logging.error("测试失败，失败用例已保存到文件: {}".format(last_fails_file))
    else:
        logging.info("测试成功")
    if send_email_after_run:
        send_email(report_file)
    logging.info("===============测试结束=====================")
    logging.info("***************发送邮件**********************")



def run_suite(suite_name):
     suite=get_suit(suite_name)
     if isinstance(suite,unittest.TestSuite):
         run(suite)
     else:
         print("TestSuite不存在")

def run_all():
    run(discover())

def collect():
    suite=unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() !=0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return suite

def collect_only():
    t0=time.time()
    i = 0
    for case in collect():
        i+=1
        print("{}.{}".format(str(i),case.id()))
    print("-------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time() - t0))


def makesuite_by_testlist(test_list_file):
    with open(test_list_file,encoding='utf-8')as f:
        testlist=f.readlines()
        #去掉每行结尾的“/n”和#开头的行
    testlist=[i.strip() for i in testlist if not i.startswith("#")]
    print(testlist)
    suite=unittest.TestSuite()
    all_cases=collect()  #获取工程test/case目录以及目录下所有的testcase
    for case in all_cases:
        case_name=case.id().split('.')[-1]  #获取testcase名称

        if case_name in testlist: #从所有testcase中匹配testlist中定义好的用例
            suite.addTest(case)
    return suite

#根据tag来组建suite
def makesuite_by_tag(tag):
    #申明一个suite
    suite=unittest.TestSuite()
    # 获取当前所有的testcase
    for i in collect():
        #tag和标签
        if i._testMethodDoc and tag in i._testMethodDoc:
            suite.addTest(i)
    return suite

#保存失败用例到文件
def sava_failures(result,file): #file为序列化保存的文件名，配置在config/config.py中
    suite=unittest.TestSuite()
    for case_result in result.failures:
        #case_result是个元组，第一个元素是用例对象，后面是失败的原因等等
        suite.addTest(case_result[0])
    with open(file,'wb')as f:
        pickle.dump(suite,f)  #序列化到指定文件

def rerun_fails(): #失败用例重跑方法
    #将用例路径添加到包搜索路径中，不然反序列化testsuite会找不到用例
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb')as f:
        suite=pickle.load(f) #反序列化得到失败的testSuite
    run(suite)


def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.tag:
        run(makesuite_by_tag(options.tag))
    else:
        run_all()

if __name__ == '__main__':
    run_all()
    # run_suite("smoke_suit")
    # collect_only()
    # suit=makesuite_by_testlist(test_list_file)
    # # run(suit)
    # suite=makesuite_by_tag("level1")
    # run(suite)
    # suite=makesuite_by_testlist(test_list_file)
    # run(suite)
    # rerun_fails()
    # main()









