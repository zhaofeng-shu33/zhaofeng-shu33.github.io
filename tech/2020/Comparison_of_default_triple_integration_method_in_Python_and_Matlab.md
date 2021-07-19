# Comparison of default triple integration method in Python and Matlab
2020/03/22

The backend engine of triple integration is different in Python and Matlab.

In Python we use `scipy.integration.tplquad` to do triple integration; In Matlab the function is called `integral3`.

Also the level of parallelism is different. In Python, it is totally serialized, one evalulation at one integration point each time. However, in Matlab it is highly paralleled. I found a 14 times 14 matrix is passed to the evalulation function. As a result, the evalulation function should support matrix computation.

Because the difference in parallelism, `integral3` is much faster than `scipy.integration.tplquad`.

Another big difference is the convergence result. I use the following example in matlab:

```Matlab
n = 8;
k = 4;
C0 = gamma(n/2) * gamma((n-1)/2) / (gamma(0.5) * gamma(k/2) * gamma((k-1)/2) * gamma((n-k)/2) * gamma((n-k-1)/2));
2 * C0 * integral3(@(x,y,z) (x.*y-z.^2).^((k-3)/2) .* (1-x-y+x.*y-z.^2).^((n-k-3)/2), 0,1,0,1,0,@(x,y) min(sqrt(x.*y), sqrt(1-x-y+x.*y)))
```
The final result is number 1.

However, when I compute the same integral in Python, I cannot get the right result:

```Python
import numpy as np
from scipy.special import gamma
from scipy.integrate import tplquad
n = 8
k = 4
C0 = 2 * gamma(n/2) * gamma((n-1)/2)
C0 /= (gamma(0.5) * gamma(k/2) * gamma((k-1)/2) * gamma((n-k)/2) * gamma((n-k-1)/2))
C0 *= tplquad(lambda x,y,z: abs(x*y-z**2)**((k-3)/2) * abs(1-x-y+x*y-z**2)**((n-k-3)/2),
              0, 1, lambda x: 0, lambda x: 1, lambda x,y: 0,
               lambda x,y: np.sqrt(np.min([x*y,1-x-y+x*y])))[0]
print(C0)
```