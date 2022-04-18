from tkinter import *
import numpy as np
from scipy.stats import weibull_min

root = Tk()
root.title('蒙特卡洛模拟器')
root.geometry('1024x540')

def Simulation():
    stress_type = stress.get()
    intensity_type = Intensity.get()
    time = times.get()
    if time != '0':  #防止输入次数为0
        time = int(time)#str转int，time为模拟次数
        stress_num = 0
        insity_num = 0
        sum = 0
        #判断应力、强度的分布类型
        if stress_type == 0 and intensity_type == 0:
            for i in range(time):
                mean_stress = norm_para_mean11.get()
                std_stress = norm_para_std11.get()
                stress_num = np.random.normal(loc=int(mean_stress),scale=int(std_stress))
                mean_insity = norm_para_mean21.get()
                std_insity = norm_para_std21.get()
                insity_num = np.random.normal(loc=int(mean_insity),scale=int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 0 and intensity_type == 1:
            for i in range(time):
                mean_stress = norm_para_mean11.get()
                std_stress = norm_para_std11.get()
                stress_num = np.random.normal(loc=int(mean_stress),scale=int(std_stress))
                lamda_insity=expo_para_lamda2.get()
                insity_num = np.random.exponential(scale=int(lamda_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 0 and intensity_type == 2:
            for i in range(time):
                mean_stress = norm_para_mean11.get()
                std_stress = norm_para_std11.get()
                stress_num = np.random.normal(loc=int(mean_stress),scale=int(std_stress))
                shape=wei_para_m2.get()
                Scale=wei_para_scale2.get()
                Loc=wei_para_r2.get()
                insity_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 0 and intensity_type == 3:
            for i in range(time):
                mean_stress = norm_para_mean11.get()
                std_stress = norm_para_std11.get()
                stress_num = np.random.normal(loc=int(mean_stress),scale=int(std_stress))
                mean_insity=norm_para_mean22.get()
                std_insity=norm_para_std22.get()
                insity_num = np.random.lognormal(int(mean_insity),int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 1 and intensity_type == 0:
            for i in range(time):
                lamda_stress=expo_para_lamda1.get()
                stress_num = np.random.exponential(scale=int(lamda_stress))
                mean_insity = norm_para_mean21.get()
                std_insity = norm_para_std21.get()
                insity_num = np.random.normal(loc=int(mean_insity),scale=int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 1 and intensity_type == 1:
            for i in range(time):
                lamda_stress=expo_para_lamda1.get()
                stress_num = np.random.exponential(scale=int(lamda_stress))
                lamda_insity=expo_para_lamda2.get()
                insity_num = np.random.exponential(scale=int(lamda_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 1 and intensity_type == 2:
            for i in range(time):
                lamda_stress=expo_para_lamda1.get()
                stress_num = np.random.exponential(scale=int(lamda_stress))
                shape=wei_para_m2.get()
                Scale=wei_para_scale2.get()
                Loc=wei_para_r2.get()
                insity_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 1 and intensity_type == 3:
            for i in range(time):
                lamda_stress=expo_para_lamda1.get()
                stress_num = np.random.exponential(scale=int(lamda_stress))
                mean_insity=norm_para_mean22.get()
                std_insity=norm_para_std22.get()
                insity_num = np.random.lognormal(int(mean_insity),int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 2 and intensity_type == 0:
            for i in range(time):
                shape=wei_para_m1.get()
                Scale=wei_para_scale1.get()
                Loc=wei_para_r1.get()
                stress_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                mean_insity = norm_para_mean21.get()
                std_insity = norm_para_std21.get()
                insity_num = np.random.normal(loc=int(mean_insity),scale=int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 2 and intensity_type == 1:
            for i in range(time):
                shape=wei_para_m1.get()
                Scale=wei_para_scale1.get()
                Loc=wei_para_r1.get()
                stress_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                lamda_insity=expo_para_lamda2.get()
                insity_num = np.random.exponential(scale=int(lamda_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 2 and intensity_type == 2:
            for i in range(time):
                shape=wei_para_m1.get()
                Scale=wei_para_scale1.get()
                Loc=wei_para_r1.get()
                stress_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                shape=wei_para_m2.get()
                Scale=wei_para_scale2.get()
                Loc=wei_para_r2.get()
                insity_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 2 and intensity_type == 3:
            for i in range(time):
                shape=wei_para_m1.get()
                Scale=wei_para_scale1.get()
                Loc=wei_para_r1.get()
                stress_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                mean_insity=norm_para_mean22.get()
                std_insity=norm_para_std22.get()
                insity_num = np.random.lognormal(int(mean_insity),int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 3 and intensity_type == 0:
            for i in range(time):
                mean_stress=norm_para_mean21.get()
                std_stress =norm_para_std21.get()
                insity_num = np.random.lognormal(int(mean_stress),int(std_stress))
                mean_insity = norm_para_mean21.get()
                std_insity = norm_para_std21.get()
                insity_num = np.random.normal(loc=int(mean_insity),scale=int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 3 and intensity_type == 1:
            for i in range(time):
                mean_stress=norm_para_mean21.get()
                std_stress =norm_para_std21.get()
                insity_num = np.random.lognormal(int(mean_stress),int(std_stress))
                lamda_insity=expo_para_lamda2.get()
                insity_num = np.random.exponential(scale=int(lamda_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 3 and intensity_type == 2:
            for i in range(time):
                mean_stress=norm_para_mean21.get()
                std_stress =norm_para_std21.get()
                insity_num = np.random.lognormal(int(mean_stress),int(std_stress))
                shape=wei_para_m2.get()
                Scale=wei_para_scale2.get()
                Loc=wei_para_r2.get()
                insity_num = weibull_min.rvs(int(shape), loc=int(Loc), scale=int(Scale), size=1)
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
        elif stress_type == 3 and intensity_type == 3:
            for i in range(time):
                mean_stress=norm_para_mean21.get()
                std_stress =norm_para_std21.get()
                insity_num = np.random.lognormal(int(mean_stress),int(std_stress))
                mean_insity=norm_para_mean22.get()
                std_insity=norm_para_std22.get()
                insity_num = np.random.lognormal(int(mean_insity),int(std_insity))
                if stress_num < insity_num:
                    sum +=1
            result_num = sum/time
            result.config(text = result_num)
    else:
        result.config(text = 0)


def ExitSystem():
    root.destroy()

#选择一个选项之后设置对应参数可编辑
def StressFunctionSelection(norm_para_mean11,norm_para_std11,expo_para_lamda1,wei_para_m1,wei_para_scale1,wei_para_r1,norm_para_mean12,norm_para_std12):
    num = stress.get()
    if num == 0:
        norm_para_mean11.config(state = 'normal')
        norm_para_std11.config(state = 'normal')
        expo_para_lamda1.config(textvariable = StringVar(''))
        expo_para_lamda1.config(state = 'readonly')
        wei_para_m1.config(textvariable = StringVar(''))
        wei_para_m1.config(state = 'readonly')
        wei_para_scale1.config(textvariable =StringVar(''))
        wei_para_scale1.config(state = 'readonly')
        wei_para_r1.config(textvariable =StringVar(''))
        wei_para_r1.config(state = 'readonly')
        norm_para_mean12.config(textvariable =StringVar(''))
        norm_para_mean12.config(state = 'readonly')
        norm_para_std12.config(textvariable = StringVar(''))
        norm_para_std12.config(state = 'readonly')
    elif num == 1:
        norm_para_mean11.config(textvariable = StringVar(''))
        norm_para_mean11.config(state = 'readonly')
        norm_para_std11.config(textvariable = StringVar(''))
        norm_para_std11.config(state = 'readonly')
        expo_para_lamda1.config(state = 'normal')
        wei_para_m1.config(textvariable = StringVar(''))
        wei_para_m1.config(state = 'readonly')
        wei_para_scale1.config(textvariable = StringVar(''))
        wei_para_scale1.config(state = 'readonly')
        wei_para_r1.config(textvariable = StringVar(''))
        wei_para_r1.config(state = 'readonly')
        norm_para_mean12.config(textvariable = StringVar(''))
        norm_para_mean12.config(state = 'readonly')
        norm_para_std12.config(textvariable = StringVar(''))
        norm_para_std12.config(state = 'readonly')
    elif num == 2:
        norm_para_mean11.config(textvariable = StringVar(''))
        norm_para_mean11.config(state = 'readonly')
        norm_para_std11.config(textvariable = StringVar(''))
        norm_para_std11.config(state = 'readonly')
        expo_para_lamda1.config(textvariable = StringVar(''))
        expo_para_lamda1.config(state = 'readonly')
        wei_para_m1.config(state = 'normal')
        wei_para_scale1.config(state = 'normal')
        wei_para_r1.config(state = 'normal')
        norm_para_mean12.config(textvariable = StringVar(''))
        norm_para_mean12.config(state = 'readonly')
        norm_para_std12.config(textvariable = StringVar(''))
        norm_para_std12.config(state = 'readonly')
    elif num == 3:
        norm_para_mean11.config(textvariable = StringVar(''))
        norm_para_mean11.config(state = 'readonly')
        norm_para_std11.config(textvariable = StringVar(''))
        norm_para_std11.config(state = 'readonly')
        expo_para_lamda1.config(textvariable = StringVar(''))
        expo_para_lamda1.config(state = 'readonly')
        wei_para_m1.config(textvariable = StringVar(''))
        wei_para_m1.config(state = 'readonly')
        wei_para_scale1.config(textvariable = StringVar(''))
        wei_para_scale1.config(state = 'readonly')
        wei_para_r1.config(textvariable = StringVar(''))
        wei_para_r1.config(state = 'readonly')
        norm_para_mean12.config(state = 'normal')
        norm_para_std12.config(state = 'normal')

def IntensityFunctionSelection(norm_para_mean21,norm_para_std21,expo_para_lamda2,wei_para_m2,wei_para_scale2,wei_para_r2,norm_para_mean22,norm_para_std22):
    num = Intensity.get()
    if num == 0:
        norm_para_mean21.config(state = 'normal')
        norm_para_std21.config(state = 'normal')
        expo_para_lamda2.config(textvariable = StringVar(''))
        expo_para_lamda2.config(state = 'readonly')
        wei_para_m2.config(textvariable = StringVar(''))
        wei_para_m2.config(state = 'readonly')
        wei_para_scale2.config(textvariable =StringVar(''))
        wei_para_scale2.config(state = 'readonly')
        wei_para_r2.config(textvariable =StringVar(''))
        wei_para_r2.config(state = 'readonly')
        norm_para_mean22.config(textvariable =StringVar(''))
        norm_para_mean22.config(state = 'readonly')
        norm_para_std22.config(textvariable = StringVar(''))
        norm_para_std22.config(state = 'readonly')
    elif num == 1:
        norm_para_mean21.config(textvariable = StringVar(''))
        norm_para_mean21.config(state = 'readonly')
        norm_para_std21.config(textvariable = StringVar(''))
        norm_para_std21.config(state = 'readonly')
        expo_para_lamda2.config(textvariable = StringVar(''))
        expo_para_lamda2.config(state = 'normal')
        wei_para_m2.config(textvariable = StringVar(''))
        wei_para_m2.config(state = 'readonly')
        wei_para_scale2.config(textvariable =StringVar(''))
        wei_para_scale2.config(state = 'readonly')
        wei_para_r2.config(textvariable =StringVar(''))
        wei_para_r2.config(state = 'readonly')
        norm_para_mean22.config(textvariable =StringVar(''))
        norm_para_mean22.config(state = 'readonly')
        norm_para_std22.config(textvariable = StringVar(''))
        norm_para_std22.config(state = 'readonly')
    elif num == 2:
        norm_para_mean21.config(textvariable = StringVar(''))
        norm_para_mean21.config(state = 'readonly')
        norm_para_std21.config(textvariable = StringVar(''))
        norm_para_std21.config(state = 'readonly')
        expo_para_lamda2.config(textvariable = StringVar(''))
        expo_para_lamda2.config(state = 'readonly')
        wei_para_m2.config(textvariable = StringVar(''))
        wei_para_m2.config(state = 'normal')
        wei_para_scale2.config(textvariable =StringVar(''))
        wei_para_scale2.config(state = 'normal')
        wei_para_r2.config(textvariable =StringVar(''))
        wei_para_r2.config(state = 'normal')
        norm_para_mean22.config(textvariable =StringVar(''))
        norm_para_mean22.config(state = 'readonly')
        norm_para_std22.config(textvariable = StringVar(''))
        norm_para_std22.config(state = 'readonly')
    elif num == 3:
        norm_para_mean21.config(textvariable = StringVar(''))
        norm_para_mean21.config(state = 'readonly')
        norm_para_std21.config(textvariable = StringVar(''))
        norm_para_std21.config(state = 'readonly')
        expo_para_lamda2.config(textvariable = StringVar(''))
        expo_para_lamda2.config(state = 'readonly')
        wei_para_m2.config(textvariable = StringVar(''))
        wei_para_m2.config(state = 'readonly')
        wei_para_scale2.config(textvariable =StringVar(''))
        wei_para_scale2.config(state = 'readonly')
        wei_para_r2.config(textvariable =StringVar(''))
        wei_para_r2.config(state = 'readonly')
        norm_para_mean22.config(textvariable =StringVar(''))
        norm_para_mean22.config(state = 'normal')
        norm_para_std22.config(textvariable = StringVar(''))
        norm_para_std22.config(state = 'normal')

#应力边框
StressFrameStyle = Frame(root,relief=GROOVE,width=1000,height=200,borderwidth=2)#脊状边缘的
StressFrameStyle.place(x=5,y=15,width=1000,height=200)
Label(StressFrameStyle, text='应力').pack()

#强度边框
IntensityFrameStyle = Frame(root,relief=GROOVE,width=1000,height=200,borderwidth=2)#脊状边缘的
IntensityFrameStyle.place(x=5,y=230,width=1000,height=200)
Label(IntensityFrameStyle, text='强度').pack()

#应力函数选择
StressFunction = Frame(StressFrameStyle,relief=GROOVE,width=240,height=190,borderwidth=2)
StressFunction.place(x=5,y=20,width=150,height=160)

Label(StressFunction, text='请选择应力服从的分布:').grid(row=1)
stress = IntVar()
rd1 = Radiobutton(StressFunction,text="正态分布",variable=stress,value=0,command= lambda:StressFunctionSelection(norm_para_mean11,norm_para_std11,expo_para_lamda1,wei_para_m1,wei_para_scale1,wei_para_r1,norm_para_mean12,norm_para_std12))
rd1.grid(row=2)
rd2 = Radiobutton(StressFunction,text="指数分布",variable=stress,value=1,command=lambda:StressFunctionSelection(norm_para_mean11,norm_para_std11,expo_para_lamda1,wei_para_m1,wei_para_scale1,wei_para_r1,norm_para_mean12,norm_para_std12))
rd2.grid(row=3)
rd3 = Radiobutton(StressFunction,text="韦伯分布",variable=stress,value=2,command=lambda:StressFunctionSelection(norm_para_mean11,norm_para_std11,expo_para_lamda1,wei_para_m1,wei_para_scale1,wei_para_r1,norm_para_mean12,norm_para_std12))
rd3.grid(row=4)
rd3 = Radiobutton(StressFunction,text="对数正态分布",variable=stress,value=3,command=lambda:StressFunctionSelection(norm_para_mean11,norm_para_std11,expo_para_lamda1,wei_para_m1,wei_para_scale1,wei_para_r1,norm_para_mean12,norm_para_std12))
rd3.grid(row=5)

#正态分布参数
NormalDistributionStress= Frame(StressFrameStyle,relief=GROOVE,width=240,height=190)
NormalDistributionStress.place(x=160,y=20,width=200,height=160)
Label(NormalDistributionStress, text='请输入分布的参数:').pack()
Label(NormalDistributionStress, text='正态分布:').pack()
mean11=Label(NormalDistributionStress, text=chr(956).lower()+':').place(x=10,y=40)
norm_para_mean11 = Entry(NormalDistributionStress,width=50)
norm_para_mean11.place(x=10,y=65,width=180)
norm_para_mean11.config(state = 'normal')
std11=Label(NormalDistributionStress, text=chr(963).lower()+':').place(x=10,y=90)
norm_para_std11 = Entry(NormalDistributionStress,width=50)
norm_para_std11.place(x=10,y=120,width=180)
norm_para_std11.config(state = 'normal')
#指数分布参数
ExponentialDistributionStress= Frame(StressFrameStyle,relief=GROOVE,width=240,height=190)
ExponentialDistributionStress.place(x=365,y=20,width=200,height=160)
Label(ExponentialDistributionStress, text='').pack()
Label(ExponentialDistributionStress, text='指数分布:').pack()
lamda1=Label(ExponentialDistributionStress, text=chr(955).lower()+':').place(x=10,y=40)
expo_para_lamda1 = Entry(ExponentialDistributionStress,width=50)
expo_para_lamda1.place(x=10,y=65,width=180)
expo_para_lamda1.config(state = 'readonly')

#韦伯分布参数
WeibullDistributionStress= Frame(StressFrameStyle,relief=GROOVE,width=240,height=190)
WeibullDistributionStress.place(x=570,y=20,width=200,height=160)
Label(WeibullDistributionStress, text='').pack()
Label(WeibullDistributionStress, text='韦伯分布:').pack()
m1=Label(WeibullDistributionStress, text='m:').place(x=10,y=60)
wei_para_m1 = Entry(WeibullDistributionStress,width=50)
wei_para_m1.place(x=35,y=60,width=150)
wei_para_m1.config(state = 'readonly')
lamda1=Label(WeibullDistributionStress, text=chr(952).lower()+'-r:').place(x=10,y=90)
wei_para_scale1 = Entry(WeibullDistributionStress,width=50)
wei_para_scale1.place(x=35,y=90,width=150)
wei_para_scale1.config(state = 'readonly')
lamda1=Label(WeibullDistributionStress, text='r:').place(x=10,y=120)
wei_para_r1 = Entry(WeibullDistributionStress,width=50)
wei_para_r1.place(x=35,y=120,width=150)
wei_para_r1.config(state = 'readonly')

#对数正态分布参数
LogNormalDistributionStress= Frame(StressFrameStyle,relief=GROOVE,width=240,height=190)
LogNormalDistributionStress.place(x=775,y=20,width=200,height=160)
Label(LogNormalDistributionStress, text='').pack()
Label(LogNormalDistributionStress, text='对数正态分布:').pack()
mean12=Label(LogNormalDistributionStress, text=chr(956).lower()+':').place(x=10,y=40)
norm_para_mean12 = Entry(LogNormalDistributionStress,width=50)
norm_para_mean12.place(x=10,y=65,width=180)
norm_para_mean12.config(state = 'readonly')
std12=Label(LogNormalDistributionStress, text=chr(963).lower()+':').place(x=10,y=90)
norm_para_std12 = Entry(LogNormalDistributionStress,width=50)
norm_para_std12.place(x=10,y=120,width=180)
norm_para_std12.config(state = 'readonly')


#强度函数选择
IntensityFunction = Frame(IntensityFrameStyle,relief=GROOVE,width=240,height=190,borderwidth=2)
IntensityFunction.place(x=5,y=20,width=150,height=160)

Label(IntensityFunction, text='请选择强度服从的分布:').grid(row=1)
Intensity = IntVar()
rd1 = Radiobutton(IntensityFunction,text="正态分布",variable=Intensity,value=0,command= lambda:IntensityFunctionSelection(norm_para_mean21,norm_para_std21,expo_para_lamda2,wei_para_m2,wei_para_scale2,wei_para_r2,norm_para_mean22,norm_para_std22))
rd1.grid(row=2)
rd2 = Radiobutton(IntensityFunction,text="指数分布",variable=Intensity,value=1,command= lambda:IntensityFunctionSelection(norm_para_mean21,norm_para_std21,expo_para_lamda2,wei_para_m2,wei_para_scale2,wei_para_r2,norm_para_mean22,norm_para_std22))
rd2.grid(row=3)
rd3 = Radiobutton(IntensityFunction,text="韦伯分布",variable=Intensity,value=2,command= lambda:IntensityFunctionSelection(norm_para_mean21,norm_para_std21,expo_para_lamda2,wei_para_m2,wei_para_scale2,wei_para_r2,norm_para_mean22,norm_para_std22))
rd3.grid(row=4)
rd3 = Radiobutton(IntensityFunction,text="对数正态分布",variable=Intensity,value=3,command= lambda:IntensityFunctionSelection(norm_para_mean21,norm_para_std21,expo_para_lamda2,wei_para_m2,wei_para_scale2,wei_para_r2,norm_para_mean22,norm_para_std22))
rd3.grid(row=5)
#正态分布参数
NormalDistributionIntensity= Frame(IntensityFrameStyle,relief=GROOVE,width=240,height=190)
NormalDistributionIntensity.place(x=160,y=20,width=200,height=160)
Label(NormalDistributionIntensity, text='请输入分布的参数:').pack()
Label(NormalDistributionIntensity, text='正态分布:').pack()
mean21=Label(NormalDistributionIntensity, text=chr(956).lower()+':').place(x=10,y=40)
norm_para_mean21 = Entry(NormalDistributionIntensity,width=50,state='normal')
norm_para_mean21.place(x=10,y=65,width=180)
std21=Label(NormalDistributionIntensity, text=chr(963).lower()+':').place(x=10,y=90)
norm_para_std21 = Entry(NormalDistributionIntensity,width=50,state='normal')
norm_para_std21.place(x=10,y=120,width=180)
#指数分布参数
ExponentialDistributionIntensity= Frame(IntensityFrameStyle,relief=GROOVE,width=240,height=190)
ExponentialDistributionIntensity.place(x=365,y=20,width=200,height=160)
Label(ExponentialDistributionIntensity, text='').pack()
Label(ExponentialDistributionIntensity, text='指数分布:').pack()
lamda2=Label(ExponentialDistributionIntensity, text=chr(955).lower()+':').place(x=10,y=40)
expo_para_lamda2 = Entry(ExponentialDistributionIntensity,width=50,state='readonly')
expo_para_lamda2.place(x=10,y=65,width=180)

#韦伯分布参数
WeibullDistributionIntensity= Frame(IntensityFrameStyle,relief=GROOVE,width=240,height=190)
WeibullDistributionIntensity.place(x=570,y=20,width=200,height=160)
Label(WeibullDistributionIntensity, text='').pack()
Label(WeibullDistributionIntensity, text='韦伯分布:').pack()

m2=Label(WeibullDistributionIntensity, text='m:').place(x=10,y=60)
wei_para_m2 = Entry(WeibullDistributionIntensity,width=50,state='readonly')
wei_para_m2.place(x=35,y=60,width=150)

lamda2=Label(WeibullDistributionIntensity, text=chr(952).lower()+'-r:').place(x=10,y=90)
wei_para_scale2 = Entry(WeibullDistributionIntensity,width=50,state='readonly')
wei_para_scale2.place(x=35,y=90,width=150)

lamda2=Label(WeibullDistributionIntensity, text='r:').place(x=10,y=120)
wei_para_r2 = Entry(WeibullDistributionIntensity,width=50,state='readonly')
wei_para_r2.place(x=35,y=120,width=150)

#对数正态分布参数
LogNormalDistributionIntensity= Frame(IntensityFrameStyle,relief=GROOVE,width=240,height=190)
LogNormalDistributionIntensity.place(x=775,y=20,width=200,height=160)
Label(LogNormalDistributionIntensity, text='').pack()
Label(LogNormalDistributionIntensity, text='对数正态分布:').pack()
mean22=Label(LogNormalDistributionIntensity, text=chr(956).lower()+':').place(x=10,y=40)
norm_para_mean22 = Entry(LogNormalDistributionIntensity,width=50,state='readonly')
norm_para_mean22.place(x=10,y=65,width=180)
std22=Label(LogNormalDistributionIntensity, text=chr(963).lower()+':').place(x=10,y=90)
norm_para_std22 = Entry(LogNormalDistributionIntensity,width=50,state='readonly')
norm_para_std22.place(x=10,y=120,width=180)


#模拟次数、可靠性、开始模拟、退出程序边框
FrameStyle1 = Frame(root,relief=GROOVE,width=1000,height=100,borderwidth=2)#脊状边缘的
FrameStyle1.place(x=5,y=435,width=250,height=100)
Label(FrameStyle1, text='模拟次数').pack()
#IniNum = StringVar(value=1)
times = Entry(FrameStyle1,width=50,state='normal')#输入可能不为数字
times.place(x=70,y=40,width=100)

FrameStyle2 = Frame(root,relief=GROOVE,width=1000,height=100,borderwidth=2)#脊状边缘的
FrameStyle2.place(x=260,y=435,width=250,height=100)
Label(FrameStyle2, text='模拟可靠度结果为：').pack()
result = Label(FrameStyle2)
result.place(x=70,y=40)

FrameStyle3 = Frame(root,relief=RAISED,width=1000,height=100,borderwidth=2)#脊状边缘的
FrameStyle3.place(x=530,y=440,width=200,height=80)
Button(FrameStyle3, text='开始模拟',command=Simulation).pack(side=BOTTOM, padx="12p",pady="20p")
FrameStyle4 = Frame(root,relief=RAISED,width=1000,height=100,borderwidth=2)#脊状边缘的
FrameStyle4.place(x=750,y=440,width=200,height=80)
Button(FrameStyle4, text='退出程序',command=ExitSystem).pack(side=BOTTOM, padx="12p",pady="20p")

root.mainloop()
