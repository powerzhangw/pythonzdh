# -*- coding: utf-8 -*-
import requests
import json
import lib.logUntil
import random
import string
import time
import uitls.config
co = uitls.config

log = lib.logUntil.Log()


def get_code():
    f = open('C:\\txt.txt', 'r')
    code = f.read()
    f.close()
    return code
po = get_code()

def get_bus():
    random_string = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    my_string = random_string.lower()
    return my_string

def get_datas(repayMethodText,customerName,deptID,funder,productId,amount,get_cod,funderProductConfig,time):
    try:
        url = '{0}/external/core/order/test'.format(co.url)
        datas = {"bankcardInfos":[{"number":"6214830283467990","code":"308","tel":"18693080140","type":"1","branch":"人民广场支行","master":customerName},{"number":"6214830283467990","code":"308","tel":"17621032205","type":"2","branch":"人民广场支行","master":customerName}],"borrowerBaseInfos":[{"addressSummary":"四川省-成都市-锦江区","reason":"","customerType":"1","addressCityCode":620100,"addressDetail":"大凉山路塔子山公园","addressAreaCode":510104,"telephone":"18693080140","customerPropertiy":"1","customerName":customerName,"customerNo":"510104199001010940","addressProvinceCode":620000,"relation":""},{"addressSummary":"四川省-成都市-锦江区","reason":"0002300003","customerType":"2","addressCityCode":460200,"addressDetail":"共借人常驻地址208","addressAreaCode":510104,"telephone":"17621032210","customerPropertiy":"1","customerName":"马强","customerNo":"510104198601013833","addressProvinceCode":460000,"relation":"0001700002"},{"addressSummary":"四川省-成都市-锦江区","reason":"0002300001","customerType":"2","addressCityCode":610100,"addressDetail":"配偶的常驻地址详细","addressAreaCode":510104,"telephone":"17621032208","customerPropertiy":"1","customerName":"王芳芳","customerNo":"620101199002287243","addressProvinceCode":610000,"relation":"0001700005"}],"attachInfo":[{"classifyIdString":"123","classifyId":123,"available":1,"sort":0,"userId":"18a65f06d323464baab9a4cfbde3a0cf","url":"038c7e806d2b4df78d877acec0cdae04","inputFlow":"","applyId":"c273e2110590445998df4a5bd6d9915c","attachType":"docx","createTime":"2019-01-24 20:07:28","attachName":"2-1（新子公司签）信息咨询服务协议（融资撮合+代办公证抵押+代收居间）（逾期不折让）.docx","extraId":"dc78c05ab84e4c12b5d3aca3da1cc7d1","attachmentId":374330,"tag":"upload1","thumbUrl":""},{"classifyIdString":"122","classifyId":122,"available":1,"sort":0,"userId":"18a65f06d323464baab9a4cfbde3a0cf","url":"1bad80ac76f34278a7fd718f31e99474","inputFlow":"","applyId":"c273e2110590445998df4a5bd6d9915c","attachType":"docx","createTime":"2019-01-24 20:08:09","attachName":"3-1（宁波签）（提清定额计价+逾期不折让）管理咨询服务协议（咨询服务+贷后管理服务）.docx","extraId":"dc78c05ab84e4c12b5d3aca3da1cc7d1","attachmentId":374331,"tag":"upload1","thumbUrl":""},{"classifyIdString":"124","classifyId":124,"available":1,"sort":0,"userId":"18a65f06d323464baab9a4cfbde3a0cf","url":"85fc3d7d985e44df91114edc93c0b536","inputFlow":"","applyId":"c273e2110590445998df4a5bd6d9915c","attachType":"docx","createTime":"2019-01-24 20:08:28","attachName":"4服务协议.docx","extraId":"dc78c05ab84e4c12b5d3aca3da1cc7d1","attachmentId":374332,"tag":"upload1","thumbUrl":""}],"loanInfo":{"funder":funder,"fileNumber":get_cod,"customerAll":"马强","serviceLimit":12,"productId":productId,"platformNumber":"0009800021","rateText":0.0860,"deptId":deptID,"contractNumber":"YJJR028201901240000101","repayMethodText":repayMethodText,"businessNumber":get_bus(),"funderProductConfig":funderProductConfig,"isCombo":0,"transferDate":"","customerName":customerName,"compreRateText":12.0000,"salerId":"afa666767df24184982a2f84c4afde54","isSpecial":"","loanLimit":12,"loanDate":time,"customerNo":"510104199001010940"},"contract":[{"extra":{"signPlace":"{北京市}{市辖区}{东城区}","overduePrice":"","signAddress":[110000,110100,110101],"serviceNumber":"YJ2105129920190124000010102","concession":"22","city":"市辖区","year":"2019","companyBankno":"0011600002","contractType":"123","documentNumber":"510104199001010940","loanFeeCh":"","companyName":"0011100001","inputUser":"18a65f06d323464baab9a4cfbde3a0cf","signDate":"2019-01-24","applyId":"c273e2110590445998df4a5bd6d9915c","bank":"人民广场支行","serviceAmount":"11","province":"北京市","agenPrice":"33","companyEmail":"0011700001","attachlists":"附件一：","concessionCh":"贰拾贰元整","inputDept":"1571404b501940b385112b937ae8d988","agenPriceCh":"叁拾叁元整","contractName":"","homeaddr":"大凉山路塔子山公园","proxyPriceCh":"肆拾肆元整","day":"24","email":"power228@qq.com","area":"东城区","loanFee":"","concession_1":"","telephone":"18693080140","contractAmountCh":"壹佰万元整","customerName":customerName,"attachs":"（见附件一）","serviceAmountCh":"壹拾壹元整","companyBank":"0011500002","month":"01","companyAddress":"0011400001","bankno":"6214830283467990","contractId":"560","beforeDay":"","contractAmount":"1000000","proxyPrice":"44","companyTelephone":"0011200003","concession_1_ch":""},"contractFileId":"038c7e806d2b4df78d877acec0cdae04","contractNumber":"YJ2105129920190124000010102","remark":"","contractName":"2-1（新子公司签）信息咨询服务协议（融资撮合+代办公证抵押+代收居间）（逾期不折让）.docx","configContractId":"01c402a307c04987ae638a6a1198a2b7"},{"extra":{"overduePrice":"12","signAddress":[110000,110100,110101],"serviceNumber":"YJ2105129920190124000010103","concession":"55","year":"2019","companyBankno":"0011600002","contractType":"122","documentNumber":"510104199001010940","loanFeeCh":"","companyName":"0011100002","inputUser":"18a65f06d323464baab9a4cfbde3a0cf","signDate":"2019-01-24","advance":"1-1|2-2|3-3|4-4|5-5|6","applyId":"c273e2110590445998df4a5bd6d9915c","bank":"人民广场支行","province":"北京市","agenPrice":"","attachlists":"附件一：","concessionCh":"伍拾伍元整","inputDept":"1571404b501940b385112b937ae8d988","proxyPriceCh":"","day":"24","s1":"12","s2":"12","s3":"12","area":"东城区","concession_4_1":"4","s4":"12","concession_2_2":"2","s5":"12","concession_2_1":"2","s6":"12","advance_3_2":"3","advance_3_1":"3","advance_5_2":"5","concession_6_1":"6","advance_5_1":"5","concession_4_2":"4","concession_1":"","telephone":"18693080140","advance_1_2":"1","contractAmountCh":"壹佰万元整","advance_1_1":"1","customerName":customerName,"month":"01","bankno":"6214830283467990","beforeDay":"","contractAmount":"1000000","beforetime":"04:04","proxyPrice":"","companyTelephone":"0011200003","signPlace":"{北京市}{市辖区}{东城区}","city":"市辖区","serviceAmount":"55","companyEmail":"0011700001","agenPriceCh":"","contractName":"","homeaddr":"大凉山路塔子山公园","email":"power228@qq.com","concession_3_2":"3","concession_3_1":"3","loanFee":"","concession_1_2":"1","concession_1_1":"1","cp2":"12","advance_4_1":"4","cp1":"12","advance_2_2":"2","cp4":"12","advance_6_1":"6","concession_5_2":"5","cp3":"12","advance_4_2":"4","concession_5_1":"5","cp6":"12","cp5":"12","advance_2_1":"2","cp":"12|12|12|12|12|12","attachs":"（见附件一）","serviceAmountCh":"伍拾伍元整","concessions":"1-1|2-2|3-3|4-4|5-5|6","s":"12|12|12|12|12|12","companyBank":"0011500001","companyAddress":"0011400002","contractId":"561","concession_1_ch":""},"contractFileId":"1bad80ac76f34278a7fd718f31e99474","contractNumber":"YJ2105129920190124000010103","remark":"","contractName":"3-1（宁波签）（提清定额计价+逾期不折让）管理咨询服务协议（咨询服务+贷后管理服务）.docx","configContractId":"3b29254360d14dac8b410668e48ae18e"},{"extra":{"signPlace":"{北京市}{市辖区}{东城区}","overduePrice":"","signAddress":[110000,110100,110101],"serviceNumber":"YJ2105129920190124000010104","concession":"","city":"市辖区","year":"2019","companyBankno":"0011600001","contractType":"124","documentNumber":"510104199001010940","loanFeeCh":"柒拾柒元整","companyName":"0011100001","inputUser":"18a65f06d323464baab9a4cfbde3a0cf","signDate":"2019-01-24","applyId":"c273e2110590445998df4a5bd6d9915c","bank":"人民广场支行","serviceAmount":"","province":"北京市","agenPrice":"","companyEmail":"","attachlists":"附件一：","concessionCh":"","inputDept":"1571404b501940b385112b937ae8d988","agenPriceCh":"","contractName":"","homeaddr":"大凉山路塔子山公园","proxyPriceCh":"","day":"24","email":"power228@qq.com","area":"东城区","loanFee":"77","concession_1":"","telephone":"18693080140","contractAmountCh":"","customerName":customerName,"attachs":"（见附件一）","serviceAmountCh":"","companyBank":"0011500002","month":"01","companyAddress":"0011400002","bankno":"6214830283467990","contractId":"562","beforeDay":"","contractAmount":"","proxyPrice":"","companyTelephone":"","concession_1_ch":""},"contractFileId":"85fc3d7d985e44df91114edc93c0b536","contractNumber":"YJ2105129920190124000010104","remark":"","contractName":"4服务协议.docx","configContractId":"ba2f537fc8f04e04bdee90f820be0ed8"}],"capitalInfos":[{"amountArrange":0.00,"compreRates":[],"amount":amount,"serviceLimit":12,"rate":0.0860,"repayMethod":"0001100003","loanLimit":12,"compreRate":12.0000,"type":1,"comboDetail":""}],"borrowerLoanInfos":[{"amountArrange":0.00,"compreRates":[],"amount":amount,"serviceLimit":12,"rate":0.0860,"repayMethod":"0001100003","loanLimit":12,"compreRate":12.0000,"type":1,"comboDetail":""}],"jointerId":"013a2f5c1e1f4e0eaba38d0f7d0a9318","guarantyInfos":[{"certificateName":"","source":"0006900001","fastSellPrice":"","landCertificateNumber":"","fastSellTime":"","landLife":"0007000003","addressCityCode":510100,"faceStreet":"0008000001","totleFloor":"","displacement":"","trafficConvenience":"0014100001","brand":"","mortgageFileId":"","hasBalcony":"","addressAreaCode":510104,"degree":"0007900001","acreage":100.00,"currentUsage":"0014000001","primaryAssessFileId":"","SaddressDetail":"大业路205号","assessmentReportId":"","agencyTele":"","hasGarden":"","carNumber":"","buildingStructure":"0014300001","useage":"0006800001","mortgageStatus":2,"maintainStatus":"0007800001","decorateStatus":"0007200001","ventilationStatus":"0007700001","addressSummary":"四川省-成都市-锦江区","classify":"0006100001","assessPrice":"","buyDate":"2008-08-08 00:00:00","leftUseTime":"","realEstateCertificateNumber":"","house":"楼盘名称","notarizationFileId":"","carColor":"","carType":"","propertyType":"","accessTotle":200.00,"latestAssessment":"","floor":33,"addressProvinceCode":510000,"residentDetail":"居住人员---------------初评录入","nature":"0007600001","repeatAssessFileId":"","assessDate":"","foundYears":"2008","certificateNumber":"chanquan001","isPeripheralBusiness":"","sharePercent":[{"name":"调试一"},{"name":"王芳芳"}],"carMileage":0.00,"shareStatus":"0007500002"}]}
        data = json.dumps(datas)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=data)
        code = response.json()['code']
        msg = response.json()['msg']
        log.info(data)
        log.info(u'进件请求结果' + ':' + msg)
        return msg
    except Exception as e:
        log.error(e)

def get_fileNumber():
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    my_code = str(now_time)[0:13]
    f = open('C:\\txt.txt','w')
    f.write(my_code)
    f.close()
    return my_code

def randomname():

    xing='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤'
    ming='小宝金鹰龙飞黄河长江豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖飞爱涵杰伦力宏'
    X=random.choice(xing)
    M="".join(random.choice(ming) for i in range(2))
    return (X+M)
def times():
    t1 = int(time.time())
    t2 = str(t1) + '000'
    time1 = int(t2)
    return (time1)


    # self.repayMethodText = u'等额本息'
    # self.customerName = randomname()
    # self.deptID = '33f1f497727b402c95607439f522ef68'
    # self.funder = '0009800003'
    # self.productId = '0012600001'
    # self.amount = 10
    # self.get_cod = get_fileNumber()
    # self.funderProductConfig = '213f18b0dca4486bbcced92e4c1f725a'
    # self.time = times()
#
postlendresult = get_datas(repayMethodText=u'等额本息',
               customerName=randomname(),
               deptID='33f1f497727b402c95607439f522ef68',
               funder='0009800003',productId='0012600001',
               amount=10,get_cod=get_fileNumber(),
               funderProductConfig='213f18b0dca4486bbcced92e4c1f725a',
               time =times())

#跑批接口
def batch_task(ID):
    try:
        url = '{0}/plan/test/open/test?fileNum={1}'.format(co.url,ID)
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        code = response.json()['code']
        msg = response.json()['msg']
        log.info('%s'%ID + u'跑批结果' + ':' + msg)
        return msg
    except Exception as e:
        log.info(e)

batch_task(get_code())