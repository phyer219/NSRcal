# re-built the result of PhysRevA.97.043626 (2018)



# Parameters

Parameter is in file paramaters.py

- name: name
- noa: numerical or analytical
# NOA 
- noa = num 纯数值(pure numerical).
- noa = ana1 只把 $\delta^p$ 的边界的边界用数值解代替(analytically calculate $\delta^p$ ).
- noa = ana2 直到积分的结果都是解析的, 微分是数值微分(analytically calculate the integral F).
- noa = ana3 对 $\mu$ 的微分也用解析结果(analytically calculate $\mu$ ).


# Order

1. First, set parameters in file paramaters.py.
2. ./cl
3. ./cal
4. python co-energy.py
5. the results is in ./fig/

