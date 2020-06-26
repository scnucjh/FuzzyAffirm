
class Rule:
    '''
规则类：


规则的一般形式为：

IF w1 P1 ^ w2 P2 ^ ... ^ w_n p_n
Then Q(CF,alpha)

CF 表示 该规则的可信度

alpha 表示应用阈值
alpha \\in [-1,1]

条件则是多个二元组的集合，每个元素是(w_i,P_i)
表示的是： w_i 为 P_i 的权重, 即前件断言 P_i 对 Q 的影响程度
在类成员函数中为conditions数组

当规则的前件可信度 Sigma >= a 时, 该规则才可用

为了使推理过程简单, 在诊断规则的前提条件中将只考虑各模糊断言之间的与 (^) 运算关系, 不考虑或
(V) 运算关系。 

而“V”运算可分成多个“^”运算来表示。

    '''

    conditions = []
    CF = 0
    alpha = 0
    result = ''
    
    def __init__(self,conditions=[]):
        self.conditions = conditions

    
    # 给当前规则添加前提条件

    def add_precondition(self,a,b):
        self.conditions.append([a,b])

    # 设置当前规则的CF值

    def set_CF(self, value):
        self.CF = value


    # 设置当前规则的alpha值

    def set_alpha(self,value):
        self.alpha = value


    # 设置当前规则的判别事件
    
    def set_resule(self,value):
        self.result = value

    # 判定该规则是否被激活

    def can_be_use(self,state):
        Sigma = 0.0
        for c in self.conditions:
            for s in state:
                if c[0]==s[0]:
                    Sigma += c[1]*s[1]
        if Sigma >= self.alpha:
            return True
        else :
            return False

    def get_Sigma(self,state):
        Sigma = 0.0
        for c in self.conditions:
            for s in state:
                if c[0]==s[0]:
                    Sigma += c[1]*s[1]
        return Sigma
