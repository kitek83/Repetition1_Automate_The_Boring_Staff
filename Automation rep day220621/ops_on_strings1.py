def picnic(pic_items,leftWidth,rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '#'))\
    for k,v in pic_items.items():

        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth,'-'))



picnic_items = {'cakes':5,'apples':12,'sups':4,'cookies':8000}
picnic(picnic_items,12,6)
picnic(picnic_items,15,8)