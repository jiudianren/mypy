# coding=gbk

#Ԫ��

#��̬���Ժ;�̬�������Ĳ�ͬ�����Ǻ�������Ķ��壬���Ǳ���ʱ����ģ���������ʱ��̬�����ġ�

def fn(self, name='world'): # �ȶ��庯��
    print('Hello, %s.' % name)


'''
type()�������δ���3��������
class�����ƣ�
�̳еĸ��༯�ϣ�ע��Python֧�ֶ��ؼ̳У����ֻ��һ�����࣬������tuple�ĵ�Ԫ��д����
class�ķ��������뺯���󶨣��������ǰѺ���fn�󶨵�������hello�ϡ�
'''

Hello = type('Hello', (object,), dict(hello=fn)) # ����Hello class
h = Hello()
h.hello()

'''
metaclass
����ʹ��type()��̬���������⣬Ҫ������Ĵ�����Ϊ��������ʹ��metaclass��
'''