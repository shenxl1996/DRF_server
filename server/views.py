from django.http import FileResponse
from django.http import HttpResponse
import glob
import json
from server.crop_dicom import crop_dicom
from django.core.serializers.json import DjangoJSONEncoder
import numpy as np
# Create your views here.
def getdicom(request):
    index = request.GET['index']
    # key = request.GET['key']
    # print("请求dicom序号",int(index))
    arr = [1,2,3,4,5,5,6,6,7,7,4]
    txtlist = glob.glob(r"./testdcm/*.dcm")
    txtlist.sort()
    dicom_name = txtlist[int(index)]
    # print("请求路径",dicom_name)
    file = open(dicom_name, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename='+index+".dcm"
    return response

def performSDK(request):
    info = request.GET['info']
    print(info)
    res = {
        'success':True,
    }
    return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder), content_type='application/json')

def read0(request):
    file = open('./testdcm/label0082.nii.gz', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="label0082.nii.gz"'
    # response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Origin"
    return response

def read1(request):
    file = open('./testdcm/1.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return response
def read2(request):
    file = open('./testdcm/2.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="2.dcm"'
    return response
def read3(request):
    file = open('./testdcm/3.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="3.dcm"'
    return response
def read4(request):
    file = open('./testdcm/4.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="4.dcm"'
    return response
def read5(request):
    file = open('./testdcm/5.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="5.dcm"'
    return response
def read6(request):
    file = open('./testdcm/6.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="6.dcm"'
    return response
def read7(request):
    file = open('./testdcm/7.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="7.dcm"'
    return response
def read8(request):
    file = open('./testdcm/8.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="8.dcm"'
    return response
def read9(request):
    file = open('./testdcm/9.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="9.dcm"'
    return response

def read1jpg(request):
    file = open('./testdcm/1.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="1.jpg"'
    return response
def read2jpg(request):
    file = open('./testdcm/2.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="2.jpg"'
    return response
def read3jpg(request):
    file = open('./testdcm/3.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="3.jpg"'
    return response
def read4jpg(request):
    file = open('./testdcm/4.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="4.jpg"'
    return response
def read5jpg(request):
    file = open('./testdcm/5.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="5.jpg"'
    return response
def read6jpg(request):
    file = open('./testdcm/6.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="6.jpg"'
    return response
def read7jpg(request):
    file = open('./testdcm/7.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="7.jpg"'
    return response
def read8jpg(request):
    file = open('./testdcm/8.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="8.jpg"'
    return response
def read9jpg(request):
    file = open('./testdcm/9.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="9.jpg"'
    return response
def readdarkjpg(request):
    file = open('./testdcm/dark.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="dark.jpg"'
    return response


def readmask1(request):
    index = request.GET['index']
    print(int(index))
    arr = [1,2,3,4,5,5,6,6,7,7,4]
    txtlist = glob.glob(r"./testdcm/*.txt")
    global res
    res = {
        'success':True,
        'data':arr
    }
    txtlist.sort()
    # print(txtlist)

    for idx,txtname in enumerate(txtlist):
        file = open(txtname,"r")
        liststr = file.readlines()
        mask = liststr[0][1:-1].split(', ')
        mask = list(map(int,mask))
        if idx == int(index):
            res = {
                'success': True,
                'data': mask
            }

    return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder), content_type='application/json')

def cropdata(request):
    position = request.POST.get('position')
    index = request.POST.get('index')
    index = int(index)
    position = position.split(',')
    position = list(map(float, position))
    position = list(map(round, position))
    position = list(map(int, position))
    txtlist = glob.glob(r"./testdcm/*.dcm")
    txtlist.sort()
    dicom_name = txtlist[index]
    print(dicom_name)
    from django.core.serializers.json import DjangoJSONEncoder
    crop_dicom(dicom_name,position[0],position[1],position[2],position[3])


    print(position,index)
    res = {
        'success': True
    }
    return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder), content_type='application/json')