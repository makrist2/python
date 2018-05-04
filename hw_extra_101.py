import re

# ^((mfn-)|(afn-)).*(?<!exists)$

li = ['mfn-fulfillable-quantity', 'afn-fulfillable-quantity', 'afn-total-quantity', 'afn-inbound-receiving-quantity',
      'per-unit-volume', 'mfn-listing-exists', 'afn-listing-exists']

for val in li:
        if re.search('^((mfn-)|(afn-)).*(?<!exists)$', val):
            print('yes')
        else:
           print('no')