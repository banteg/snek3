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

### Continued Development
The Struct definitions from snek3 have been adopted and extended in the [evmspec](https://github.com/BobTheBuidler/evmspec) library
