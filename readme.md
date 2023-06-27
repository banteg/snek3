# eth api spec

[msgspec](https://jcristharif.com/msgspec/) definitions of ethereum [execution apis](https://github.com/ethereum/execution-apis)

## usage

```python
from snek3 import Snek3
import rich

s = Snek3()

block = s.get_block('latest', True)
rich.print(block)
```
