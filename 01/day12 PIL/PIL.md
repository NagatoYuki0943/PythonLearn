# 导入错误解决

将PIL文件夹放到项目目录即可

# PIL Pillow

使用python进行数字图片处理，还得安装Pillow包。虽然python里面自带一个PIL（python images library), 但这个库现在已经停止更新了，所以使用Pillow, 它是由PIL发展而来的。

**pil能处理的图片类型**
 pil可以处理光栅图片(像素数据组成的的块)。

**通道**
 一个图片可以包含一到多个数据通道，如果这些通道具有相同的维数和深度，Pil允许将这些通道进行叠加

```objectivec
模式
1             1位像素，黑和白，存成8位的像素
L             8位像素，黑白
P             8位像素，使用调色板映射到任何其他模式
RGB           3×8位像素，真彩
RGBA          4×8位像素，真彩+透明通道
CMYK          4×8位像素，颜色隔离
YCbCr         3×8位像素，彩色视频格式
I             32位整型像素
F             32位浮点型像素
```

**坐标**
 Pil采取左上角为(0,0)的坐标系统

## 1 图片的打开与显示 Image.open() image.show()

```dart
from PIL import Image
image=Image.open('d:/dog.png')
image.show()
```

虽然使用的是Pillow，但它是由PIL fork而来，因此还是要从PIL中进行import. 使用open()函数来打开图片，使用show()函数来显示图片。

这种图片显示方式是调用操作系统自带的图片浏览器来打开图片，有些时候这种方式不太方便，因此我们也可以使用另上一种方式，让程序来绘制图片。

```dart
from PIL import Image
import matplotlib.pyplot as plt
image=Image.open('d:/dog.png')
plt.figure("dog")
plt.figure(num=1, figsize=(8,5),)
plt.title('The image title')
plt.axis('off') # 不显示坐标轴
plt.imshow(image)
plt.show()
```

这种方法虽然复杂了些，但推荐使用这种方法，它使用一个matplotlib的库来绘制图片进行显示。matplotlib是一个专业绘图的库，相当于matlab中的plot,可以设置多个figure,设置figure的标题，甚至可以使用subplot在一个figure中显示多张图片。matplotlib 可以直接安装.
 figure默认是带axis的，如果没有需要，我们可以关掉

```python
plt.axis('off')
```

图像加标题

```python
plt.title('The image title')
```

## 2 matplotlib标准模式

```dart
plt.figure(num='newimage', figsize=(8,5),)
plt.title('The image title', color='#0000FF')
plt.imshow(lena) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
```

**PIL image 查看图片信息，可用如下的方法**

```python
print(type(image))
print(image.size)  #图片的尺寸
print(image.mode)  #图片的模式
print(image.format)  #图片的格式
```



## 3 图片的保存 image.save()

```bash
image.save('d:/dog.jpg')
```

就一行代码，非常简单。这行代码不仅能保存图片，还是转换格式，如本例中，就由原来的png图片保存为了jpg图片。



## 4 PIL image 查看图片信息，可用如下的方法

```python
print(type(image))
print(image.size)  				#图片的尺寸
print(image.mode)  				#图片的模式
print(image.format)  			#图片的格式
print(image.getpixel((0,0)))	#得到像素：

```

### image.getpixel((宽, 高)) 获取像素信息

读出来的图片获得某点像素用getpixel((w,h))可以直接返回这个点三个通道的像素值

```python
print(image.getpixel((0,0)))	#得到像素：
# (255, 10, 185)
```



## 5 图像通道/几何变换/裁剪 

PIL可以对图像的颜色进行转换，并支持诸如24位彩色、8位灰度图和二值图等模式，简单的转换可以通过Image.convert(mode)函数完  成，其中mode表示输出的颜色模式，例如''L''表示灰度，''1''表示二值图模式等。但是利用convert函数将灰度图转换为二值图时，是采用 固定的阈 值127来实现的，即灰度高于127的像素值为1，而灰度低于127的像素值为0。

### 5.1 彩色图像转灰度图 image.convert(mode)

```dart
from PIL import Image
import matplotlib.pyplot as plt
image=Image.open('d:/ex.jpg')
gray=image.convert('L')
plt.figure("beauty")
plt.imshow(gray,cmap='gray')
plt.axis('off')
plt.title('The color image to gray image')
plt.show()
```

使用函数convert()来进行转换，它是图像实例对象的一个方法，接受一个 mode 参数，用以指定一种色彩模式，mode 的取值可以是如下几种：

```tsx
1 		(1-bit pixels, black and white, stored with one pixel per byte)
L 		(8-bit pixels, black and white)
P 		(8-bit pixels, mapped to any other mode using a colour palette)
RGB 	(3x8-bit pixels, true colour)
RGBA 	(4x8-bit pixels, true colour with transparency mask)
CMYK 	(4x8-bit pixels, colour separation)
YCbCr 	(3x8-bit pixels, colour video format)
I 		(32-bit signed integer pixels)
F 		(32-bit floating point pixels)
```

### 5.2 通道分离与合并 image.split()  Image.merge()

```python
from PIL import Image
import matplotlib.pyplot as plt
image=Image.open('d:/ex.jpg')  	#打开图像
gray=image.convert('L')   		#转换成灰度

r,g,b=image.split()   			#分离三通道
pic=Image.merge('RGB',(r,g,b)) 	#合并三通道
plt.figure(figsize=(10,8))
plt.subplot(2,3,1), plt.title('origin'), plt.imshow(image),             plt.axis('off')
plt.subplot(2,3,2), plt.title('gray'),   plt.imshow(image,cmap='gray'), plt.axis('off')
plt.subplot(2,3,3), plt.title('merge'),  plt.imshow(pic),               plt.axis('off')
plt.subplot(2,3,4), plt.title('r'),      plt.imshow(r,cmap='gray'),     plt.axis('off')
plt.subplot(2,3,5), plt.title('g'),      plt.imshow(g,cmap='gray'),     plt.axis('off')
plt.subplot(2,3,6), plt.title('b'),      plt.imshow(b,cmap='gray'),     plt.axis('off')
plt.show()
```

### 5.3 裁剪图片 image.crop()

从原图片中裁剪感兴趣区域（roi),裁剪区域由4-tuple决定，该tuple中信息为(left, upper, right, lower)。 Pillow左边系统的原点（0，0）为图片的左上角。坐标中的数字单位为像素点。

```python
from PIL import Image
import matplotlib.pyplot as plt
image=Image.open('d:/ex.jpg')  #打开图像

plt.figure(figsize=(10,8))
plt.subplot(1,2,1), plt.title('origin')
plt.imshow(image),plt.axis('off')

#box变量是一个四元组(左，上，右，下)。 
box=(80,100,260,300)
roi=image.crop(box)
plt.subplot(1,2,2)
plt.title('roi')
plt.imshow(roi)
plt.axis('off')
plt.show()
```

用plot绘制显示出图片后，将鼠标移动到图片上，会在右下角出现当前点的坐标，以及像素值。

### 5.4 几何变换  image.resize((宽,高))、image.rotate(逆时针角度表示)
 Image类有resize()、rotate()和transpose()方法进行几何变换。
 图像的缩放和旋转

```python
plt.figure(figsize=(10,8))
#                      (宽,高)
resize = image.resize((900, 1280))
plt.imshow(resize)
plt.axis('off')
plt.show()

plt.figure(figsize=(10,8))
rotate = image.rotate(45)
plt.imshow(rotate)
plt.axis('off')
plt.show()
```

### 5.5 转换图像 image.transpose()

**transpose()和rotate()没有性能差别。**

参数:

- Image.FLIP_LEFT_RIGHT
- Image.FLIP_TOP_BOTTOM
- Image.ROTATE_90
- Image.ROTATE_180
- Image.ROTATE_270

```python
dst = image.transpose(Image.FLIP_LEFT_RIGHT) 	#左右互换
dst = image.transpose(Image.FLIP_TOP_BOTTOM) 	#上下互换
dst = image.transpose(Image.ROTATE_90)  		#顺时针旋转
dst = image.transpose(Image.ROTATE_180)
dst = image.transpose(Image.ROTATE_270)
```

```python
left_right = image.transpose(Image.FLIP_LEFT_RIGHT) 	#左右互换
top_bottom = image.transpose(Image.FLIP_TOP_BOTTOM) 	#上下互换

plt.figure(figsize=(10,8))
plt.subplot(1,2,1)
plt.title('left_right')
plt.imshow(left_right)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('top_bottom')
plt.imshow(top_bottom)
plt.axis('off')
plt.show()
```



## 6 python图像处理库Image模块

### 6.1 创建一个新的图片 Image.new()

参数:

- mode: "1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"
- size: (宽, 高)
- color: float / 文字如'red' / (0~255, 0~255, 0~255)

```python
Image.new(mode, size)  
Image.new(mode, size, color)  

image = Image.new('RGB', (900, 600), 100)
plt.figure(figsize=(9, 6))
plt.imshow(image)
plt.show()

image = Image.new('RGB', (900, 600), 'red')
plt.figure(figsize=(9, 6))
plt.imshow(image)
plt.show()

image = Image.new('RGB', (900, 600), (0, 255, 0))
plt.figure(figsize=(9, 6))
plt.imshow(image)
plt.show()
```

### 6.2 层叠图片 Image.blend(image1, image2, alpha) 

层叠两个图片，image1和image2, 

alpha是一个介于[0,1]的浮点数

- 如果为0，  效果为image1

- 如果为1.0，效果为image2

当然image1和image2的尺寸和模式必须相同。这个函数可以做出很漂亮的效果来，而图形的算术加减后边会说到。

```python
Image.blend(image1, image2, alpha)  

blend1 = Image.blend(image1, image2, 0.7) 
plt.figure(figsize=(9, 6))
plt.imshow(blend1)
plt.show()
```

### 6.3 蒙板 Image.composite(image1, image2, mask)

composite可以使用另外一个图片作为蒙板(mask)，所有的这三张图片必须具备相同的尺寸，mask图片的模式可以为“1”，“L”，“RGBA”

```python
Image.composite(image1, image2, mask) 

composite = Image.composite(image3, image3, mask) 
plt.figure(figsize=(9, 6))
plt.imshow(composite)
plt.show()
```

## 7 添加水印

### 7.1 添加文字水印

```csharp
from PIL import Image, ImageDraw, ImageFont

image = Image.open('./image/71479714_p0.jpg').convert('RGBA')
txt=Image.new('RGBA', image.size, (0,0,0,0))
fnt=ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
d=ImageDraw.Draw(txt)
d.text((txt.size[0]-80,txt.size[1]-30), "cnBlogs",font=fnt, fill=(255,255,255,255))
out=Image.alpha_composite(image, txt)
    
plt.figure(figsize=(10,8))
plt.imshow(out)
plt.axis('off')
plt.show()
```

### 7.2 添加小图片水印

```kotlin
mark=Image.open('./image/71479714_p0.jpg')
layer=Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-150,im.size[1]-60))
out=Image.composite(layer, image, layer)

plt.figure(figsize=(10,8))
plt.imshow(out)
plt.axis('off')
plt.show()
```

## 8 PIL Image 图像互转 numpy 数组

### 8.1 将 PIL Image 图片转换为 numpy 数组 np.array(image)

```cpp
img = np.array(image)
# 也可以用 np.asarray(image) 区别是 np.array() 是深拷贝，np.asarray() 是浅拷贝
```

更多细节见[python中的深拷贝与浅拷贝](https://link.jianshu.com?t=http://blog.csdn.net/jiandanjinxin/article/details/78214133)

### 8.2 numpy image 查看图片信息 .shape .dtype

```python
print(img.shape)
print(img.dtype)
```

### 8.3 将 numpy 数组转换为 PIL 图片 Image.fromarray(数组)

**这里采用 matplotlib.image 读入图片数组，注意这里读入的数组是 float32 型的，范围是 0-1，而 PIL.Image 数据是 uinit8 型的，范围是0-255*，所以要进行转换：**

```python
import matplotlib.image as mpimage
from PIL import Image
lena = mpimage.imread('lena.png') # 这里读入的数据是 float32 型的，范围是0-1
im = Image.fromarray(np.uinit8(lena*255))
im.show()
```



## 9 图像中的像素访问 numpy

前面的一些例子中，我们都是利用Image.open（）来打开一幅图像，然后直接对这个PIL对象进行操作。如果只是简单的操作还可以，但是如果操作稍微复杂一些，就比较吃力了。因此，通常我们加载完图片后，都是把图片转换成矩阵来进行更加复杂的操作。
 打开图像并转化为矩阵，并显示

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image=np.array(Image.open('d:/lena.jpg'))  #打开图像并转化为数字矩阵
plt.figure("dog")
plt.imshow(image)
plt.axis('off')
plt.title('The image title')
plt.show()
```

调用numpy中的array（）函数就可以将PIL对象转换为数组对象。

## 10 查看图片信息，可用如下的方法

**PIL image 查看图片信息，可用如下的方法**

```python
print(type(image))
print(image.size)  				#图片的尺寸
print(image.mode)  				#图片的模式
print(image.format)  			#图片的格式
print(image.getpixel((0,0)))	#得到像素：
#image读出来的图片获得某点像素用getpixel((w,h))可以直接返回这个点三个通道的像素值
```

**numpy image 查看图片信息，可用如下的方法**

```python
print(image.shape)
print(image.dtype)
```

如果是RGB图片，那么转换为array之后，就变成了一个rows*cols*channels的三维矩阵,因此，我们可以使用

```css
image[i,j,k]
```

来访问像素值。
 例1：打开图片，并随机添加一些椒盐噪声

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image = Image.open('./image/71479714_p0.jpg')
img = np.array(image)

#随机生成5000个椒盐
rows, cols, dims = img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255

plt.figure(figsize=(9, 16))
#         直接使用numpy数组就能输出
plt.imshow(noise_img)
plt.axis('off')
plt.show()
```

例2：将图像二值化，像素值大于128的变为1，否则变为0

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
    
image = Image.open('./image/71479714_p0.jpg')
#                 黑白图片
image = image.convert('L')
img = np.array(image)

    
rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
        if (img[i,j]<=128):
            img[i,j]=0
        else:
            img[i,j]=1


plt.figure(figsize=(9, 16))
plt.imshow(two_img,cmap='gray')
plt.axis('off')
plt.show()
```

如果要对多个像素点进行操作，可以使用数组切片方式访问。切片方式返回的是以指定间隔下标访问 该数组的像素值。

下面是有关灰度图像的一些例子：

```python
image[i,:] = im[j,:] 	# 将第 j 行的数值赋值给第 i 行
image[:,i] = 100 		# 将第 i 列的所有数值设为 100
image[:100,:50].sum() 	# 计算前 100 行、前 50 列所有数值的和
image[50:100,50:100] 	# 50~100 行，50~100 列（不包括第 100 行和第 100 列）
image[i].mean() 		# 第 i 行所有数值的平均值
image[:,-1] 			# 最后一列
image[-2,:] (or im[-2]) # 倒数第二行
```

## 10 直接操作像素点

不但可以对每个像素点进行操作，而且，每一个通道都可以独立的进行操作。比如，将每个像素点的亮度(不知道有没有更专业的词)增大20%

```csharp
out = image.point(lambda i : i * 1.2)
#注意这里用到一个匿名函数(那个可以把i的1.2倍返回的函数)  
argument * scale + offset  
e.g  
out = image.point(lambda i: i*1.2 + 10)
```

## 11 图像直方图

我们先来看两个函数reshape和flatten:

假设我们先生成一个一维数组：

```python
vec=np.arange(15)
print vec
```

如果我们要把这个一维数组，变成一个3*5二维矩阵，我们可以使用reshape来实现

```python
mat= vec.reshape(3,5)
print mat
```

现在如果我们返过来，知道一个二维矩阵，要变成一个一维数组，就不能用reshape了，只能用flatten. 我们来看两者的区别

```python
a1=mat.reshape(1,-1)  #-1表示为任意，让系统自动计算
print a1
a2=mat.flatten()
print a2
```

可以看出，用reshape进行变换，实际上变换后还是二维数组，两个方括号，因此只能用flatten.

我们要对图像求直方图，就需要先把图像矩阵进行flatten操作，使之变为一维数组，然后再进行统计

**画灰度图直方图**
 绘图都可以调用matplotlib.pyplot库来进行，其中的hist函数可以直接绘制直方图。
 调用方式：

```python
n, bins, patches = plt.hist(arr, bins=50, normed=1, facecolor='green', alpha=0.75)
```

hist的参数非常多，但常用的就这五个，只有第一个是必须的，后面四个可选

```python
arr: 需要计算直方图的一维数组
bins: 直方图的柱数，可选项，默认为10
normed: 是否将得到的直方图向量归一化。默认为0
facecolor: 直方图颜色
alpha: 透明度
```

返回值 ：

```cpp
n: 直方图向量，是否归一化由参数设定
bins: 返回各个bin的区间范围
patches: 返回每个bin里面包含的数据，是一个list
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image=np.array(Image.open('d:/pic/lena.jpg').convert('L'))

plt.figure("lena")
arr=image.flatten()
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)  
plt.title('The image title')
plt.show()
```

**彩色图片直方图**
 实际上是和灰度直方图一样的，只是分别画出三通道的直方图，然后叠加在一起。

```dart
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
src=Image.open('d:/ex.jpg')
r,g,b=src.split()
plt.figure("lena")
ar=np.array(r).flatten()
plt.hist(ar, bins=256, normed=1,facecolor='r',edgecolor='r',hold=1)
ag=np.array(g).flatten()
plt.hist(ag, bins=256, normed=1, facecolor='g',edgecolor='g',hold=1)
ab=np.array(b).flatten()
plt.hist(ab, bins=256, normed=1, facecolor='b',edgecolor='b')
plt.title('The image title')
plt.show()
```

由此可见，matplotlib的画图功能是非常强大的，直方图只是其中非常小的一部分，更多的请参看官方文档：
 [http://matplotlib.org/api/pyplot_summary.html](https://link.jianshu.com?t=http://matplotlib.org/api/pyplot_summary.html)

## PIL 6 ImageDraw, ImageFont

```python
'''
无法导入: 将PIL文件夹放到项目目录即可
'''

import os
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont

image = Image.open('./image/71479714_p0.jpg')


# 画图 ImageDraw
draw = ImageDraw.Draw(image)
#获取图像的宽和高
width, height = image.size

# 文字字体 ImageFont
#选择文字字体和大小
setFont = ImageFont.truetype('C:/windows/fonts/Dengl.ttf', 20)
#设置文字颜色
fillColor = "blue"
#写入文字
draw.text((40, height - 100), u'黄前久美子,黄大叔', font=setFont, fill=fillColor)

plt.figure(figsize=(9,16))
plt.axis('off') # 不显示坐标轴
plt.imshow(image)
plt.show()
```





# Python如何读取指定文件夹下的所有图像

```python
'''
Load the image files form the folder
input:
    imageDir: the direction of the folder
    imageName:the name of the folder
output:
    data:the data of the dataset
    label:the label of the datset
'''
def load_image(imageDir,imageFoldName):
    images = os.listdir(imageDir+imageFoldName)
    imageNum = len(images)
    data = np.empty((imageNum,1,12,12),dtype="float32")
    label = np.empty((imageNum,),dtype="uint8")
    for i in range (imageNum):
        image = Image.open(imageDir+imageFoldName+"/"+images[i])
        arr = np.asarray(image,dtype="float32")
        data[i,:,:,:] = arr
        label[i] = int(images[i].split('.')[0])
    return data,label
```

**调用方式**

```kotlin
craterDir = "./data/Craterimage/Adjust/"
foldName = "East_CraterAdjust12"
data, label = load_image(craterDir,foldName)
```

------

# Python图形图像处理库ImageEnhance模块图像增强

可以使用ImageEnhance模块，其中包含了大量的预定义的图片加强方式
 加强器包括，色彩平衡，亮度平衡，对比度，锐化度等。通过使用这些加强器，可以很轻松的做到图片的色彩调整，亮度调整，锐化等操作，google picasa中提供的一些基本的图片加强功能都可以实现。

**颜色加强color**用于调整图片的色彩平衡，相当于彩色电视机的色彩调整。这个类实现了上边提到的接口的enhance方法。

```bash
ImageEnhance.Color(image)#获得色彩加强器实例  
```

然后即可使用enhance(factor)方法进行调整。

**亮度加强brightness**用于调整图片的明暗平衡。

```bash
ImageEnhance.Brightness(image)#获得亮度加强器实例  
```

factor=1返回一个黑色的图片对象，0返回原始图片对象

**对比度加强contrast**用于调整图片的对比度，相当于彩色电视机的对比度调整。

```bash
ImageEnhance.Contrast(image) #获得对比度加强器实例  
import ImageEnhance  
enh = ImageEnhance.Contrast(im)  
enh.ehhance(1.5).show("50% more contrast")
```

**锐化度加强sharpness**用于锐化/钝化图片。

```bash
ImageEnhance.Sharpness(image) #返回锐化加强器实例  
```

应该注意的是锐化操作的factor是一个0-2的浮点数，当factor=0时，返回一个完全模糊的图片对象，当factor=1时，返回一个完全锐化的图片对象，factor=1时，返回原始图片对象

------

# Python图像处理库ImageChops模块

这个模块主要包括对图片的算术运算，叫做通道运算(channel operations)。这个模块可以用于多种途径，包括一些特效制作，图片整合，算数绘图等等方面。
 **Invert:**

```css
ImageChops.invert(image) 
```

图片反色，类似于集合操作中的求补集，最大值为Max，每个像素做减法，取出反色.
 **公式**

```csharp
out = MAX - image
```

**lighter:**

```css
ImageChops.lighter(image1, image2)  
```

**darker:**

```css
ImageChops.darker(image1, image2)  
```

**difference**

```css
ImageChops.difference(image1, image2)
```

求出两张图片的绝对值，逐像素的做减法
 **multiply**

```css
ImageChops.multiply(image1, image2)
```

将两张图片互相叠加，如果用纯黑色与某图片进行叠加操作，会得到一个纯黑色的图片。如果用纯白色与图片作叠加，图片不受影响。
 计算的公式如下公式

```csharp
out = image1 * image2 / MAX
```

**screen:**

```css
ImageChops.screen(image1, image2)  
```

先反色，后叠加。
 公式

```csharp
out = MAX - ((MAX - image1) * (MAX - image2) / MAX)
```

**add:**

```csharp
ImageChops.add(image1, image2, scale, offset)  
```

对两张图片进行算术加法，按照一下公式进行计算
 公式

```csharp
out = (image1+image2) / scale + offset
```

如果尺度和偏移被忽略的化，scale=1.0, offset=0.0即
 out = image1 + image2
 **subtract:**

```css
ImageChops.subtract(image1, image2, scale, offset)  
```

对两张图片进行算术减法：
 公式

```csharp
out = (image1-image2) / scale + offset
```

------

# Python图形图像处理库ImageFilter模块图像滤镜

ImageFilter是PIL的滤镜模块，通过这些预定义的滤镜，可以方便的对图片进行一些过滤操作，从而去掉图片中的噪音(部分的消除)，这样可以降低将来处理的复杂度(如模式识别等)。

```css
滤镜名称                      		含义
ImageFilter.BLUR          		模糊滤镜
ImageFilter.CONTOUR       		轮廓
ImageFilter.EDGE_ENHANCE    	边界加强
ImageFilter.EDGE_ENHANCE_MORE   边界加强(阀值更大)
ImageFilter.EMBOSS              浮雕滤镜
ImageFilter.FIND_EDGES         	边界滤镜
ImageFilter.SMOOTH              平滑滤镜
ImageFilter.SMOOTH_MORE      	平滑滤镜(阀值更大)
ImageFilter.SHARPEN             锐化滤镜
```

要使用PIL的滤镜功能，需要引入ImageFilter模块

```python
import Image, ImageFilter  
  
def inHalf(image):  
    w,h = image.size  
    return image.resize((w/2, h/2))  
  
def filterDemo():  
    image = Image.open("sandstone_half.jpg")  
    #image = inHalf(image)  
    imagefilted = image.filter(ImageFilter.SHARPEN)  
    #imagefilted.show()  
    imagefilted.save("sandstone_sharpen.jpg")  
  
if __name__ == "__main__":  
    filterDemo()  
```