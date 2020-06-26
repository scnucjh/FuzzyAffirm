import Rule
import Rule_set


rs = Rule_set.get_rule_set()

# for x in rs:
#     print(x.conditions,x.CF,x.alpha,x.result)

state = [
    ['水处理不合格',0.0],
    ['受热管局部汽化',0.0],    
    ['排污不及时',0.0],    
    ['对流管束积灰',0.9],    
    ['水冷壁管结焦',0.0],    
    ['清垢处理不及时',0.92],    
    ['清灰处理不及时',0.8],    
    ['受热管结垢',0.85],    
    ['传热热阻增大',0.0],    
]

# print(state)

result = ''
CF = []
Sigma = []

for i in range(0,4):
    if rs[i].can_be_use(state):
        Sigma.append( rs[i].get_Sigma(state) )
        result = rs[i].result
        print( '规则',i,'被激活',
        '前件置信度为：',
        Sigma[-1] )

        CF.append(rs[i].CF)

sum = 0.0
for x in CF:
    sum += x

for i in range(len(CF)):
    CF[i] /= sum
    print(CF[i])


beta = 0.0

for i in range(len(CF)):
    beta += CF[i] * Sigma[i]

print('结论是 ： ', result)
print('可信度为 ： ',beta)