from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))


print('This is a script')

from example_package import module1

a, b = 2, 3
print('{} + {} = {}'.format(a, b, module1.add(a, b)))