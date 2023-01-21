with open('mozbuy_com.py', 'a') as xfile:
    with open('links.coc', 'r') as file:
        x = 0
        for line in file.readlines():
            x += 1
            xfile.write('url{}="{}"'.format(x, line))