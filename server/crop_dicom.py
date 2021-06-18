import SimpleITK as sitk
from PIL import Image

def crop_dicom(dicom_path,x1,y1,x2,y2):
    # x1 = 200
    # y1 = 200
    # x2 = 800
    # y2 = 800
    file_reader = sitk.ImageFileReader()
    file_reader.SetFileName(dicom_path)  # 这里只显示了必需的,还有很多可以设置的参数
    image = file_reader.Execute()
    # 使用这种方法读取Dicom的Tag Value
    # for key in file_reader.GetMetaDataKeys():
    #     print(key, file_reader.GetMetaData(key))
    print(image.GetWidth())
    crop = sitk.CropImageFilter()
    crop.SetLowerBoundaryCropSize([x1,y1, 0])
    x_upper = image.GetWidth()-x2
    y_upper = image.GetHeight()-y2
    print(x_upper,y_upper)
    crop.SetUpperBoundaryCropSize([x_upper,y_upper,0])
    cropped_image = crop.Execute(image)
    writer = sitk.ImageFileWriter()
    writer.SetFileName(dicom_path)
    writer.Execute(cropped_image)
    data_np = sitk.GetArrayFromImage(cropped_image) # z, y, x
    im = Image.fromarray(data_np[0])
    im = im.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
    im.save('./testdcm/outfile.jpg')
    # over


# crop_dicom("../testdcm/1.dcm",236,105,746,763)