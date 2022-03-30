from DynamicHtml import DynamicHtml

if __name__ == '__main__':
    content = DynamicHtml('https://www.google.com/search?q=cats&sxsrf=APq-WBundIDbI9LaEcV9oPPo3JNrmEz5ZA:1648600645206&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjDz9X-y-z2AhWqDEQIHZasBcoQ_AUoAXoECAIQAw&biw=1920&bih=941&dpr=1#imgrc=0V922RrJgQc9SM')
    htmlFile = open('testHtml.html', 'w')
    htmlFile.write(content)
    htmlFile.close()