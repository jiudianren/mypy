# coding=gbk

#�ܶ�ʱ�����ݶ�д��һ�����ļ���Ҳ�������ڴ��ж�д��
#StringIO����˼��������ڴ��ж�дstr��


from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#���Ҫ�������������ݣ�����Ҫʹ��BytesIO

from io import BytesIO
f = BytesIO()
f.write('����'.encode('utf-8'))
print(f.getvalue())